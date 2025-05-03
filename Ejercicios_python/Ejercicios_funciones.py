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

class PingPongParent:
  pass
class Ping(PingPongParent):
  def __init__(self, pong):
    self.pong = pong

class Pong(PingPongParent):
  def __init__(self, pings=None):
    if pings is None:
      self.pings = []
    else:
      self.pings = pings
  def add_ping(self, ping):
    self.pings.append(ping)

def to_decimal(n):
  """Funcion para convertir un numero binario a decimal"""
  n = list(n)
  n.reverse()
  decimal = 0
  for i in range(len(n)):
    decimal += int(n[i]) * 2 ** i
  return decimal

def to_binary(n):
  binary = []
  while n > 0 :
    binary.appen(str(n % 2))
    n //= 2
    binary.reverse()
    return ''.join(binry)

def count_words(text):
  """Function that contain a number of times appears each word in a text"""
  text = text.split()
  words = {}
  for _ in text:
    if _ in words:
      words[_] += 1
    else: 
      words[_] = 1
return words

def most_repeated(words):
  max_word = ''
  max_freq = 0
  for word, freq in words.items():   # Trae tanto la clave como el valor
    if freq > max_freq:
      max_freq = freq
      max_word = word
return  max_freq,  max_word




if __name__ = '__main__':
  # Exercise 1
  #greet()
  # Exercise 2
  number = 5  # We harcore a number that pass into the function
  #factorialNumber(number)
  # Ejercicio 3
  #print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
  # print(count_alpha_digit("Logical python1 0101"))
  pong = Pong()
  ping = Ping(pong)
  pong.add_ping(ping)
  # Conversion de decimal a binario
  # Conversion de binario a decimal
  print(t_decimal('10110'))
  print(to_binary(22))
  # Calculo de la palabra con mayor frecuencia
  texto = "Como quiere que te quiera carinito, si de tu amor no me das ni si quiera un poquito, mientras tu te haces la disimulada, ve mi amor y dime que me quieres carinito"
  print(most_repeated(count_words(texto)))
