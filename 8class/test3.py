class Phone():

    def __init__(self, name, model):
        self.name = name 
        self.model = model 

    def call(self):
        print(self.name, "phone is calling tu tu tu")

    def message(self):
        print(self.name, "is messaging. tin ton")


# ph1 = Phone("Googl Pixel", "4A")
# print(ph1.name)
# print(ph1.model)
# ph1.call()
# ph1.message()