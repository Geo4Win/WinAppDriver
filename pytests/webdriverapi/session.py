

class MyClass():
    value_class = 1

    @classmethod
    def print_cls(cls):
        print(cls.value_class)
        cls.value_class = 2


    def print_instance(self):
        print(self.value_class)




def test_one():
    c = MyClass()

    c.print_cls()
    c.print_instance()