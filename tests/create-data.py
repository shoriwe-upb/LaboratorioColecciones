from random import randint


def create_line(department):
    a = 19
    b = 30
    if department in ("Capital District", ):
        a = 7
        b = 20
    elif department in ("La Guajira", "Amazonas"):
        a = 29
        b = 50
    return f"{department},{';'.join(str(randint(a, b)) for n in range(12))}\n"


departments = ("Capital District", "Amazonas", "Antioquia", "Arauca", "Atlantico", "Bolívar", "Boyaca", "Caldas",
               "Caqueta", "Casanare", "Cauca", "Cesar", "Choco", "Cordoba", "Cundinamarca", "Guainia", "Guaviare",
               "Huila", "La Guajira", "Magdalena", "Meta", "Nariño", "Norte de Santander", "Putumayo", "Quindío",
               "Risaralda", "San Andres y Providencia", "Santander", "Sucre", "Tolima", "Valle del Cauca", "Vaupes",
               "Vichada")


file = open("db.csv", "w")
for department in departments:
    file.write(create_line(department))
file.close()
