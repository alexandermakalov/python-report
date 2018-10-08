# -*- coding: utf-8 -*-
import random
from random import randint
import datetime
from datetime import date
import math
import numpy as np
import decimal
from decimal import ROUND_UP
print ('***АТЭНШЭН!!! ВСЕ ДРОБНЫЕ ЧИСЛА ВВОДИТЬ ТОЛЬКО ЧЕРЕЗ ТОЧКУ "."***')
print ('')
print('''       ОЛСО!!! ЕСЛИ КАССИРОВ ТРОЕ, то КАССИРА с НАИМЕНЬШИМ количеством отработанных ЧАСОВ вводите ПЕРВЫМ. 
       И ЕЩЁ!!! Если кассир один, то вместо его введите человека с другой должностью, но ставьте меньше часов. Человек с другой должностью не может работать за кассой на равных или больше кассира.''')
print('')
while (True):
        cashiers = int(input('Введите количество кассиров: '))
        if cashiers == 2:
                cashier1 = input('Введите фамилию первого кассира: ')                                           #фамилии первого, второго и третьего кассира
                hc1 = int(input('Введите количество часов отработанных первым кассиром: '))             #количество часов отработанных кассиром
                cashier2 = input ('Введите фамилию второго кассира: ')
                hc2 = int(input('Введите количество часов отработанных вторым кассиром: '))
                break
        elif cashiers == 3:
                cashier1 = input('Введите фамилию первого кассира: ')                                           #фамилии первого, второго и третьего кассира
                hc1 = int(input('Введите количество часов отработанных первым кассиром: '))             #количество часов отработанных кассиром
                cashier2 = input ('Введите фамилию второго кассира: ')
                hc2 = int(input('Введите количество часов отработанных вторым кассиром: '))
                cashier3 = input ('Введите фамилию третьего кассира: ')
                hc3 = int(input('Введите количество часов отработанных третьим кассиром: '))
                break
        elif cashiers <= 1:                                                                                                                                     #сообщение об ошибке, меньше двух касииров в смене не предусмотрено регламентом работы магазина
                print('Алоха! Кассиров не может быть меньше двух!')
        elif cashiers > 3:                                                                                                                                      #сообщение об ошибке, в Ленина6А не предусмотрено больше трёх кассиров
                print('Поздравляю! Ваш штат увеличился и вам пора внести изменения в скрипт! А пока продолжайте вводить значения по старой системе.')
print ('')
while (True):
		try:
			m = float(input('Введите выручку: '))                                                                           #выручка
			c = int(input('Введите количество чеков: '))                                                            #количество чеков
			dc = int(input('Введите количество проданных 7% карт: '))                                       #проданные дисконтные 7% карты
			ca25 = int(input('Введите количество чеков свыше 25р. со скидкой: '))           #чеки свыше 25р.
			i = float(input('Введите сумму выданной инкассации: '))                                         #сумма выданной инкассации
			b = float(input ('Введите сумму безнала: '))
			break
		except ValueError:
			print('Введено одно или несколько неверных значений, попробуйте ввести заново.')
			print('')                                                            #выручка безнала
print('')
today = datetime.date.today()                                           
print('')
print(today.strftime("%d.%m.%Y"))
print('Скидель, Ленина 6А.')
ac = m/c                                                                                                                                        #средний чек
if dc == 0:
        dcr = randint(0, 0)                                                                                                     #рандомное значение дисконтных карт здесь и в дальнейшем, зависит от количества чеков
elif 1 <= dc <= 4:
        dcr = randint(0, 1)
elif 5 <= dc <= 10:
        dcr = 1
elif 11 <= dc <= 18:
        dcr = randint(2, 3)
elif dc >=19:
        dcr = randint(4, 5)
print ('Выручка:', "{:.2f}".format(m).replace(".", ","))
print ('Чеки:', c)
print ('Ср. чек:', "{:.2f}".format(ac).replace(".", ","))
print ('Проданных 7% карт:', dc)
print ('Чеки свыше 25р. со скидкой:', ca25)
if i > 0:
        print ('Инкассация: ', "{:.2f}".format(i).replace(".", ","))
else:
        print ('Инкассация: 0')
if b > 0:
        print ('Безнал:', "{:.2f}".format(b).replace(".", ","))
else:
        print ('Безнал: 0')
