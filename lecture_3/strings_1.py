# new_name: str = input('type name: ')

# greet_message: str = 'hello bob'

# greet_message: str = (
#     greet_message[:-3] + new_name
# )

# greet_message: str = (
#     greet_message.replace('bob', new_name)
# )

# print(greet_message)


# river: str = 'mississippiiii'

# print(
#     river.rstrip('i') + 'i'
# )

# words: str = '<!---dsa das das---!>'

# print(
#     words.strip('<!>-').split()
# )

# import string

# numbers: str = string.digits

# word: str = 'hell123o b32ob ho312w ar3e y231ou'

# for number in numbers:
#     word = word.replace(number, '')

# _word: str = ''
# _sum: float = 0.0
# _prod: float = 1.0
# _list: list = []
# _set: set = set([])

# for ch in word:
#     if ch in numbers:
#         continue
#     else:
#         _word += ch
# word = _word
# del _word

# print(
#     word.replace(numbers, '')
# )

# words: str = 'Hello Bob, are you a bob? BOB!!!'
# words = words.lower().find('bob')

# while True:
#     bob_index = words.lower().find('bob')
#     if bob_index == -1:
#         break
#     else:
#         # words = words[:bob_index]
#         words = words.lower().replace('bob', 'gregory')
#         print(words)
#         break

# print(
#     words
# )

_list: list = [1, 2, 3]
_str: str = '123'
_tuple: tuple = (1, 2, 3)

# 3 -> 5

_list[-1] = 5

print(_list, _str, _tuple)