class Category:
  
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.balance = 0
        self.expenses = 0

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
        
