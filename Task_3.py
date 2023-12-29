'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки.
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
'''
from random import randint as rd

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
counter = 0

pick_num = rd(LOWER_LIMIT, UPPER_LIMIT)
while counter < 11:
    guess_num = int(input("Введите число для угадывания!: "))
    counter += 1
    if guess_num == pick_num:
        print(f"Поздравляем, Вы угадали число {pick_num} c {counter} попыток")
        break
    elif guess_num < pick_num:
        print("Загаданое число больше!")
    elif guess_num > pick_num:
        print("Загаданое число меньше!")
else:
    print(f"К сожалению Ваши попытки закончились! Было загадано число {pick_num}")