print ('')
if cashiers == 2:                                                                                                                       #если кассиров в смене было двое, то данные рассчитываются на двоих 
        if 0 <= c <= 50:
                if hc1 != hc2:                                                                                                  #разница чеков у кассиров (рандомная, зависит от кол-ва чеков здесь и в дальнейшем)
                        c1 = (c*hc1)//(hc1+hc2)
                        c2 = (c*hc2)//(hc1+hc2)
                        dc1 = (dc*hc1)//(hc1+hc2)
                        dc2 = (dc*hc2)//(hc1+hc2)
                        print ('Касса #1', cashier1)
                        print ('Чеки:', int(np.ceil(c1)))
                        print ('Проданных 7%:', dc1)
                        print ('')
                        print ('Касса #1', cashier2)
                        print ('Чеки:', int(np.ceil(c2)))
                        print ('Проданных 7%:', int(round(dc2+1)))
                elif hc1 == hc2:
                        d1 = randint(2, 4)                                                                                                  #разница чеков у кассиров (рандомная, зависит от кол-ва чеков здесь и в дальнейшем)
                        c1 = (c*hc1)//(hc1+hc2) + d1
                        c2 = c - c1
                        dc1 = (dc*hc1)//(hc1+hc2)
                        dc2 = dc - dc1
                        print ('Касса #1', cashier1)
                        print ('Чеки:', int(np.ceil(c1)))
                        print ('Проданных 7%:', int(np.ceil(dc1)))
                        print ('')
                        print ('Касса #1', cashier2)
                        print ('Чеки:', int(np.ceil(c2)))
                        print ('Проданных 7%:', int(np.ceil(dc2)))
        elif 50 < c <= 100:
                if hc1 != hc2:                                                                                                  #разница чеков у кассиров (рандомная, зависит от кол-ва чеков здесь и в дальнейшем)
                        c1 = (c*hc1)//(hc1+hc2)
                        c2 = (c*hc2)/(hc1+hc2)
                        dc1 = (dc*hc1)//(hc1+hc2)
                        dc2 = (dc*hc2)//(hc1+hc2)
                        print ('Касса #1', cashier1)
                        print ('Чеки:', int(np.ceil(c1)))
                        print ('Проданных 7%:', dc1)
                        print ('')
                        print ('Касса #1', cashier2)
                        print ('Чеки:', int(np.ceil(c2)))
                        print ('Проданных 7%:', int(round(dc2+1)))
                elif hc1 == hc2:
                        d1 = randint(3, 5)                                                                                                  #разница чеков у кассиров (рандомная, зависит от кол-ва чеков здесь и в дальнейшем)
                        c1 = (c*hc1)//(hc1+hc2) + d1
                        c2 = c - c1
                        dc1 = (dc*hc1)//(hc1+hc2)
                        dc2 = dc - dc1
                        print ('Касса #1', cashier1)
                        print ('Чеки:', int(np.ceil(c1)))
                        print ('Проданных 7%:', int(np.ceil(dc1)))
                        print ('')
                        print ('Касса #1', cashier2)
                        print ('Чеки:', int(np.ceil(c2)))
                        print ('Проданных 7%:', int(np.ceil(dc2)))
        elif 100 < c < 200:
                if hc1 != hc2:                                                                                                  #разница чеков у кассиров (рандомная, зависит от кол-ва чеков здесь и в дальнейшем)
                        c1 = (c*hc1)//(hc1+hc2)
                        c2 = (c*hc2)//(hc1+hc2)
                        dc1 = (dc*hc1)//(hc1+hc2)
                        dc2 = (dc*hc2)//(hc1+hc2)
                        print ('Касса #1', cashier1)
                        print ('Чеки:', int(np.ceil(c1)))
                        print ('Проданных 7%:', dc1)
                        print ('')
                        print ('Касса #1', cashier2)
                        print ('Чеки:', int(np.ceil(c2)))
                        print ('Проданных 7%:', int(round(dc2+1)))
                elif hc1 == hc2:
                        d1 = randint(4, 8)                                                                                                  #разница чеков у кассиров (рандомная, зависит от кол-ва чеков здесь и в дальнейшем)
                        c1 = (c*hc1)//(hc1+hc2) + d1
                        c2 = c - c1
                        dc1 = (dc*hc1)//(hc1+hc2)
                        dc2 = dc - dc1
                        print ('Касса #1', cashier1)
                        print ('Чеки:', int(np.ceil(c1)))
                        print ('Проданных 7%:', int(np.ceil(dc1)))
                        print ('')
                        print ('Касса #1', cashier2)
                        print ('Чеки:', int(np.ceil(c2)))
                        print ('Проданных 7%:', int(np.ceil(dc2)))
        elif c >= 200:
                if hc1 != hc2:                                                                                                  #разница чеков у кассиров (рандомная, зависит от кол-ва чеков здесь и в дальнейшем)
                        c1 = (c*hc1)//(hc1+hc2)
                        c2 = (c*hc2)//(hc1+hc2)
                        dc1 = (dc*hc1)//(hc1+hc2)
                        dc2 = (dc*hc2)//(hc1+hc2)
                        print ('Касса #1', cashier1)
                        print ('Чеки:', int(np.ceil(c1)))
                        print ('Проданных 7%:', dc1)
                        print ('')
                        print ('Касса #1', cashier2)
                        print ('Чеки:', int(np.ceil(c2)))
                        print ('Проданных 7%:', int(round(dc2+1)))
                elif hc1 == hc2:
                        d1 = randint(6, 11)                                                                                                  #разница чеков у кассиров (рандомная, зависит от кол-ва чеков здесь и в дальнейшем)
                        c1 = (c*hc1)//(hc1+hc2) + d1
                        c2 = c - c1
                        dc1 = (dc*hc1)//(hc1+hc2)
                        dc2 = dc - dc1
                        print ('Касса #1', cashier1)
                        print ('Чеки:', int(np.ceil(c1)))
                        print ('Проданных 7%:', int(np.ceil(dc1)))
                        print ('')
                        print ('Касса #1', cashier2)
                        print ('Чеки:', int(np.ceil(c2)))
                        print ('Проданных 7%:', int(np.ceil(dc2)))
