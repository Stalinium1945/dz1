#Задача 5: Уровень - решатель.

#Условие: На вход вашей программе в стандартном вводе даны действительные коэффициенты A, B и C уравнения Ax² + Bx + C = 0. 
#Выведите все его различные действительные корни в любом порядке. 
#Гарантируется, что хотя бы один из коэффициентов не равен нулю.

a=int(input("Введите число А "))
b=int(input("Введите число B "))
c=int(input("Введите число C "))

from math import sqrt
D=(b**2 - 4*a*c)
x1=(-b+sqrt(D))/(2*a)
x2=(-b-sqrt(D))/(2*a)
if D > 0:
        print("Корни уравнения равны x1: ", x1 ," x2: ", x2)    
elif ( D == 0 ):
        print("Корень уравнения равен ", x1)
elif D<0:
        print("Нет корней")