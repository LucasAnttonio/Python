city = input('Em qual cidade você nasceu? ').strip()

if city.lower().find('santos') == -1:
    print('Sua cidade NÃO tem Santos no nome.')
else:
    print('Sua cidade tem Santos no nome') 
