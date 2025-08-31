#Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
#If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
#Write a Python program to solve the general version of the above problem.
#Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm.
#Your program should output what the time will be on a 24-hour clock when the alarm goes off.

clock = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
time_now_input = int(input('Enter the time in hours (from 0 to 23): '))
alarm_input = int(input('How many hours until you would like your alarm to go off?: '))
