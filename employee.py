"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, time=None):  
        self.name = name
        self.salary = salary 
        self.time = time
        self.hourly = True
        if (self.time == None):
            self.hourly = False
            self.time = 1

    def get_pay(self):
        pay = self.salary * self.time
        return pay

    def string_output_helper_initial(self):
        if (self.hourly != True):
            returnString = str(self.name) + " works on a monthly salary of " + str(self.get_pay())
        else:
            returnString = str(self.name) + " works on a contract of " + str(self.time) + " hours at " + str(self.salary) + "/hour"

        return returnString
    
    def string_output_helper_final(self):
        returnString = ". Their total pay is " + str(self.get_pay()) + "."
        return returnString

    def __str__(self):
        return self.string_output_helper_initial() + self.string_output_helper_final()

class ComissionEmployee(Employee):
    def __init__(self, name, salary, bonus, time = None, contract = None): 
        super().__init__(name, salary, time)
        self.bonus = bonus
        self.contract = contract
        self.contractCommission = True
        if self.contract == None:
            self.contractCommission = False
            self.contract = 1

    def get_pay(self):
        basePay = super().get_pay()
        totalPay = basePay + self.bonus * self.contract
        return totalPay
    
    def __str__(self):
        returnString = super().string_output_helper_initial()
        if self.contractCommission == False:
            returnString = returnString + " and receives a bonus commission of " + str(self.bonus)
        else:
            returnString = returnString + " and receives a commission for " + str(self.contract) + " contract(s) at " + str(self.bonus) + "/contract"
        returnString = returnString + super().string_output_helper_final()
        return returnString
    

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee(name = 'Billie', salary = 4000)
print(billie.get_pay())
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee(name = 'Charlie', salary = 25, time = 100)
print(charlie.get_pay())
print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = ComissionEmployee(name = 'Renee', salary = 3000, bonus = 200, contract = 4)
print(renee.get_pay())
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ComissionEmployee(name = 'Jan', salary = 25, time = 150, bonus = 220, contract = 3)
print(jan.get_pay())
print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = ComissionEmployee(name = 'Robbie', salary = 2000, bonus = 1500)
print(robbie.get_pay())
print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ComissionEmployee(name = 'Ariel', salary = 30, time = 120, bonus = 600)
print(ariel.get_pay())
print(str(ariel))
