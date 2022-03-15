# task 1
name = input('1)Как Вас зовут? ')
print ('Привет, ', name)
age = input('Сколько Вам лет? ')
print ('Вам ', age, ', а мне 25')

# task 2
time = input('2)Введите количество секунд: ')
time = int(time)
hours = time // 3600
min = (time - hours * 3600) // 60
sec = time - (hours * 3600 + min * 60)
print (f'В формате "чч:мм:сс" это =  {hours}:{min}:{sec}')

# task 3
n = input('3)Задайте число "n" от 1 до 9: ')
nn = n*2
nnn = n*3
total = int(n)+int(nn)+int(nnn)
print('Найдём n + nn + nnn')
print(n, '+', nn, '+', nnn, '=', total)
#task 4
n = abs(int(input("4)Введите целое положительное число - ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе - ", max)
    break
# TASK 5,6
vir = input('5)Введите сумму выручки ')
izd = input('Введите сумму издержек вашей компании ')
vir = float(vir)
izd = float(izd)
prib = vir - izd
ub = izd - vir
if vir > izd:
    print('Ваша прибыль =', prib,'. Рентабельность выручки составила = ', prib / izd)
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {prib / workers:.2f}")
else:
        print('Ваш убыток =', ub)

#task 7
a = int(input("7)Введите результаты пробежки спортсмена за первый день в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)