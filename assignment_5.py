class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def describe(self):
        print(f'The name of this food is {self.name} and is of the kind {self.kind}')

    @classmethod
    def desc_cls_mthd(cls, name, kind):
        print(f'The name of this food is {name} and is of the kind {kind}')

    @staticmethod
    def desc_stc_mthd(name, kind):
        print(f'The name of this food is {name} and is of the kind {kind}')


class Fruit(Food):
    def clean(self):
        print("Fruit cleaned!")


class Meat(Food):
    def cook(self):
        print("Meat cooked!")