def rock_paper_scissors_winner(player1, player2):
    if player1 == player2:
        return "Ничья"
    elif player1 == "камень" and player2 == "ножницы":
        return "игрок 1 выиграл"
    elif player1 == "ножницы" and player2 == "бумага":
        return "игрок 1 выиграл"
    elif player1 == "бумага" and player2 == "камень":
        return "игрок 1 выиграл"
    else:
        return "игрок 2 выиграл"
    
input_str = input("Введите два слова (например, 'бумага камень'): ").split()
player1 = input_str[0]
player2 = input_str[1]
result = rock_paper_scissors_winner(player1, player2)
print(result)