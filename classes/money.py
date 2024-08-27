class Money:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.savings = 0
        money_to_save = amount * 0.2
        money_to_spend = amount - money_to_save
        print(name, 'all_money:', amount)
        print(name, 'money to save:', money_to_save)
        print(name, 'money_to_spend:', money_to_spend)


    def upgrade(self, money_to_add):
        self.savings += money_to_add
        print('Savings:', self.savings) 

        
        