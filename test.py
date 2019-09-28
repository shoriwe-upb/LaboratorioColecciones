from laboratory import main, local_results, Analisys
from random import choice
from itertools import permutations

departments = ("Capital District", "Amazonas", "Antioquia", "Arauca", "Atlantico", "Bolívar", "Boyaca", "Caldas",
               "Caqueta", "Casanare", "Cauca", "Cesar", "Choco", "Cordoba", "Cundinamarca", "Guainia", "Guaviare",
               "Huila", "La Guajira", "Magdalena", "Meta", "Nariño", "Norte de Santander", "Putumayo", "Quindío",
               "Risaralda", "San Andres y Providencia", "Santander", "Sucre", "Tolima", "Valle del Cauca", "Vaupes",
               "Vichada")

file = open("test.txt", "w")
for number in range(20):
    file.write(f"+++++++++ Cicle {number + 1} +++++++++\n")
    for method in dir(Analisys)[26:]:
        if method == "department_med":
            arg = choice(departments)
        elif method in ("med_of_most_hot_month_of_departments", "most_hot_med"):
            arg = ",".join(choice(tuple(permutations(departments, 3))))
        else:
            arg = None
        args = {"OPTION": method, "FILE": "tests/db.csv", "ARG": arg}

        main(args)
        if len(local_results):
            result = local_results.pop()
        else:
            result = "Error"
        file.write(f"\t{'-'*9}\n\tMethod: {method}\n\tARG: {arg}\n\tResult: {result}\n\t{'-'*9}\n\n")