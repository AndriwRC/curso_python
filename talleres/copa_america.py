# Diseñe un algoritmo que determine el campeón de la copa América.
print("¡¡¡TORNEO COPA AMERICA!!!")
print("*** CUARTOS DE FINAL ***")

# Partido 1: Brasil vs Chile
seleccion = int(input("Ingresa el ganador del Partido Brasil VS Chile:\n1. Brasil\n2. Chile\n"))
if (seleccion == 1):
  ganadorP1 = 'Brasil'
else:
  ganadorP1 = 'Chile'
print(f"{ganadorP1} Clasifica a la semifinal!\n")

# Partido 2: Argentina vs Venezuela
seleccion = int(input("Ingresa el ganador del Partido Argentina VS Venezuela:\n1. Argentina\n2. Venezuela\n"))
if (seleccion == 1):
  ganadorP2 = 'Argentina'
else:
  ganadorP2 = 'Venezuela'
print(f"{ganadorP2} Clasifica a la semifinal!\n")

# Partido 3: Peru vs Paraguay
seleccion = int(input("Ingresa el ganador del Partido Peru VS Paraguay:\n1. Peru\n2. Paraguay\n"))
if (seleccion == 1):
  ganadorP3 = 'Peru'
else:
  ganadorP3 = 'Paraguay'
print(f"{ganadorP3} Clasifica a la semifinal!\n")

# Partido 4: Uruguay vs Colombia
seleccion = int(input("Ingresa el ganador del Partido Uruguay VS Colombia:\n1. Uruguay\n2. Colombia\n"))
if (seleccion == 1):
  ganadorP4 = 'Uruguay'
else:
  ganadorP4 = 'Colombia'
print(f"{ganadorP4} Clasifica a la semifinal!\n")

print("*** SEMIFINALES ***")
print(f"{ganadorP1}, {ganadorP2}, {ganadorP3} y {ganadorP4} clasificaron a la semifinal!")

# Semifinal 1: GanadorP1 vs GanadorP3
seleccion = int(input(f"Ingresa el ganador de la semifinal {ganadorP1} VS {ganadorP3}:\n1. {ganadorP1}\n2. {ganadorP3}\n"))
if (seleccion == 1):
  ganador_semi_1 = ganadorP1
  perdedor_semi_1 = ganadorP3
else:
  ganador_semi_1 = ganadorP3
  perdedor_semi_1 = ganadorP1
print(f"{ganador_semi_1} clasifica a la final!\n")

# Semifinal 2: GanadorP2 vs GanadorP4
seleccion = int(input(f"Ingresa el ganador de la semifinal {ganadorP2} VS {ganadorP4}:\n1. {ganadorP2}\n2. {ganadorP4}\n"))
if (seleccion == 1):
  ganador_semi_2 = ganadorP2
  perdedor_semi_2 = ganadorP4
else:
  ganador_semi_2 = ganadorP4
  perdedor_semi_2 = ganadorP2
print(f"{ganador_semi_2} clasifica a la final!\n")

print("*** TERCER LUGAR ***")
# Tercer lugar: perdedor_semi_1 vs perdedor_semi_2
seleccion = int(input(f"Ingresa el ganador del partido por el tercer puesto:\n1. {perdedor_semi_1}\n2. {perdedor_semi_2}\n"))
if (seleccion == 1):
  tercer_lugar = perdedor_semi_1
else:
  tercer_lugar = perdedor_semi_2
print(f"{tercer_lugar} se queda con el tercer lugar!\n")

print("*** FINAL DE LA COPA AMERICA ***")
seleccion = int(input(f"Ingresa el ganador del partido final:\n1. {ganador_semi_1}\n2. {ganador_semi_2}\n"))
if (seleccion == 1):
  ganador = ganador_semi_1
  perdedor = ganador_semi_2
else:
  ganador = ganador_semi_2
  perdedor = ganador_semi_1
print(f"{ganador} ES EL CAMPEON!!!")
print(f"{perdedor} es subcampeon!")

print("*** FIN DEL TORNEO ***")