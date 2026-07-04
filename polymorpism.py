class cat:
    def sound(self):
        print("meav,meav")

class dog:
    def sound(self):
        print("bark,bark")

animal=[cat(),dog()]
for animal in animal:
 animal.sound()