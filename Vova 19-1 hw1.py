Chui = int(input('Введите температуру в Чуйской области:'))
Osh =  int(input('Введите температуру в Ошской области:'))
Naryn = int(input('Введите температуру в Нарынской области:'))
Usuk  = int(input('Введите температуру в Ыссык-Кульской области:'))
Talas = int(input('Введите температуру в Таласской области:'))
Bishkek = int(input('Введите температуру в Бишкеке :'))

temp = (Chui + Osh + Naryn + Usuk + Talas + Bishkek + Dgalal) / 7
average = round(temp,1)
print ('Средний показатель температуры воздуха по КР на сегодня' , average , "°С.")
