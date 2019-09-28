from custom_functions.temperature_methods import load_data_from_file, Analisys
from random import choice
from statistics import mean
from itertools import permutations
from unittest import TestCase
from unittest import main as main_test
from numpy import std


class TestScript(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestScript, self).__init__(*args, **kwargs)
        self.__departments = (
            "Capital District", "Amazonas", "Antioquia", "Arauca", "Atlantico", "Bolívar", "Boyaca", "Caldas",
            "Caqueta", "Casanare", "Cauca", "Cesar", "Choco", "Cordoba", "Cundinamarca", "Guainia", "Guaviare",
            "Huila", "La Guajira", "Magdalena", "Meta", "Nariño", "Norte de Santander", "Putumayo", "Quindío",
            "Risaralda", "San Andres y Providencia", "Santander", "Sucre", "Tolima", "Valle del Cauca", "Vaupes",
            "Vichada")

        self.__analiser = Analisys(load_data_from_file("test/db.csv"))

    def test_department_med(self):
        department = choice(self.__departments)
        result_from_analisys = self.__analiser.department_med(department)[1]
        correct_result = mean(self.__analiser._data[department])
        self.assertEqual(result_from_analisys, correct_result)

    def test_national_med(self):
        result_from_analisys = self.__analiser.national_med(None)[1]
        correct_result = sum(mean(self.__analiser._data[key]) for key in self.__analiser._data.keys()) / len(
            self.__analiser._data.keys())
        self.assertEqual(result_from_analisys, correct_result)

    def test_most_hot(self):
        result_from_analisys = tuple(value[2] for value in self.__analiser.most_hot(None))
        correct_result = tuple(max(self.__analiser._data[key]) for key in self.__analiser._data.keys())
        self.assertEqual(result_from_analisys, correct_result)

    def test_med_of_most_hot_month_of_departments(self):
        departments = choice(tuple(permutations(self.__departments, 3)))
        result_from_analisys = self.__analiser.med_of_most_hot_month_of_departments(",".join(departments))[1]
        correct_result = mean(max(self.__analiser._data[department]) for department in departments)
        self.assertEqual(result_from_analisys, correct_result)

    def test_most_hot_med(self):
        departments = choice(tuple(permutations(self.__departments, 3)))
        result_from_analisys = self.__analiser.most_hot_med(",".join(departments))[1]
        correct_result = max(mean(self.__analiser._data[department]) for department in departments)
        self.assertEqual(result_from_analisys, correct_result)

    def test_most_hot_month_of_year(self):
        result_from_analisys = self.__analiser.most_hot_month_of_year(None)[2]
        correct_result = max(max(self.__analiser._data[key]) for key in self.__analiser._data.keys())
        self.assertEqual(result_from_analisys, correct_result)

    def test_standard_deviation(self):
        result_from_analisys = tuple(result[1] for result in self.__analiser.standard_deviation(None))
        correct_result = tuple(std(self.__analiser._data[key]) for key in self.__analiser._data.keys())

        number_of_departments = len(self.__analiser._data.keys())
        index = 0

        while index < number_of_departments:
            self.assertAlmostEqual(result_from_analisys[index], correct_result[index], delta=0.5)
            index += 1


if __name__ == '__main__':
    main_test()
