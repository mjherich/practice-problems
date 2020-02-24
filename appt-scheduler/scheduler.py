
def find_appointment_times(person_1_cal, person_2_cal, availability_bounds):
    """
    Finds available appointment times given two calendars and bounds.
    """
    # Destructure availability_bounds

    # Initialize potential_start_time to be be first bound
    # Initialize valid_appts to keep track of appointments that work for both people

    # Loop with end condition when potential_start_time is after latest availability
        # Set potential_end_time to be an hour after potential_start_time
        # Check to see if there are any conflicts with the two calendars
            # If False, then add to valid_appts
        # Add 30 minutes to potential_start_time
    pass



# Test it
person_1_cal = [['8:00', '9:00'], ['10:00', '10:30'], ['4:00', '5:00']]
person_2_cal = [['8:00', '9:00'], ['10:00', '11:30'], ['2:30', '3:00'], ['3:30', '4:00']]
availability_bounds = ['07:00', '18:30']
print(find_appointment_times(person_1_cal, person_2_cal, availability_bounds))