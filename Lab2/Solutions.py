class Calculator:
    def __init__(self):
        self.firstInput = None

    def user_interface(self):
        userChoice = input("Для початку обчислення, введіть 1:")
        if userChoice == '1':
            self.user_input()

    def user_input(self):
        self.firstInput = float(input("Введіть перше чилсо: "))
        self.secondInput = float(input("Введіть дргуе чилсо: "))
        self.operator = input("введіть оператор (+,-,*,/): ")
        self.check_operator()

    def check_operator(self):
        if self.operator == '+':
            self.add()
        elif self.operator == '-':
            self.subtract()
        elif self.operator == '*':
            self.multiply()
        elif self.operator == '/':
            self.divide()
        else:
            print("введено неправильний оператор")
            return 1

    def add(self):
        result = self.firstInput + self.secondInput
        print(result)

    def subtract(self):
        result = self.firstInput - self.secondInput
        print(result)

    def divide(self):
        result = self.firstInput / self.secondInput
        print(result)

    def multiply(self):
        result = self.firstInput * self.secondInput
        print(result)

