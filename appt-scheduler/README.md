# Appointment Scheduler

Given the calendars of two people, return a list of available 1 hour appointment times that would work for both people. Each calendar is a list of tuples of a starting time and ending time in military time. You are also given the earliest and latest times each person is available and the available appointments you return should be within these limits.

**Example Input**

`person_1_cal = [['8:00', '9:00'], ['10:00', '10:30'], ['4:00', '5:00']]`

`person_2_cal = [['8:00', '9:00'], ['10:00', '11:30'], ['2:30', '3:00'], ['3:30', '4:00']]`

`availability_bounds = ['07:00', '18:30']`

`find_appointment_times(person_1_cal, person_2_cal, availability_bounds)`

**Expected Output**

You should return potential appointment times in 30 minute increments (on the hour and half hour).

`[
    ['9:00', '10:00'], ['11:30', '12:30'], ['12:00', '1:00'], ['12:30', '1:30'],
    ['1:00', '2:00'], ['1:30', '2:30'], ['5:00', '6:00'], ['5:30', '6:30']
]`