def truncate(n):
    multiplier = 100  
    return int(n * multiplier) / multiplier

def getTotals(categories):
    total = 0
    breakdown = []
    for category in categories:
        total += category.get_withdrawals()
        breakdown.append(category.get_withdrawals())
    rounded = list(map(lambda x: truncate(x / total * 100), breakdown))
    return rounded

def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    totals = getTotals(categories)
    
    for i in range(100, -1, -10):
        res += str(i).rjust(3) + "| "
        for total in totals:
            if total >= i:
                res += "o  "
            else:
                res += "   "
        res += "\n"

    res += "    " + "---" * len(categories) + "-\n"

    max_len = max([len(category.name) for category in categories])

    for i in range(max_len):
        res += "     "
        for category in categories:
            if i < len(category.name):
                res += category.name[i] + "  "
            else:
                res += "   "
        if i < max_len - 1:
            res += "\n"

    return res

class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
            total += item['amount']

        output = title + items + "Total: " + str(total)
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        return None

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total_cash = 0
        for item in self.ledger:
            total_cash += item["amount"]
        return total_cash

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        return False

    def get_withdrawals(self):
        total = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total += item["amount"]
        return total