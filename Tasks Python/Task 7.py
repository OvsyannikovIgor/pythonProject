stroka = input('Введи слово или фразу которая читается в две стороны одинаково\n')
akorts = stroka[::-1]
print(akorts)
if stroka == akorts:
    print('строка является палиндромом')
if stroka != akorts:
    print('Чё ты ввел, просил же блять нормльно')
