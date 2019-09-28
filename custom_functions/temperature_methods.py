# Function to print the help message when the user give parameters to a function that don't have
def _default_help_no_args():
    return 'This option don\'t have arguments'


# Handler for the functions
class Analisys(object):
    def __init__(self, data: dict):
        self.__data = data
        # Reference to return month outputs by they name
        self.__ref = (
            'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
            'november',
            'dicember')

    # Calculate department med temperature of a specific department
    def department_med(self, department_name):
        if department_name == 'help' or not department_name:
            return "You need to specify the department name"
        else:
            return department_name, sum(self.__data[department_name]) / len(self.__data[department_name])

    # Calculate the national temperature med
    def national_med(self, no_arg):
        if no_arg:
            return _default_help_no_args()
        else:
            return "National", sum(self.department_med(key)[1] for key in self.__data.keys()) / len(self.__data.keys())

    # return the most hot month of every department
    def most_hot(self, no_arg):
        if no_arg:
            return _default_help_no_args()
        else:

            for key in self.__data.keys():
                most_hot_month = max(self.__data[key])
                month = self.__ref[self.__data[key].index(most_hot_month)]
                yield key, month, most_hot_month

    # Calculate the med betwen the most hot month of three user specified departments
    def med_of_most_hot_month_of_departments(self, departments):
        if departments == "help" or not departments:
            return "Comma separated names of the departments"
        else:
            departments = departments.split(",")
            return departments, sum(max(self.__data[department]) for department in departments) / len(departments)

    # Calculate the med of all departments and return the higher one
    def most_hot_med(self, departments):
        if departments == "help" or not departments:
            return "Comma separated names of the departments"
        else:
            departments = departments.split(",")
            return max((self.department_med(department) for department in departments), key=lambda value: value[1])

    # Return the department, month, temperature of all the year
    def most_hot_month_of_year(self, no_arg):
        if no_arg:
            return _default_help_no_args()
        return max(self.most_hot(None), key=lambda value: value[2])

    # Calculate the standard deviation of all states
    def standard_deviation(self, no_arg):
        # Really i dont know f this is the right formula
        if no_arg:
            _default_help_no_args()
        for key in self.__data.keys():
            number_observations = len(self.__data[key])
            med = sum(self.__data[key]) / number_observations
            yield key, ((sum((value - med) ** 2 for value in self.__data[key]) / number_observations - 1) ** (1/2))
