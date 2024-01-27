# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self):
        Animal.num_of_animal += 1

class Dog(Animal):
    def bark(self):
        print('멍멍!')

class Cat(Animal):
    def __init__(self, word):
        Animal.num_of_animal += 1
        self.word = word
    def meow(self):
        print(self.word + "!")


class Pet(Dog, Cat):
    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'


pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
