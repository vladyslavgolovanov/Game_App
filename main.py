class Hero(object):
    health = 100
    ability = 100
    phrases = ["I kill you('-')", "I am hungry"]
    race = None

    def __init__(self, skill, skin,lvl):
        self.lvl = lvl
        self.skill = skill
        self.skin = skin

    def show(self):
        sh = [self.race, self.skill, self.skin, self.health, self.ability]
        for i in sh:
            print(i)



    def attack(self):
        return self.phrases[0]

    def death(self):
        return self.phrases[1]

    @classmethod
    def validate(cls):
        if cls.race == "Wizard":
            cls.health = 80
            cls.ability = 120
        elif cls.race == "Human" or cls.race == "Goblin":
            cls.health = 120
            cls.ability = 80
        return 'this race does not exist'

    def __str__(self):
        return f'Hello, my lord!!!'

    @staticmethod
    def valid_skin(skin):
        if skin == 'common' or skin == 'rare' or skin == 'vip':
            print('Good')
        return 'ERROR'







