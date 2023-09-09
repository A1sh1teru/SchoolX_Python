if __name__ == "__main__":

    def max_common_div(a: int, b: int) -> int:

        if not (a > 0 and b > 0):
            return 0

        while a > 0 and b > 0:
            if a > b:
                a = a - b
            else:
                b = b - a

        return max(a, b)

    a = int(input('Введите значение для натурального числа "a": '))
    b = int(input('Введите значение для натурального числа "b": '))

    print(max_common_div(a, b))