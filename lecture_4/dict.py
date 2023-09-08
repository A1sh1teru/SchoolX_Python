alphabet: dict[
      int | str | None | float,
      str | int | float | dict[int, str | int | dict[int | str, int]]
] = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'X',
    10: 'Y',
    'Z': 10,
}

O_letter = alphabet.get('O', None)
if not bool(O_letter):
    print('NO 0')

# print(alphabet['Z'])

# print(alphabet[2])

for key, value in alphabet.items():      #.keys()    #.values()
    # if value in 'AY':
        print(f'Ключ: {key} Значение: {value}')