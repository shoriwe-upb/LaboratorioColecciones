# Function to print the help message when the user give parameters to a function that don't have
def _default_help_no_args():
    return 'This option don\'t have arguments'


def load_data_from_file(file_path):
    file = open(file_path)
    lines = file.readlines()
    file.close()
    data = {}
    for line in lines:
        department, values = line.strip().split(',')
        data[department] = tuple(map(lambda value: float(value), values.split(';')))
    return data


# Handler for the functions
class Analisys(object):
    def __init__(self, data: dict):
        self._data = data
        # Reference to return month outputs by they name
        self.__ref = (
            'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
            'november',
            'dicember')

    # Calculate department med temperature of a specific department
    def department_med(self, department_name):
        if department_name == 'help' or not department_name:
            return "You need to specify the department name"
        return department_name, sum(self._data[department_name]) / len(self._data[department_name])

    # Calculate the national temperature med
    def national_med(self, no_arg):
        if no_arg:
            return _default_help_no_args()
        return "National", sum(self.department_med(key)[1] for key in self._data.keys()) / len(self._data.keys())

    # return the most hot month of every department
    def most_hot(self, no_arg):
        if no_arg:
            return _default_help_no_args()
        for key in self._data.keys():
            most_hot_month = max(self._data[key])
            month = self.__ref[self._data[key].index(most_hot_month)]
            yield key, month, most_hot_month

    # Calculate the med betwen the most hot month of three user specified departments
    def med_of_most_hot_month_of_departments(self, departments):
        if departments == "help" or not departments:
            return "Comma separated names of the departments"
        departments = departments.split(",")
        return departments, sum(max(self._data[department]) for department in departments) / len(departments)

    # Calculate the med of all departments and return the higher one
    def most_hot_med(self, departments):
        if departments == "help" or not departments:
            return "Comma separated names of the departments"
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
            return _default_help_no_args()
        for key in self._data.keys():
            number_observations = len(self._data[key])
            med = sum(self._data[key]) / number_observations
            yield key, ((sum((value - med) ** 2 for value in self._data[key]) / number_observations - 1) ** (1/2))
