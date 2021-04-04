class Category:
  def __init__(self, name):
    self.ledger = []
    self.name = name

  def deposit(self, amount, description = ''):
    entry = {
      'amount' : amount,
      'description' : description
    }
    self.ledger.append(entry)
    
  def withdraw(self, amount, description = ''):
    if self.check_funds(amount) == True:
      entry = {
        'amount' : -amount,
        'description' : description
        }
      self.ledger.append(entry)
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for entry in self.ledger:
      balance += entry['amount']
    return balance
  
  def transfer(self, amount, budget_category):
    if self.check_funds(amount) == True:
      entry = {
        'amount' : -amount,
        'description' : f'Transfer to {budget_category.name}'
      }
      self.ledger.append(entry)
      budget_category.deposit(amount, description = f'Transfer from {self.name}')
      return True
    else:
      return False

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def __str__(self):
    output = ''
    output += self.name.center(30, '*')
    for entry in self.ledger:
      amount = round(entry['amount'], 2)
      whole, decimal = str(float(amount)).split('.')
      amount_string = whole + '.' + decimal.ljust(2, '0')
      description = entry['description']
      output += '\n' + description[:23].ljust(23, ' ') + \
        amount_string[:7].rjust(7, ' ')
    output += '\nTotal: '+ str(self.get_balance())
    return output

def create_spend_chart(categories):
  category_names = []
  spent = []
  spent_percentages = []

  for category in categories:
    total_categories = 0
    for entry in category.ledger:
      if entry['amount'] < 0:
        total_categories -= entry['amount']
    spent.append(round(total_categories, 2))
    category_names.append(category.name)

  for amount in spent:
    spent_percentages.append(round(amount / sum(spent), 2) * 100)
  
  graph = 'Percentage spent by category\n'

  labels = range(100, -10, -10)

  for label in labels:
    graph += str(label).rjust(3) + '| '
    for percent in spent_percentages:
      if percent >= label:
        graph += 'o  '
      else:
        graph += '   '
    graph += '\n'

  graph += '    ----' + ('---' * (len(category_names) - 1))
  graph += '\n     '

  longest_name_length = 0

  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for limit in range(longest_name_length):
    for name in category_names:
      if len(name) > limit:
        graph += name[limit] + '  '
      else:
        graph += '   '
    if limit < longest_name_length - 1:
      graph += '\n     '

  return(graph)