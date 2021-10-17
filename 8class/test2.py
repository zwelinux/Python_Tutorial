class Hero():

    def __init__(self, name, hp, hero_type):
        self.name = name 
        self.hp = hp 
        self.hero_type = hero_type

    def run(self):
        print("your hero", self.name, " is running")

    def attack(self):
        print("Your hero ", self.name, "is now attacking")

h1 = Hero("zilong", 100, "assasin")
h1.run()
print(h1.name)