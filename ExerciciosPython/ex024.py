city = input('Em qual cidade você nasceu? ').strip()

if city.lower().find('santo') == -1:
    print('Sua cidade NÃO tem Santo no nome.')
else:
    print('Sua cidade tem Santo no nome') 
