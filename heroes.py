from main import Hero




class Wizard(Hero):
    race = 'Wizard'
    action = ['Hill', 'Badly']



    def wiz(self):
        self.validate()
        a = int(self.lvl)
        b = int(self.ability)
        if a == 10 and 120 >= b >= 80:
            print('Powerful magic')
        elif 9 >= a >= 3 and 120 >= b >= 40:
            print('Optimal magic')

        elif 3 >= a >= 0 and 120 >= b >= 80:
            print('Initial magic')
        else:
            print('Data is incorrect')

    def damage(self):
        return self.action[1]

    def hill(self):
        return self.action[1]





class Goblin(Hero):
    race = 'Goblin'
    action = ['Poison', 'Make money']


    def big_goblin(self):
        self.validate()
        return self.show()

    def poison(self):
        return self.action[0]

    def loot(self):
        return self.action[0]


gob1 = Goblin('speedrun','vip',5)
gob1.big_goblin()













