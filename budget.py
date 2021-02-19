class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.funds = 0;
  
  def deposit(self, amount, description = ''):
    self.ledger.append({
      "amount": amount,
      "description": description
    });
    self.funds += amount
  
  def withdraw(self, amount, description = ''):
    if self.check_funds(amount):
      self.ledger.append({
        "amount": -amount,
        "description": description
      });
      self.funds -= amount
      return True
    return False
  
  def get_balance(self):
    return self.funds
  
  def transfer(self, amount, another):
    if not self.check_funds(amount):
      return False
    
    self.ledger.append({
      "amount": -amount,
      "description": "Transfer to {}".format(another.name)
    })
    self.funds -= amount;

    another.ledger.append({
      "amount": amount,
      "description": "Transfer from {}".format(self.name)
    })
    another.funds += amount;
    return True
  
  def check_funds(self, amount):
    if (amount > self.funds):
      return False
    else:
      return True

  def __str__(self):
    str = ''
    str += self.name.center(30, '*') + '\n'
    for operation in self.ledger:
      if (len(operation['description']) > 23):
        str += operation['description'][0:23]
      else:
        str += operation['description'][0:23].ljust(23)
      
      str += '{0:.2f}'.format(operation['amount']).rjust(7)
      str += '\n'
    str += 'Total: {}'.format(self.funds)
    return str;
    

    
def create_spend_chart(categories):
    result = 'Percentage spent by category\n'
    
    withdraws = {}
    total = 0;

    for categorie in categories:
      withdraws[categorie.name] = 0;
      for movement in categorie.ledger:
        if movement['amount'] < 0:
          withdraws[categorie.name] += movement['amount']
      withdraws[categorie.name] = -withdraws[categorie.name]
      total += withdraws[categorie.name]

    for name in withdraws:
      withdraws[name] = int(withdraws[name]*100/total)
      
      
    for i in range (100, -10, -10):
      result+= str(i).rjust(3) + '| '
      for name in withdraws:
        if withdraws[name] >= i:
          result += 'o  '
        else:
          result += '   '
      result += '\n'
    
    result += " " * 4 + "-" * (len(withdraws) * 3 + 1) + '\n'

    maxLen = 0

    for categorie in categories:
      if len(categorie.name) > maxLen:
        maxLen = len(categorie.name)
    
    for i in range(maxLen):
      result += ' ' * 5
      for categorie in categories:
        if len(categorie.name) > i:
          result += categorie.name[i] + '  '
        else:
          result += '   '
      result += '\n'
    return result[0:-1]
