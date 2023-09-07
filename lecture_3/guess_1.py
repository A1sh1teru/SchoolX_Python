# def my_personal_sum( # объявляем функцию
        # x: int | float, # переменная x с типом int или float
        # y: int | float # переменная y с типом int или float
        # )-> int | float: # функция вернет int или float
    
    # return x + y

    # for num in num_list:
    #     answer += num
    # return answer

    # print(my_personal_sum(3, 5, 1))
    # print(sum[3, 5])

def my_personal_sum(*args, **kwargs) -> int | float:
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')
