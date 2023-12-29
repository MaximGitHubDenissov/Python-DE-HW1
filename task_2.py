'''

 Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
 Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
 Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''

num = int(input("Введите число больше нуля и меньше 100_000 включительно:  "))


def is_prime(num):
    if num < 0 or num > 100_000:
        return "Число не попадает в выбранный диапазон"
    elif num == 1 or num == 0:
        return "Число не простое и не составное"
    else:
        for i in range(2, num):
            if num % i == 0:
                return "Число составное"
        return "Число простое"


print(is_prime(num))