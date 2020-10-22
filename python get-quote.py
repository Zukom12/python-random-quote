'''O  modulo para poder gerar numeros aleatórios num intervalo a definir'''

import random

last = 13
rnd = random.randint(0, last)

def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rnd])

if __name__== "__main__":
  primary()

