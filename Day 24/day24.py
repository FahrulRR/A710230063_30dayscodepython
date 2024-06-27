class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'says bark, bark, bark!')

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'says meeeoooow')

class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'says tweet')

# Membuat objek dari kelas Dog, Cat, dan Bird
oDog1 = Dog('Rover')
oDog2 = Dog('Fido')
oCat1 = Cat('Fluffy')
oCat2 = Cat('Spike')
oBird = Bird('Big Bird')

# Menyimpan objek-objek ke dalam list
petsList = [oDog1, oDog2, oCat1, oCat2, oBird]

# Memanggil method speak pada setiap objek dalam list
for oPet in petsList:
    oPet.speak()
