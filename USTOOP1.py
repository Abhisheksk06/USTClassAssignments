# 1 Write a program which contains one class named as Demo.
# That class contains one class variable as value.
# There are two instance methods of the class as Fun and Gun which display values of instance variables.
# Initialize instance variables in the constructor by accepting the values from the user.
# After creating the class, create two objects of the Demo class as:
# Obj1 = Demo(11, 21)
# Obj2 = Demo(51, 101)
#
# Now call the instance methods as:
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()

class Demo:
    # class variable
    value = "class variable"

    def __init__(self, x, y):
        # instance variables
        self.x = x
        self.y = y
    
    # instance method1
    def Fun(self):
        print(f"Inside Fun: x = {self.x}, y = {self.y}")
    # instance method2
    def Gun(self):
        print(f"Inside Gun: x = {self.x}, y = {self.y}")

# creating objects
obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()


# 2 Write a program which contains one class named as BookStore.
# Bookstore class contains two instance variables as Name, Author.
# That class contains one class variable as NoOfBooks which is initialized to 0.
# There is one instance method of the class as Display which displays name, author, and number of books.
# Initialize instance variables in the __init__ method by accepting the values from the user as name and author.
# Inside __init__ method, increment the value of NoOfBooks by one.
# After creating the class, create two objects of the BookStore class as:
# Obj1 = BookStore("Linux System Programming", "Robert Love")
# Obj1.Display()  # Linux System Programming. No of books: 1
#
# Obj2 = BookStore("C Programming", "Dennis Ritchie")
# Obj2.Display()  # C Programming by Dennis Ritchie. No of books: 2

class BookStore:
    # class variable
    NoOfBooks = 0

    def __init__(self, name, author):
        # instance variables
        self.name = name
        self.author = author

        # inncrement value when new object is created
        BookStore.NoOfBooks += 1
    # instance method
    def Display(self):
        print(f"{self.name} by {self.author}. No of Books: {BookStore.NoOfBooks}")

# creating objects
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()
    
Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()

# 3 Write a program which contains one class named as Circle.
# Circle class contains three instance variables as Radius, Area, Circumference.
# That class contains one class variable as PI which is initialized to 3.14.
# Inside __init__ method initialize all instance variables to 0.0.
# There are three instance methods inside the class as:
# Accept(), CalculateArea(), CalculateCircumference(), Display().
# Accept method will accept the value of Radius from the user.
# CalculateArea() method will calculate the area of the circle and store it into the instance variable Area.
# CalculateCircumference() method will calculate the circumference of the circle and store it into the instance variable Circumference.
# Display() method will display the value of all the instance variables as radius, Area, and Circumference.
# After designing the above class, call all instance methods by creating multiple objects

class Circle:
    # class variable
    PI = 3.14
    def __init__(self):
        # instance variables
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0
    
    # instance method1
    def Accept(self):
        self.radius = float(input("Enter the radius of the circle: "))
    
    # instance method2
    def CalculateArea(self):
        self.area = Circle.PI * self.radius ** 2
    
    # instance method3:
    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    # method to display radius, area and circumference
    def Display(self):
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area}")
        print(f"Circumference: {self.circumference}")

# creating objects
circle1 = Circle()
circle1.Accept()
circle1.CalculateArea()
circle1.CalculateCircumference()
circle1.Display()

circle2 = Circle()
circle2.Accept()
circle2.CalculateArea()
circle2.CalculateCircumference()
circle2.Display()

# 4 Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name and Amount.
# That Class Contains one class variable as ROI which is initialized to 10.5.
# Inside __init__ method, initialize all name and amount variables by accepting values from the user.
# There are four instance methods inside the class as:
# Display(), Deposit(), Withdraw(), CalculateInterest().
# Deposit() method will accept the amount from the user and add that value to the class instance variable Amount.
# Withdraw() method will accept the amount to be withdrawn from the user and subtract that amount from the class instance variable Amount.
# CalculateInterest() method calculates the interest based on the Amount, considering the rate of interest which is the Class variable ROI.
# Display() method will display the values of all the instance variables as Name and Amount.
# After designing the above class, call all instance methods by creating multiple objects.

class BankAccount:
    # Class variable
    ROI = 10.5

    def __init__(self):
        # instance variables that accepting user input
        self.name = input("Enter account holder's name: ")
        self.amount = float(input(f"Enter the amount for {self.name}: "))

    # Method to display the account details
    def Display(self):
        print(f"Account Holder: {self.name}")
        print(f"Amount: {self.amount}")
    
    # Method to deposit amount into the account
    def Deposit(self):
        deposit_amount = int(input("Enter the amount that has to be depsoited: "))
        self.amount += deposit_amount
        print(f"{deposit_amount} has been deposited. New Balance: {self.amount}")
    
    # Method to withdraw amount from the account
    def Withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= self.amount:
            self.amount -= withdraw_amount
            print(f"{withdraw_amount} has been withdrawn. New balance: {self.amount}")
        else:
            print("Insufficient Balance!")
    
    # Method to calculate interest
    def CalculateInterest(self):
        interest = (self.amount * BankAccount.ROI) / 100
        print(f"Interest on the current balance ({self.amount}) is {interest}")

