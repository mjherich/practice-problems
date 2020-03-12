import unittest
from scheduler import find_appointment_times

class Test(unittest.TestCase):

    def test_case_1(self):
        person_1_cal = [['8:00', '9:00'], ['10:00', '10:30'], ['16:00', '17:00']]
        person_2_cal = [['10:00', '11:30'], ['14:30', '15:00'], ['15:30', '16:00']]
        availability_bounds = ['7:00', '18:30']
        expected_output = [['7:00', '8:00'], ['9:00', '10:00'], ['11:30', '12:30'], ['12:00', '13:00'], ['12:30', '13:30'],
    ['13:00', '14:00'], ['13:30', '14:30'], ['14:00', '15:00'], ['15:00', '16:00'], ['17:00', '18:00'], ['17:30', '18:30']]
        self.assertEqual(find_appointment_times(person_1_cal, person_2_cal, availability_bounds), expected_output)
  

if __name__ == '__main__':
    unittest.main()