elif cashiers == 3:                                                                                                                             #если кассиров в смене было трое, то данные рассчитываются на троих
        if 0 <= c <= 50:
                d1 = randint(2, 4)                                                                                                      
                c1 = (c*hc1)//(hc1+hc2+hc3)                                                                     #формула расчёта чеков для первого кассира (остальные отталкиваются от первого, что отличается от расчёта между двумя кассирами)
                c2 = (c - c1)//2 + d1
                c3 = c - c1 - c2
                dc1 = (dc*hc1)//(hc1+hc2+hc3)                                                                   #формула расчёта дисконтных карт для первого кассира (остальные отталкиваются от первого, что отличается от расчёта между двумя кассирами)
                dc2 = (dc - dc1)//2
                dc3 = dc - dc1 - dc2
                print ('Касса #1', cashier1)
                print ('Чеки:', c1)
                print ('Проданных 7%:', dc1)
                print ('')
                print ('Касса #1', cashier2)
                print ('Чеки:', c2)
                print ('Проданных 7%:', dc2)
                print ('')
                print ('Касса #1', cashier3)
                print ('Чеки:', c3)
                print ('Проданных 7%:', dc3)
        elif 50 < c <= 100:
                d1 = randint(2, 5)
                c1 = (c*hc1)//(hc1+hc2+hc3)      
                c2 = (c - c1)//2 + d1
                c3 = c - c1 - c2
                dc1 = (dc*hc1)//(hc1+hc2+hc3) 
                dc2 = (dc - dc1)//2
                dc3 = dc - dc1 - dc2
                print ('Касса #1', cashier1)
                print ('Чеки:', c1)
                print ('Проданных 7%:', dc1)
                print ('')
                print ('Касса #1', cashier2)
                print ('Чеки:', c2)
                print ('Проданных 7%:', dc2)
                print ('')
                print ('Касса #1', cashier3)
                print ('Чеки:', c3)
                print ('Проданных 7%:', dc3)
        elif 100 < c < 200:
                d1 = randint(4, 8)
                c1 = (c*hc1)//(hc1+hc2+hc3)      
                c2 = (c - c1)//2 + d1
                c3 = c - c1 - c2
                dc1 = (dc*hc1)//(hc1+hc2+hc3) 
                dc2 = (dc - dc1)//2
                dc3 = dc - dc1 - dc2
                print ('Касса #1', cashier1)
                print ('Чеки:', c1)
                print ('Проданных 7%:', dc1)
                print ('')
                print ('Касса #1', cashier2)
                print ('Чеки:', c2)
                print ('Проданных 7%:', dc2)
                print ('')
                print ('Касса #1', cashier3)
                print ('Чеки:', c3)
                print ('Проданных 7%:', dc3)
        elif c >= 200:
                d1 = randint(6, 11)
                c1 = (c*hc1)//(hc1+hc2+hc3)      
                c2 = (c - c1)//2 + d1
                c3 = c - c1 - c2
                dc1 = (dc*hc1)//(hc1+hc2+hc3)
                dc2 = (dc - dc1)//2
                dc3 = dc - dc1 - dc2
                print ('Касса #1', cashier1)
                print ('Чеки:', c1)
                print ('Проданных 7%:', dc1)
                print ('')
                print ('Касса #1', cashier2)
                print ('Чеки:', c2)
                print ('Проданных 7%:', dc2)
                print ('')
                print ('Касса #1', cashier3)
                print ('Чеки:', c3)
                print ('Проданных 7%:', dc3)
print('')
input("Для выхода нажмите Enter")