# creating objects   
account1 = BankAccount()
account1.Display()
account1.Deposit()
account1.Withdraw()
account1.CalculateInterest()

account2 = BankAccount()
account2.Display()
account2.Deposit()
account2.Withdraw()
account2.CalculateInterest()


# 5 Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variable as Value.
# Inside __init__ method, initialize that instance variable to the value which is accepted from the user.
# There are four instance methods inside the class as:
# ChkPrime(), ChkPerfect(), SumFactors(), Factors().
# ChkPrime() method will return true if the number is prime, otherwise return false.
# ChkPerfect() method will return true if the number is perfect, otherwise return false.
# Factors() method will display all factors of the instance variable.
# SumFactors() method will return the sum of all factors. Use this method in any other method as a helper method if required.
# After designing the above class, call all instance methods by creating multiple objects.

class Numbers:
    def __init__(self, value):
        # Initialize instance variable 'Value' from user input
        self.value =  value
    
    # Method for prime
    def ChkPrime(self):
        if self.value <= 1:
            return False
        for i in range(2, int(self.value ** 0.5) + 1):
            if self.value % i == 0:
                return False
        return True
    
    # Method for Perfect
    def ChkPerfect(self):
        if self.value <= 1:
            return False
        sum_of_factors = self.SumFactors()
        return sum_of_factors == self.value
    
    # Method to find and display all factors of number
    def Factors(self):
        factors = []
        for i in range(1, self.value):
            if self.value % i == 0:
                factors.append(i)
        return factors
     
     # Method to display factors
    def DisplayFactors(self):
        factors = self.Factors()
        print(f"Factors of {self.value}: {factors}")
    

    
    # Method to calculate sum of all factors
    def SumFactors(self):
        factors = self.Factors()
        return sum(factors)
    

# Creating objects
num1 = Numbers(6)
print(f"Is {num1.value} prime? {num1.ChkPrime()}")
num1.DisplayFactors()
print(f"Is {num1.value} perfect? {num1.ChkPerfect()}")
print(f"Sum of factors of {num1.value}: {num1.SumFactors()}")

num2 = Numbers(28)
print(f"Is {num2.value} prime? {num2.ChkPrime()}")
num2.DisplayFactors()
print(f"Is {num2.value} perfect? {num2.ChkPerfect()}")
print(f"Sum of factors of {num2.value}: {num2.SumFactors()}")


# 6 Write a program which contains one class named as Numbers.
#  Arithmetic class contains one instance variables as Value1,Value2.
#  Inside init method initialize all instance variables to 0.
# There are three instance methods inside class as Accept(),Addition(),Subtraction(),Multiplication(),Division().
# Accept method will accept value of value1 and value2 from user.
# Addition() method will perform addition of Value1 and Value2 and return result.
# Subtraction() method will perform subtraction of Value1 and Value2 and return result.
# Multiplication() method will perform multiplication of Value1 and Value2 and return result.
# Division() method will perform division of Value1 and Value2 and return result.
# After Designing the above class call all instance methods by creating multiple objects.

class Numbers2:
    def __init__(self):
        # Initialize instance variables to 0
        self.Value1 = 0
        self.Value2 = 0
    
    # Method to accept values from the user
    def Accept(self):
        self.Value1 = float(input("Enter the first value (Value1): "))
        self.Value2 = float(input("Enter the second value (Value2): "))
    
    # Method to perform addition
    def Addition(self):
        return self.Value1 + self.Value2

    # Method to perform subtraction
    def Subtraction(self):
        return self.Value1 - self.Value2

    # Method to perform multiplication
    def Multiplication(self):
        return self.Value1 * self.Value2

    # Method to perform division
    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Error! Division by zero."
        
# Creating objects
num1 = Numbers2()
num1.Accept()
print(f"Addition of {num1.Value1} and {num1.Value2}: {num1.Addition()}")
print(f"Subtraction of {num1.Value1} and {num1.Value2}: {num1.Subtraction()}")
print(f"Multiplication of {num1.Value1} and {num1.Value2}: {num1.Multiplication()}")
print(f"Division of {num1.Value1} and {num1.Value2}: {num1.Division()}")

num2 = Numbers2()
num2.Accept()
print(f"Addition of {num2.Value1} and {num2.Value2}: {num2.Addition()}")
print(f"Subtraction of {num2.Value1} and {num2.Value2}: {num2.Subtraction()}")
print(f"Multiplication of {num2.Value1} and {num2.Value2}: {num2.Multiplication()}")
print(f"Division of {num2.Value1} and {num2.Value2}: {num2.Division()}")

    