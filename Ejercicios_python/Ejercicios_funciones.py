# This script contain practical exercises usign functions in python
def greet():
  """ Function that show greetings on display """
  print(f'Hi Everyone, have a wonderful day')
  
def factorialNumber(number):
  if number == 0 or number == 1:
     factorial = 1
  else:
    factorial = number * factorialNumber(number - 1 )
  return factorial

def factorialNumber2(number):
  temp_var = 1
  for i in range(number):
    temp_var *= i + 1
  return temp_var
def square(sample):
  """ Funcion para calcular los cuadrados de una lista de numeros"""
  list = []
  for i in sample:
    list.append(i**2)
  return list

def statistics(sample):
  '''Funcion que calcula varianza, media y desviacion de muestras '''
  stat = {}
  stat['media'] = sum(sample)/ len(sample)
  stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2
  stat['desviacion tipica'] = stat['varianza']**0.5
  return stat

def count_alpha_digit(str):
  dict = {'alphabet' : 0, 'digit ': 0}
  for s in str:
    if s.isalpha():
    dict['alphabet'] += 1
    elif s.isdigit():
      dict['digit'] += 1
    else: pass
  return dict
  
# Punto de entrada principal del programa
if __name__ = '__main__':
  # Exercise 1
  #greet()
  # Exercise 2
  number = 5  # We harcore a number that pass into the function
  #factorialNumber(number)
  # Ejercicio 3
  #print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
  # print(count_alpha_digit("Logical python1 0101"))
