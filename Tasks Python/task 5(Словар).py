dick = {'city': 'Москва', 'temperature': '20'}
print(dick)
print(dick['city'])
dick['temperature'] = int(dick['temperature']) - 5
print(dick)
dick.setdefault('Country', 'Россия')
print(dick)
dick['Date'] = '01.11.2022'
print(dick)
print(len(dick))

