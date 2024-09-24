class MyClass:
    def __init__(self):
        self.mutable_attr = []  # Changed to instance attribute

my_instance_1 = MyClass()
my_instance_1.mutable_attr.append(1)
print(my_instance_1.mutable_attr)

my_instance_2 = MyClass()
print(my_instance_2.mutable_attr)
