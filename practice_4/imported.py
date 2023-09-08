from import_this import RACE_DATA

for n in RACE_DATA.values():
    if n.get('FinishedPlace') == 1:
        winner = f'Выиграл - {n.get("RacerName")}!!! Поздравляем!!'
        break
winner += "\n"+"_"*len(winner)
print(winner)

print("")

print('Первые три места:')

print("")

print('Гонщик на 1 месте:')

for i in RACE_DATA.values():
    if i.get('FinishedPlace') == 1:
        first_winnerName = f'Имя: {i.get("RacerName")}'
        break
for i2 in RACE_DATA.values():
    if i2.get('FinishedPlace') == 1:
        first_winnerTeam = f'Команда: {i.get("RacerTeam")}'
        break
for i3 in RACE_DATA.values():
    if i3.get('FinishedPlace') == 1:
        first_winnerTime = f'Время: {i.get("FinishedTimeSeconds")}'
        break

# def convert_to_preferred_format(sec): 
#     sec = sec % (24 * 3600) 
#     hour = sec // 3600 
#     sec %= 3600 
#     min = sec // 60 
#     sec %= 60 
#     return "%02d:%02d:%02d" % (hour, min, sec) 

# n = 10000 
# print(convert(n))
    
print('   ', first_winnerName)
print('   ', first_winnerTeam)
print('   ', first_winnerTime)

print("")

print('Гонщик на 2 месте:')

for k in RACE_DATA.values():
    if k.get('FinishedPlace') == 2:
        second_winnerName = f'Имя: {k.get("RacerName")}'
        break
for k2 in RACE_DATA.values():
    if k2.get('FinishedPlace') == 2:
        second_winnerTeam = f'Команда: {k2.get("RacerTeam")}'
        break
for k3 in RACE_DATA.values():
    if k3.get('FinishedPlace') == 2:
        second_winnerTime = f'Время: {k3.get("FinishedTimeSeconds")}'
        break
print('   ', second_winnerName)
print('   ', second_winnerTeam)
print('   ', second_winnerTime)

print("")

print('Гонщик на 3 месте:')

for r in RACE_DATA.values():
    if r.get('FinishedPlace') == 3:
        third_winnerName = f'Имя: {r.get("RacerName")}'
        break
for r2 in RACE_DATA.values():
    if r2.get('FinishedPlace') == 3:
        third_winnerTeam = f'Команда: {r2.get("RacerTeam")}'
        break
for r3 in RACE_DATA.values():
    if r3.get('FinishedPlace') == 3:
        third_winnerTime = f'Время: {r3.get("FinishedTimeSeconds")}'
        break
print('   ', third_winnerName)
print('   ', third_winnerTeam)
print('   ', third_winnerTime)

print("")

if __name__ == "__main__":
    print(f"Это неимпортируемый модуль с именем {__name__}")
else:
    print(f"Это импортированный модуль с именем {__name__}")