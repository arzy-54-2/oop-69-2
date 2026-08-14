# from lessons import Hero, MageHero
# from lessons.lesson1 import Hero
# from lessons.lesson2 import MageHero
# from lessons.lesson4 import *
# print(random.randint(1, 1000))

from colorama import Fore, Back, Style
import random
# print(Fore.RED + 'text')


import requests


data = requests.get('http://localhost:8001/api/v1/customers/4436937/cashbacks/history?offset=0&limit=50')
print(data.request)
