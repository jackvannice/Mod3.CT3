#Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
#If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
#Write a Python program to solve the general version of the above problem.
#Ask the user for the time now (in hours) and then ask for the number of hours to wait for the alarm.
#Your program should output what the time will be on a 24-hour clock when the alarm goes off.

#create the list that mimics the 24 hr "clock"
clock = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

#get inputs for time now and alarm
time_now_input = int(input('Enter the time in hours (from 0 to 23): '))
alarm_input = int(input('How many hours until you would like your alarm to go off?: '))

#determine the position of time now in the "clock" list
time_now_index = clock.index(time_now_input)

#loop through the "clock" list as many times as "alarm input" requires
for i in range(alarm_input):
    time_now_index += 1
    if time_now_index == 24:
        time_now_index = 0

#return the alarm time based on the new time_now_index
alarm_time = clock[time_now_index]
print('Alarm time: ', alarm_time)
