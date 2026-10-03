class Parent:
    def feature_a(self):
        print("Feature A from Parent")

class Child(Parent):
    def feature_b(self):
        print("Feature B from Child")

# Usage
obj = Child()
obj.feature_a()  # Inherited
obj.feature_b()  # Own method
