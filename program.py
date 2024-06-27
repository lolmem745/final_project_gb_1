class Animal:
    def __init__(self, name, birth_date):
        self.__name = name
        self.__birth_date = birth_date

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def train_new_commands(self, command):
        self.__command = command




class Pet(Animal):
    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date)
        self.__command = command

    def get_command(self):
        return self.__command


class PackAnimal(Animal):
    def __init__(self, name, birth_date, command):
        super().__init__(name, birth_date)
        self.__command = command

    def get_command(self):
        return self.__command


class Dog(Pet):
    pass


class Cat(Pet):
    pass


class Hamster(Pet):
    pass


class Horse(PackAnimal):
    pass


class Donkey(PackAnimal):
    pass


class Registry:
    def __init__(self):
        self.animals = []

    def add_new_animal(self, animal):
        self.animals.append(animal)

    def determine_class(self, animal):
        if isinstance(animal, Pet):
            return 'Pet'
        elif isinstance(animal, PackAnimal):
            return 'Pack Animal'

    def list_commands(self, animal):
        return animal.get_command()

    def train_new_commands(self, animal, command):
        animal.train_new_commands(command)

    def menu(self):
        while True:
            choice = input(
                "Choose an action: 1. Add new animal 2. Determine animal class 3. List commands 4. Train new commands 5. Exit: ")
            if choice == '1':
                name = input("Enter animal name: ")
                birth_date = input("Enter birth date (YYYY-MM-DD): ")
                command = input("Enter command: ")
                type_ = input("Enter type (Dog, Cat, Hamster, Horse, Donkey): ")
                if type_ == 'Dog':
                    animal = Dog(name, birth_date, command)
                elif type_ == 'Cat':
                    animal = Cat(name, birth_date, command)
                elif type_ == 'Hamster':
                    animal = Hamster(name, birth_date, command)
                elif type_ == 'Horse':
                    animal = Horse(name, birth_date, command)
                elif type_ == 'Donkey':
                    animal = Donkey(name, birth_date, command)
                self.add_new_animal(animal)
            elif choice == '2':
                name = input("Enter animal name: ")
                for animal in self.animals:
                    if animal.get_name() == name:
                        print(f"{name} is a {self.determine_class(animal)}")
            elif choice == '3':
                name = input("Enter animal name: ")
                for animal in self.animals:
                    if animal.get_name() == name:
                        print(f"{name} knows the following command: {self.list_commands(animal)}")
            elif choice == '4':
                name = input("Enter animal name: ")
                new_command = input("Enter new command: ")
                for animal in self.animals:
                    if animal.get_name() == name:
                        animal.train_new_commands(new_command)
            elif choice == '5':
                break


class Counter:
    def __init__(self):
        self.count = 0
        self.resource_open = False

    def __enter__(self):
        self.resource_open = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.resource_open = False

    def add(self):
        if not self.resource_open:
            raise Exception("Resource is not open")
        self.count += 1


# Example usage of Counter with Registry

registry = Registry()

try:
    with Counter() as counter:
        registry.add_new_animal(Dog("Buddy", "2022-01-01", "sit"))
        counter.add()
        registry.add_new_animal(Cat("Whiskers", "2021-05-15", "jump"))
        counter.add()
        registry.menu()
except Exception as e:
    print(e)
