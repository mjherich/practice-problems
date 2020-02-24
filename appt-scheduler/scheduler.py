import math


def find_appointment_times(person_1_cal, person_2_cal, availability_bounds):
    """
    Finds available appointment times given two calendars and bounds.
    """
    # Helper function to translate string times into decimal
    def ttd(time):
        hour, minute = time.split(":")
        if minute == "30":
            return int(hour) + 0.5
        else:
            return int(hour)
    

    # Helper function to translate decimal times to string
    def dtt(dec):
        hour = math.floor(dec)
        minute = str(dec).split(".")[1]
        if minute == "5":
            return f"{hour}:30"
        else:
            return f"{hour}:00"

    
    # Helper to check if potential appointment would conflict with current appointments
    # Returns True if no conflicts
    def does_not_conflict(start_time, end_time):
        pass

    # Destructure availability_bounds
    earliest_availability, latest_availability = availability_bounds
    latest_availability = ttd(earliest_availability)

    # Initialize potential_start_time to be be first bound
    potential_start_time = ttd(earliest_availability)
    # Initialize valid_appts to keep track of appointments that work for both people
    valid_appts = []

    # Loop with end condition when potential_start_time is after latest availability
    while potential_start_time <= latest_availability - 1:
        # Set potential_end_time to be an hour after potential_start_time
        potential_end_time = potential_start_time + 1

        # Check to see if there are any conflicts with the two calendars
        if does_not_conflict(potential_start_time, potential_end_time):
            valid_appts.append([dtt(potential_start_time), dtt(potential_end_time)])

        # Add 30 minutes to potential_start_time
        potential_start_time += 0.5
    
    return valid_appts


# Test it
person_1_cal = [['8:00', '9:00'], ['10:00', '10:30'], ['4:00', '5:00']]
person_2_cal = [['8:00', '9:00'], ['10:00', '11:30'], ['2:30', '3:00'], ['3:30', '4:00']]
availability_bounds = ['7:00', '18:30']
print(find_appointment_times(person_1_cal, person_2_cal, availability_bounds))