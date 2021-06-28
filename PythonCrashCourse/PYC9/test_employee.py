import unittest
from employee import Employee

class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.employee=Employee("Daniel","Florek",5000)

    def test_give_default_rise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary,10000)

    def test_give_custom_rise(self):
        self.employee.give_raise(7000)
        self.assertEqual(self.employee.annual_salary, 12000)


if __name__ == '__main__':
    unittest.main()
