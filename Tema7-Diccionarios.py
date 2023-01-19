miDiccionario = {
    "Matricula": 20001399, 
    "Apellidos": "Aguilera"
    }
print(miDiccionario["Apellidos"])
miDiccionario["Materia"] = "DWP"
print(miDiccionario)
miDiccionario["Matricula"] = 98765
print(miDiccionario)
del miDiccionario["Apellidos"]
print(miDiccionario)