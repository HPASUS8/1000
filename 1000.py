first = int(input('Привет! Напиши первое любое число: '))
second = int(input('Теперь напиши второе число (любое, конечно) и если сумма 2-ух числе меньше 1000, то будет сложение, а если больше - умножение: '))
sum = first + second

if first + second <1000:
    print(f'Итак... Сумма {first} и {second} равна... {sum}!')
else:
    multi = first * second
    print(f'Итак... Сумма {first} и {second} равна... {sum}! Поэтому я выполняю умножение...')
    print(f'Итак! Умножение {first} на {second} равна... {multi}!')