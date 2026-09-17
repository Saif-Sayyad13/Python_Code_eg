'''class Employee:
    """
    Employee class to demonstrate:
    - Instance variables
    - Instance methods
    - Magic/Dunder methods
    - Python inspection functions
    """

    company = "ABC Technologies"       # Class variable

    def __init__(self, name, age, salary):
        # Instance variables
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        """Display employee information."""
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Salary : {self.salary}")
        print(f"Company: {self.company}")

    def increment_salary(self, amount):
        """Increase employee salary."""
        self.salary += amount

    # ---------------- MAGIC METHODS ----------------

    def __str__(self):
        """Called when print(object) is used."""
        return f"{self.name} - ₹{self.salary}"

    def __repr__(self):
        """Developer-friendly representation."""
        return f"Employee('{self.name}', {self.age}, {self.salary})"

    def __eq__(self, other):
        """Called when two objects are compared using ==."""
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        """Called when < is used."""
        return self.salary < other.salary

    def __len__(self):
        """Called when len(object) is used."""
        return len(self.name)


# =====================================================
# CREATING OBJECTS
# =====================================================

e1 = Employee("Rahul", 25, 50000)
e2 = Employee("Amit", 30, 70000)


# =====================================================
# 1. type()
# =====================================================

print("1. TYPE")
print(type(e1))


# =====================================================
# 2. isinstance()
# =====================================================

print("\n2. ISINSTANCE")
print(isinstance(e1, Employee))
print(isinstance(e1, object))


# =====================================================
# 3. __dict__
# =====================================================

print("\n3. OBJECT __dict__")
print(e1.__dict__)


# =====================================================
# 4. CLASS __dict__
# =====================================================

print("\n4. CLASS __dict__")
print(Employee.__dict__)


# =====================================================
# 5. dir()
# =====================================================

print("\n5. DIR")
print(dir(e1))


# =====================================================
# 6. __doc__
# =====================================================

print("\n6. DOCUMENTATION")
print(Employee.__doc__)


# =====================================================
# 7. help()
# =====================================================

print("\n7. HELP")
help(Employee.display)


# =====================================================
# 8. hasattr()
# =====================================================

print("\n8. HASATTR")

print(hasattr(e1, "name"))
print(hasattr(e1, "salary"))
print(hasattr(e1, "address"))


# =====================================================
# 9. getattr()
# =====================================================

print("\n9. GETATTR")

print(getattr(e1, "name"))
print(getattr(e1, "salary"))

# If attribute doesn't exist, use default value
print(getattr(e1, "address", "Address Not Available"))


# =====================================================
# 10. setattr()
# =====================================================

print("\n10. SETATTR")

setattr(e1, "address", "Pune")

print(e1.address)

print(e1.__dict__)


# =====================================================
# 11. callable()
# =====================================================

print("\n11. CALLABLE")

print(callable(e1.display))
print(callable(e1.name))


# =====================================================
# 12. INSTANCE METHOD
# =====================================================

print("\n12. INSTANCE METHOD")

e1.display()


# =====================================================
# 13. MODIFY INSTANCE VARIABLE
# =====================================================

print("\n13. MODIFY INSTANCE VARIABLE")

e1.salary = 60000

print(e1.salary)
print(e2.salary)


# =====================================================
# 14. CLASS VARIABLE
# =====================================================

print("\n14. CLASS VARIABLE")

print(Employee.company)
print(e1.company)
print(e2.company)


# Modify class variable

Employee.company = "XYZ Technologies"

print(e1.company)
print(e2.company)


# =====================================================
# 15. __str__()
# =====================================================

print("\n15. __str__")

print(e1)


# =====================================================
# 16. __repr__()
# =====================================================

print("\n16. __repr__")

print(repr(e1))


# =====================================================
# 17. __eq__()
# =====================================================

print("\n17. __eq__")

e3 = Employee("Rahul", 25, 90000)

print(e1 == e3)


# =====================================================
# 18. __lt__()
# =====================================================

print("\n18. __lt__")

print(e1 < e2)


# =====================================================
# 19. __len__()
# =====================================================

print("\n19. __len__")

print(len(e1))


# =====================================================
# 20. METHOD MODIFICATION
# =====================================================

print("\n20. MODIFY USING METHOD")

print("Before:", e1.salary)

e1.increment_salary(10000)

print("After :", e1.salary)
'''