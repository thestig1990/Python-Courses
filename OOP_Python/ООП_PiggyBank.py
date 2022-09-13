# the class description piggy bank. use function 'print' in method's

class PiggyBank:
    # create __init__ and add_money
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        print(f'we have in piggy bank_1 - {self.dollars}.{self.cents}$ at start')

    def add_money(self, deposit_dollars, deposit_cents):
        self.deposit_dollars = deposit_dollars
        self.deposit_cents = deposit_cents
        if self.deposit_dollars < 1:
            self.dollars += 0
            self.cents += self.deposit_cents
        else:
            self.dollars += self.deposit_dollars
            self.cents += self.deposit_cents
        if self.cents > 99:
            self.dollars += self.cents//100
            self.cents = self.cents % 100
        print(f'added {self.deposit_dollars}.{self.deposit_cents}$; total - {self.dollars}.{self.cents}$')


bank = PiggyBank(0, 0)
bank.add_money(4, 50)
bank.add_money(0, 50)
bank.add_money(100, 0)


# the class description piggy bank. use 'return' in method's

class PiggyBank2:
    # create __init__ and add_money
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        print(f'we have in piggy bank_2 - {self.dollars}.{self.cents}$ at start')

    def add_money_2(self, deposit_dollars, deposit_cents):
        self.deposit_dollars = deposit_dollars
        self.deposit_cents = deposit_cents
        if self.deposit_dollars < 1:
            self.dollars += 0
            self.cents += self.deposit_cents
        else:
            self.dollars += self.deposit_dollars
            self.cents += self.deposit_cents
        if self.cents > 99:
            self.dollars += self.cents//100
            self.cents = self.cents % 100
        return f'added {self.deposit_dollars}.{self.deposit_cents}$; total - {self.dollars}.{self.cents}$'


bank1 = PiggyBank2(1, 0)
print(bank1.add_money_2(4, 50))
print(bank1.add_money_2(0, 50))
print(bank1.add_money_2(1000, 0))
