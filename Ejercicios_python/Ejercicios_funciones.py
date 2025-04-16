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


# Punto de entrada principal del programa
if __name__ = '__main__':
  # Exercise 1
  greet()
  # Exercise 2
  number = 5  # We harcore a number that pass into the function
  factorialNumber(number)
