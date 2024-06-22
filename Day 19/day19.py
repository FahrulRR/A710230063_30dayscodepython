class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.medical_history = []

    def add_medical_record(self, date, description):
        self.medical_history.append({"date": date, "description": description})

    def display_medical_history(self):
        print(f"Medical History for {self.name} ({self.species}):")
        for record in self.medical_history:
            print(f"Date: {record['date']}, Description: {record['description']}")

    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}, Breed: {self.breed}"


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Cat")
        self.breed = breed

    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}, Breed: {self.breed}"


# Membuat objek hewan peliharaan
dog1 = Dog("Buddy", "Golden Retriever")
cat1 = Cat("Whiskers", "Siamese")

# Menambahkan riwayat medis
dog1.add_medical_record("2023-01-10", "Annual vaccination")
dog1.add_medical_record("2023-06-15", "Flea treatment")

cat1.add_medical_record("2023-02-20", "Dental cleaning")
cat1.add_medical_record("2023-07-10", "Spaying surgery")

# Menampilkan informasi hewan peliharaan
print(dog1)
dog1.display_medical_history()

print("\n" + str(cat1))
cat1.display_medical_history()
