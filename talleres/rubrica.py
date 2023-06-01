# Leer 10 numeros: Mayor, pares, impares, suma pares, suma impares, promedio pares, promedio impares
numbers = []
for i in range(10):
  num = int(input("Ingrese el numero "+ str(i+1)+ ": "))
  while (num == 0):
    num = int(input("ERROR: por favor ingrese un numero distinto de 0..."))
  numbers.append(num)

even = []
odd = []
for num in numbers:
  if (num%2 == 0):
    even.append(num)
  else:
    odd.append(num)

sum_even = 0
for num in even:
  sum_even += num

sum_odd = 0
for num in odd:
  sum_odd += num

prom_even = sum_even / len(even)
prom_odd = sum_odd / len(odd)

print("Pares: ", even)
print("Impares: ", odd)
print("Suma Pares: ", sum_even)
print("Suma Impares: ", sum_odd)
print("Promedio Pares: ", prom_even)
print("Promedio Impares: ", prom_odd)