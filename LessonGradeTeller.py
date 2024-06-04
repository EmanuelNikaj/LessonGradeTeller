# Import any needed libraries
import sys

# Constants
A = 5
message1 = 'the lesson with the highest grade is '
message2 = 'and the lesson with the lowest grade is'
message3 = 'you have been disquilified from this/these lesson/lessons'
message4 = 'you have been quilified in this/these lesson/lessons'

# Variables
mathima_1 = input('please enter your mathima_1: ')
mathima_2 = input('please enter your mathima_2: ')
mathima_3 = input('please enter your mathima_3: ')
mathima_4 = input('please enter your mathima_4: ')

mathimatos_1 = float(input('grade mathimatos_1: '))
mathimatos_2 = float(input('grade mathimatos_2: '))
mathimatos_3 = float(input('grade mathimatos_3: '))
mathimatos_4 = float(input('grade mathimatos_4: '))

print()
print(message1)
if mathimatos_1 > mathimatos_2 and mathimatos_1 > mathimatos_3 and mathimatos_1 > mathimatos_4:
    print(mathima_1)
if mathimatos_2 > mathimatos_3 and mathimatos_2 > mathimatos_4 and mathimatos_2 > mathimatos_1:
    print(mathima_2)
if mathimatos_3 > mathimatos_4 and mathimatos_3 > mathimatos_1 and mathimatos_3 > mathimatos_2:
    print(mathima_3)
if mathimatos_4 > mathimatos_1 and mathimatos_4 > mathimatos_2 and mathimatos_4 > mathimatos_3:
    print(mathima_4)

print(message2)
if mathimatos_1 < mathimatos_2 and mathimatos_1 < mathimatos_3 and mathimatos_1 < mathimatos_4:
    print(mathima_1)
if mathimatos_2 < mathimatos_3 and mathimatos_2 < mathimatos_4 and mathimatos_2 < mathimatos_1:
    print(mathima_2)
if mathimatos_3 < mathimatos_4 and mathimatos_3 < mathimatos_1 and mathimatos_3 < mathimatos_2:
    print(mathima_3)
if mathimatos_4 < mathimatos_1 and mathimatos_4 < mathimatos_2 and mathimatos_4 < mathimatos_3:
    print(mathima_4)

max = 0
print(message3)
if mathimatos_1 > max:
    max = mathimatos_1
    print(max)
if mathimatos_2 > max:
    max = mathimatos_2
    print(max)
if mathimatos_3 > max:
    max = mathimatos_3
    print(max)
if mathimatos_4 > max:
    max = mathimatos_4
    print(max)

print(message4)
if mathimatos_1 < max:
    max = mathimatos_1
    print(max)
if mathimatos_2 < max:
    max = mathimatos_2
    print(max)
if mathimatos_3 < max:
    max = mathimatos_3
    print(max)
if mathimatos_4 < max:
    max = mathimatos_4
    print(max)

