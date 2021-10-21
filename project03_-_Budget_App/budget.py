class Category:
  
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0
        self.expenses = 0

    # def __repr__(self):
    #     title = str(self.category).center(30, "*")
    #     text = title + "\n"
    #     total = 0
        
    #     for i in range(len(self.ledger)):
    #         description = self.ledger[i]['description']
    #         amount = self.ledger[i]['amount']
    #         amount_str = '{:.2f}'.format(amount)
            
    #         left = description[0:23]
    #         right = amount_str.rjust(30-len(left))
    #         text += left + right + "\n"
    #         total += amount
        
    #     total = "Total: {:.2f}".format(total)
    #     text += total
        
    #     return text
    
    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })
        self.balance += amount
        
    def withdraw(self, amount, description=""):
        if not self.check_founds(amount):
            return False
        else:    
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            self.balance -= amount
            return True
        
    def get_balance(self):
        return self.balance

    def transfer(self, amount, other_category):
        if not self.check_founds(amount):
            return False
        else:        
            self.withdraw(amount, f"Transfer to {other_category.category}")
            other_category.deposit(amount, f"Transfer from {self.category}")
            return True
        
    def check_founds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True