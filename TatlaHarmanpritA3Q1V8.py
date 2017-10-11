# -*- coding: utf-8 -*-
"""TatlaHarmanpritA3Q1
￼￼

COMP 1012 SECTION A01
INSTRUCTOR Terrance H. Andres
ASSIGNMENT: A3 Question 1
AUTHOR Harmanprit Tatla
VERSION 2015 - February - 24

PURPOSE: To generate a full year's calendar for any year from 1900 to 9999, 
using excel dates, functions, unicode characters, and more. 
"""
#Imports
import time
import math

def calcExcelDate(year, month):
    """Returns an integer excel date that refers to the given
       year (1900 to 9999) and month (1 to 12), with day = 1."""
    
    DAYS_IN_YEAR  = 365 #num of whole days in year [day]
    
    y2_after1900  = year - 1900 #year difference [year]
   
    #if an early month, treat it as part of previous year [year]
    em_earlyMonth = (14 - month) // 12
   
    yearAdj = y2_after1900 - em_earlyMonth #adjustment [year]   
    
    m2_monthAdj = month + 12 * em_earlyMonth #adjustment [month] 
    
    #count the number of leap years [year]
    l_leapYears   = ( 1 + min(yearAdj,0) + yearAdj // 4 
                      - yearAdj // 100 + (yearAdj + 300) // 400 )
    
    #num of days preceding given month in non-leap year [day]
    d1_daysToMonth  = math.floor(-1.63 + (m2_monthAdj - 1) * 30.6) 
    
    #Calculates excel date for given month and year with day = 1 [day]
    excelDate = 1 + yearAdj * DAYS_IN_YEAR + l_leapYears + d1_daysToMonth 
    
    return int(excelDate)

def calcWeekDay(excelDate):
    """ Given an integer excel date, returns the calendar day it refers to,
        as an integer between 0 - 6, where 0 = Sunday and 6 = Saturday. """
    
    #Constants
    DAYS_IN_WEEK = 7 #num of days in a week 
    ADJUSTMENT = 1 #Adjusts computed calendar day 
    #Used to adjust calendar day when it = -1 to 6 for Saturday. 
    SATURDAY_FIX = -1 
    
    #Computes calendar day excel date refers to
    calendarDay = (excelDate % DAYS_IN_WEEK) - ADJUSTMENT 
    
    #If calendarDay = -1 adjusts its value to 6 for Saturday 
    #otherwise, it assigns calendarDay to dayInWeek
    dayInWeek = calendarDay + DAYS_IN_WEEK * (calendarDay == SATURDAY_FIX) 
    
    return dayInWeek 

def daysInMonth (year, month):
    """Given a year (1900 - 9999) and month (1 - 12), returns the number of 
       days in that month, using integer excel dates"""
    
    #excel date for given month and year [days]
    date1 = calcExcelDate(year, month) 
    
    #excel date for next month and given year [days]
    date2 = calcExcelDate(year, month + 1) 
    
    #computes num of days in month [days]
    numDays = date2 - date1 
      
    return numDays
print daysInMonth(2016, 12)
def listMonthDays(year):
    """Given a year, returns a 13 item list, which contains the year followed
       by the month details of each month enclosed in two element tuples."""
    
    #Variables & Constants needed in following blocks of code.
    #12 months in year beginning with January
    MONTHS = ('JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE',
              'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER')
              
    #Later used to assign either '  1' or '(star)1' as first day for each month 
    FIRST_DAY = ['%3s' % '1', U"\N{BLACK STAR}" + '1']
    #Used to replace first day in January and July with '(star)1'
    JAN, JUL = 1, 7 
    
    monthDetails = [year] #Later holds month details for each month
    #Max num of entries for monthInfo list, as 6 part weeks * 7 day/week = 42  
    MONTH_MAX = 42 
    
    #Computes the month details for all 12 months, beginning with January 
    for month in range(1, len(MONTHS) + 1):
        
        #Computes calendar day the excel date of year and month, refers to.
        dayOfWeek = calcWeekDay(calcExcelDate(year, month)) 
        
        #Computes num of days in month for given year [days]
        daysOfMonth = daysInMonth(year, month) 
        
        #Creates list of blanks used to line up first day of month to corrrect
        #calendar day, then creates list of days of that month 
        monthInfo = (['%3s' % '' for num in range(dayOfWeek)] +
                     ['%3d' % num for num in range (1, daysOfMonth + 1)])
              
        #Adds blanks to end of monthInfo until total entries in 
        #monthInfo > MONTH_MAX
        while len(monthInfo) < MONTH_MAX:
            monthInfo += ['%3s' % '']
        
        #Replaces first day of January and July  with '(star)1', and all other
        #months with '  1'
        monthInfo[dayOfWeek] = FIRST_DAY[(month is JAN) or (month is JUL)] 
        
        #Appends tuple containing month name and its monthInfo to list
        #month name is in position month - 1 in MONTHS
        monthDetails.append((MONTHS[month -1], monthInfo)) 
       
    return monthDetails 

def formatCalendar(monthDetail):
    """ Given the monthDetail for any month, as a two entry tuple, which has 
        as its first entry the month name as a single character string, and 
        second entry, a 42 entry list comprising the days of that month, 
        returns, a formatted multi-line calendar for that month, as a single 
        character string.
        """
    
    strMonth = monthDetail[0] #0 as month name in 0th position in monthDetail
    listDays = monthDetail[1] #1 as list of days in 1st position in monthDetail
    
    #Variables & Constants needed in following blocks of code.
    WEEK = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat') #Days of week 
    strDays = '' #Later holds days of month as single character string
    count = 0 #Counter 
    DAYS_IN_WEEK = 7 #Num of days in week
    PART_WEEKS = 6 #Max num of part weeks in a month
    #Vertical bar for monthly calendar
    VLINE = '%s' % U"\N{BOX DRAWINGS HEAVY VERTICAL}" 
    
    #Creates 7 entry list for each part week in month, then converts to string,
    #adds appropriate spacing, vertical bars, and new line character at end.
    for num in range(PART_WEEKS):
        strDays += (VLINE + '%1s' % ''  + '  '.join(listDays[count: 
                    DAYS_IN_WEEK + count])  + '%2s' % '' +  VLINE + '\n')
        
        count += DAYS_IN_WEEK
    
    #Controls formatting for month, week, and day of monthly calendar     
    MONTH_FORMAT = ' %-35s' % strMonth
    WEEK_FORMAT = ' %-35s' % '  '.join(WEEK)
    DAY_FORMAT =  '%-s' % strDays
    
    #Controls formatting for horiz line above and below monthly calendar
    LENGTH = 18 #controls horizontal line length 
    HORIZ_TOP = '%18s' % (U"\N{BOX DRAWINGS HEAVY HORIZONTAL}" * LENGTH)
    HORIZ_BOT = '%18s' % (U"\N{BOX DRAWINGS HEAVY HORIZONTAL}" * LENGTH)
    
    #Controls formatting for corners of monthly calendar
    TOP_L_CORN = '%s' % U"\N{BOX DRAWINGS HEAVY DOWN AND RIGHT}" 
    TOP_R_CORN = '%s' % U"\N{BOX DRAWINGS HEAVY DOWN AND LEFT}"
    BOT_L_CORN = '%s' % U"\N{BOX DRAWINGS HEAVY UP AND RIGHT}"
    BOT_R_CORN = '%s' % U"\N{BOX DRAWINGS HEAVY UP AND LEFT}"
    
    #Formatted multi-line monthly calendar as a single character string 
    formattedMonth =   (TOP_L_CORN + HORIZ_TOP + TOP_R_CORN + '\n' + VLINE + 
                        MONTH_FORMAT + VLINE + '\n' + VLINE + WEEK_FORMAT + 
                        VLINE + '\n' + DAY_FORMAT + BOT_L_CORN + HORIZ_BOT + 
                        BOT_R_CORN) 
               
    return formattedMonth
    
def theEnd():
    """Prints termination message to indicate succesful completion of 
       program."""
    
    print '\nProgrammed by Harmanprit Tatla'
    print 'Date:', time.ctime()
    print 'End of processing...' 
    
    return    

YEAR = 2015 #year to make calendar 
monthDetails = listMonthDays(YEAR) #details for each month 
print '%64s' % " ".join(str(YEAR)) #prints the year double spaced and centred

#Calls formatCalendar once for each month in order to create full year calendar 
for month in range (1, 13, 3):
    left = formatCalendar(monthDetails[month]).split('\n')
    centre = formatCalendar(monthDetails[month + 1]).split('\n')
    right = formatCalendar(monthDetails[month+2]).split('\n')
    for row in range (len(left)):
        print '%s %s %s' % (left[row], centre[row], right[row])

theEnd()