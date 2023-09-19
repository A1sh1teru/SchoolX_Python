# def convert_a_to_int(a: str, b: str) -> tuple[int, int]:

#     while True:
#         a, b = input('Введите два числа для их суммы: ').split()
#         a, b = int(a), int(b)

#         ab_sum = a + b
#         print(f'Сумма {a} + {b} = {ab_sum}')
#         print()
# try
# except ZeroDivisionError as e:
#     print(f'Ошибка: {e}')
#     print()

a: list[int] = [1, 2, 3, 3, 5]
b: list[int] = [0, 0, 1, 0, 1]

# answer = [i*2 for i in a]

# for i in a:
#     answer.append(i*2)

# print(answer)

answer = [val*b[i] for i, val in enumerate(a)]

print(answer)

for i, val in enumerate(a):
    print(f'index = ')