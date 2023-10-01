class Character:
	def __init__(
			self,
			name: str = 'Name',
			sex: bool = True,
			isHuman: bool = True,
			color: str = 'Color',
	):
			self.name = name
			self.sex = sex
			self.color = color
			self.isHuman = isHuman


	def mainInfo(self):
			print('Name:', self.name)
			print('Sex:', self.sex if 'Man' else 'Woman')
			print('Color:', self.color)
			print('Human:', self.isHuman if 'Yes' else 'No')

class OptimusPrime(Character):
	name = 'OptimusPrime'
	sex = True
	color = 'red and blue'
	isHuman = False	
	gunType = 'gun'
	transfromationType = 'truck'


	def mainInfo(self):
			print('Name:', self.name)
			print('Sex:', self.sex if 'Man' else 'Woman')
			print('Color:', self.color)
			print('Human:', self.isHuman if 'Yes' else 'No')
			print('Gun type:', self.gunType)
			print('Transformation type:', self.transfromationType)

	def motivate(self):
		print(f'{self.name} motivates you to be the greatest warrior!')

	def transform(self):
		print(f'{self.name} transforms in a {self.transfromationType}.')
	
	def shoot(self):
		print(f'{self.name} shoots from his {self.gunType}.')


class SpiderMan(Character):
	name = 'SpiderMan'
	sex = True
	color = 'red and blue'
	isHuman = True
	hero = 'hero'


	def mainInfo(self):
			print('Name:', self.name)
			print('Sex:', self.sex if 'Man' else 'Woman')
			print('Color:', self.color)
			print('Human:', self.isHuman if 'Yes' else 'No')
			print('Hero:', self.hero)

	def usesWeb(self):
		print(f'{self.name} uses a web to move faster')

	def helpsPeople(self):
		print(f'{self.name} helps people cause he is a {self.hero}.')
	
	def climbes(self):
		print(f'{self.name} can climb.')


class Tars(Character):
	name = 'TARS'
	sex = True
	color = 'gray'
	isHuman = False
	robot = 'robot'


	def mainInfo(self):
			print('Name:', self.name)
			print('Sex:', self.sex if 'Man' else 'Woman')
			print('Color:', self.color)
			print('Human:', self.isHuman if 'Yes' else 'No')
			print('Robot:', self.robot)

	def navigatesStarship(self):
		print(f'{self.name} can navigate a starship')

	def doTasks(self):
		print(f'{self.name} can do different tasks cause he is a {self.robot}.')
	
	def speaks(self):
		print(f'{self.name} can speak to humans.')


class UnstableMixin():
	def move(self):
		print('игрушка сдвинулась')

class SinkedMixin():
	def sink(self):
		print('игрушка утонула')

class FunkoPopMixin(UnstableMixin, SinkedMixin):
	pass


class FallableMixin():
	def fall(self):
		print('игрушка упала')

class AnnoyingMixin():
	def loud(self):
		print('игрушка кричит')

class PlayableMixin(FallableMixin, AnnoyingMixin):
	pass


class PlayableOptimusPrime(OptimusPrime,  PlayableMixin):
	pass
class FunkoPopOptimusPrime(OptimusPrime, FunkoPopMixin):
	pass

class PlayableSpiderMan(SpiderMan, PlayableMixin):
	pass
class FunkoPopSpiderMan(SpiderMan, FunkoPopMixin):
	pass

class PlayableTars(Tars,  PlayableMixin):
	pass
class FunkoPopTars(Tars, FunkoPopMixin):
	pass