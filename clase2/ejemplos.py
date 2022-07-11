# calculando la raíz cuadrada
user_input = input("Ingrese un valor: ")
number = int(user_input)
sqrt_number = number**0.50
print("La raíz cuadrada es: " + str(sqrt_number))

# ecuación cuadrática
# 0 = ax^2 + bx + c
# x1 = (-b + (b^2 - 4ac)^0.5))/2a
# x2 = (-b - (b^2 - 4ac)^0.5))/2a
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
root1 = ( -b + (b**2 - 4*a*c)**0.5)/(2*a)
root2 = ( -b - (b**2 - 4*a*c)**0.5)/(2*a)
print("raiz 1: " + str(root1))
print("raiz 2: " + str(root2))

# intercambiando variables
x = 1
y = 2
print(x, y)
temporal = y
y = x
x = temporal
print(x, y)