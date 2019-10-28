'''
a = {'gksrmf' : 170, 'age' : 230, 'value' : 300 , 'height' : 220, 'height' : 100}

a['hello'] = 111

print(a['age'])
print(a.keys())
print(a.values())
print(a.items())
del a['age']
print(a)
'''

''''''
a = {'temper' : 54, 'humidit' : 43, 'wind' : 78}
b = {'temper' : 42, 'humidit' : 84, 'wind' : 33}
c = {'temper' : 68, 'humidit' : 56, 'wind' : 27}
d = {'temper' : 73, 'humidit' : 22, 'wind' : 69}
e = {'temper' : 62, 'humidit' : 19, 'wind' : 38}

forecast = [a, b, c, d, e]

print(forecast[0]['temper'])
