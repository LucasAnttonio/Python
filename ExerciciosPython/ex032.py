
from datetime import datetime

year = int(input('Diga o ano, 0 para ano atual: '))

if year == 0:
    year = datetime.now().date().year

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f'O ano {year} é BISSEXTO')
else:
    print(f'O ano {year} NÃO É BISSEXTO')
