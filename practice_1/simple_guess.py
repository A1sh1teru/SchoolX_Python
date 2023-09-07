#вводим число, если корень целый, то оставляем, если нет, то появляется комментарий "вывести трудно"

def guess(x: int) -> int | str:
    x: int = int(input('Введите натуральное число: '))
    for n in range(x+1):
        if n*n == x: 
            return n
    
    return "Вывести трудно"

print(guess(25))