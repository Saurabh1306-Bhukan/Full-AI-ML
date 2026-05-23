# Methods: instance method, class method, static method 

# Instance method: It can access the class as well as instance attributes.

class Laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")


l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

l1.get_info()


# Class method: It can access only class attributes.
# It is defined using the `@classmethod` decorator.

class Laptop1:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
        

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")


    

l1 = Laptop1("16gb", "512gb")


Laptop1.get_storage_type()  # we can call class method using class name  
l1.get_storage_type()  # we can also call class method using object name


# Static method: It cannot access class attributes or instance attributes. 
# It is defined using the `@staticmethod` decorator.

class Laptop2:
    
    @staticmethod
    def cal_discount( price, discount):
        final_price = price - (discount* price /100)
        print(f"final price = {final_price}")


    
l2 = Laptop2()
l2.cal_discount(40_000, 10)



# ===================================Practice Question==========================

print("==================Practice Question================")

#QS: Product Store: 
# Design & create an online store for Products (name, price).
# Track total products being created.
# Create a statc method to calculate discount on each product based on a % parameter.

class Product:
    count = 0

    def __init__ (self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):   # instance method
        print(f"Price of {self.name} is Rs. {self.price}")
    
    @classmethod
    def get_count(cls):
        print(f"Total Products = {cls.count}")

    @staticmethod
    def cal_discount(price, discount):
        print(f"Discounted price = Rs. {price - (price * discount / 100)}")

      
p1 = Product("Phone", 10_000)
p2 = Product("Laptop", 50_000)
p3 = Product("Pen", 10)

p1.get_info()
Product.get_count()

p2.cal_discount(50_000, 20)

