#вводим число, если корень целый, то оставляем, если нет, то появляется комментарий "вывести трудно"

# def guess(x: int) -> int | str:
#     x: int = int(input('Введите натуральное число: '))
#     for n in range(x+1):
#         if n*n == x: 
#             return n
#         if n*n > x:
#             break
    
#     return "Вывести трудно"

# print(guess(x))

def guess(x: int) -> int | str:
    if x == 0:
        return 0
    
    for n in range(1, x+1):
        if n*n == x:
            return n
        if n*n > x:
            break
            
    return "Слишком сложно, не могу вывести результат"

x = int(input('Введите натуральное число: '))
print(guess(x))