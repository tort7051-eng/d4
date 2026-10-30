class Тварина:
    def __init__(self, ім_я, вік):
        self.ім_я = ім_я
        self.вік = вік

    def інформація(self):
        print(f"Ім'я: {self.ім_я}")
        print(f"Вік: {self.вік} років")

    def звук(self):
        print("Тварина видає звук")


class Собака(Тварина):
    def звук(self):
        print("Собака гавкає: Гав-гав!")


class Кіт(Тварина):
    def звук(self):
        print("Кіт нявкає: Няв-няв!")


sobaka = Собака("Бобік", 3)
kit = Кіт("Мурчик", 2)

print("--- Собака ---")
sobaka.інформація()
sobaka.звук()

print("--- Кіт ---")
kit.інформація()
kit.звук()
