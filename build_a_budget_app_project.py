class Category():
    def __init__(self, name):
        self.ledger = []
        self.balance = 0.0
        self.name = name
    
    def __str__(self):
        st = ""
        title = (self.name).center(30, "*")
        descrip = max([len(item["description"][:23]) for item in self.ledger]) 
        length_amount = [len("{:.2f}".format(float(str(item["amount"])[:4]))) for item in self.ledger]
        #print(length_amount)
        for item in self.ledger:
            if len(str(item["amount"])) <=7:
                st += item["description"][:23].ljust(descrip + 1)  + "{:.2f}".format(item["amount"]).rjust(max(length_amount)) + "\n"
           
        total = f"Total: {self.get_balance()}"
        return title + "\n" + st + total
       
        
    def deposit(self, amount, descrip = ""):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': descrip})
        
    def withdraw(self, amount, descrip = ""):
        
        if self.check_funds(amount):
            amount = amount * (-1)
            self.ledger.append({'amount': amount, 'description': descrip})#
            self.balance = self.balance + amount
            return True
        else: 
            self.balnace = self.balance
            return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, cat):
       
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {cat.name}")
            cat.deposit(amount, f"Transfer from {self.name}")
            return True
        else:        
            return False
    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        return True



def create_spend_chart(categories):
    num_cat = len(categories)
    title = "Percentage spent by category"
    lines = "    "
    s = ""
    wid= {}
    per = {}
    cat_str="     "
    if num_cat < 5:
        for category in categories:
            sum_wid = 0
            for i in range(len(category.ledger)):
                if category.ledger[i]["amount"] < 0:
                    sum_wid += category.ledger[i]["amount"]*(-1)
            wid[category.name] = sum_wid
        total = sum(wid.values())
        for k,v in wid.items():
            #print((v/total)*100)
            per[k] =   round(((v/total)*100 // 10 * 10))
        
        #print(per)
        for i in range(100, -10,-10):
            
            s += f"\n{str(i).rjust(3)}| "
        
            for k,v in per.items():
                if i <=v:
                    s += "o  "
                else:
                    s+= "   "
        s+= "\n"
        for i in range(len(per.items())):
            lines += ("-"*3)
        lines +="-"
        
        max_len = max([len(ele) for ele in list(per.keys())])
        #print(max_len)
        padded_categories = [k.ljust(max_len) for k in per.keys()]
        for cat in zip(*padded_categories): 
           
            cat_str += "  ".join(cat) + "  \n     "
        
        
        return title + s + lines +"\n" +cat_str.rstrip() + "  "
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")    
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")

food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))


