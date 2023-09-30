class MixinFlyable:
    def fly(self):
        print('I fly')

class MixinWalkable:
    def walk(self):
        print('I walk')

class MixinSwimable:
    def swim(self):
        print('I swim')

class MixinTalkable:
    def make_noise(self):
        print('Tweet')

class BaseBird:
    wings_length_cm: float = 12.5
    legs_length_cm: float = 3.5
    color: str = 'red'

    def __init__(
        self, 
        wings_length_cm: float = 12.5,
        legs_length_cm: float = 3.5,
        color: str = 'red',
    ):
        self.wings_length: float = wings_length_cm
        self.legs_length: float = legs_length_cm
        self.color: str = color
        print('BaseBird Initialized')

class Bird(
    BaseBird,
    MixinFlyable, 
    MixinWalkable, 
    MixinSwimable,
    MixinTalkable,
):
    pass

class RubberToy(MixinTalkable):
    toxic: bool = False
    size_cm3: float = 12
    color: str = 'yellow'

    def __init__(
        self,
        toxic: bool = False,
        size_cm3: float = 12,
        color: str = 'yellow',
    ):
        self.toxic: bool = toxic
        self.size_cm3: float = size_cm3
        self.color: str = color
        print('RubberToy Initialized')
    
    def bounce(self):
        print('plums')

    def deform(self):
        print('morphing time')

    def make_noise(self):
        print('peep')

bird1 = Bird()
bird1.make_noise()

toy1 = RubberToy()
toy1.make_noise()

class RubberBird(
    RubberToy, 
    BaseBird
):
    pass

rub_bird1 = RubberBird()

#rub_bird1.fly()
rub_bird1.wings_length_cm

rub_bird1.deform()

rub_bird1.make_noise()