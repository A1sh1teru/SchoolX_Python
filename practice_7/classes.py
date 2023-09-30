class Character:
    name: str
    strength: int | float
    agility: int | float
    intelligence: int | float
    speed: int | float
    damage: int | float

    def __init__(
        self,
        name,
        strength,
        agility,
        intelligence,
        speed,
        damage,
    ):
        self.name = name,
        self.strength = strength,
        self.agility = agility,
        self.intelligence = intelligence,
        self.speed = speed,
        self.damage = damage,

        print('Character initialized!')


    def name(self):
        print(f'Моё имя: {self.name}')

class Pudge(Character):
    isStink: bool


    def hook():
        print('Пудж хукнул')

    def set_isStink(self, isStink):
        self.isStink = isStink


    def info_stats(self):
        print('Имя: ', self.name)
        print('Cила: ', self.strength)
        print('Ловкость: ', self.agility)
        print('Интеллект: ', self.intelligence)
        print('Cкорость: ', self.speed)
        print('Урон: ', self.damage)
        print('----------------')
        print('Cпособность вонять: ', 'да' if self.isStink else 'нет')


    def stink(self):
        print(f'{self.name} завонял!')

class Mercy(Character):


class BirdMan(Character):
    armor: int | float
    isFly: bool


    def set_armor(self, armor):
        self.armor = armor

    def set_isFly(self, isFly):
        self.isFly = isFly


    def info_stats(self):
        print('Имя: ', self.name)
        print('Cила: ', self.strength)
        print('Ловкость: ', self.agility)
        print('Интеллект: ', self.intelligence)
        print('Cкорость: ', self.speed)
        print('Урон: ', self.damage)
        print('----------------')
        print('Броня: ', self.armor)
        print('Cпособность летать: ', 'да' if self.isFly else 'нет')


    def fly(self):
        print(f'{self.name} взлетел(а)!')



class BlueTractor(Character):

class FunkoPop():
    def __init__(self, ):

class Playable():