from test3 import *

class Android(Phone):

    def __init__(self, name, model):
        super().__init__(name, model)
        self.ram = 2

    def use_internet(self):
        print("opening internet")

    def update_ram(self, new_ram):
        print("Your phone ram has now", new_ram, "GB")

ph1 = Android("Google Pixel", "4A")
ph1.call()
ph1.use_internet()
print(ph1.ram)
ph1.update_ram(8)