class Dog:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def bark(self):
        print(f"nöf! olen {self.name}")



dog1 = Dog("Rekku", 8)
dog2 = Dog("Vili", 12)



print("Koira 1: ", dog1.name, dog1.weight)
print("Koira 2: ", dog2.name, dog2.weight)

dog1.bark()
dog2.bark()