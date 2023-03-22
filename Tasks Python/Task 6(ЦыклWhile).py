while 1:
    b = input('угадай слово')
    if b == 'Лох' or b == 'лох':
        print('Угадал')
        break
    if b != 'стоп' or b != 'Стоп':
        print('Лох, трусы в горох')

