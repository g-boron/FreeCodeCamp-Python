class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []
    

  def __str__(self):
    chars = (30 - len(self.name)) // 2
    title = chars * '*' + self.name + chars * '*' + '\n'
    total = 'Total: ' + str(self.get_balance()) 
    
    desc = ''
    amounts = ''
    whole_desc = ''
    distance = ''
    for i in self.ledger:
        for k, v in i.items():
            if k == 'description':
                if len(v) <= 23:
                    desc = v
                else:
                    desc = v[:23]
            else:
                v = '%.2f' % v
                if len(str(v)) <= 7:
                    amounts = str(v)
                else:
                    amounts = str(v[:7])

        if len(desc) < 23:
            desc += (23 - len(desc)) * ' '

        if len(amounts) < 7:
            distance = (7 - len(amounts)) * ' '

        whole_desc += desc + distance + amounts + '\n'

      
    return title + whole_desc + total

  
  def deposit(self, amount, description=''):
    if description == '':
      self.ledger.append({'amount': amount, 'description': ''})
    else:
      self.ledger.append({'amount': amount, 'description': description})
      
  
  def withdraw(self, amount, description=''):
    if self.check_funds(amount) and description == '':
      self.ledger.append({'amount': -1 * amount, 'description': ''}) 
      
      return True
      
    elif self.check_funds(amount) and description != '':
      self.ledger.append({'amount': -1 * amount, 'description': description}) 
      
      return True
    else:
      
      return False

  
  def get_balance(self):
    sum = 0
    for i in self.ledger:
      sum += i['amount']

    return sum

  
  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.withdraw(amount, f'Transfer to {category.name}')
      category.deposit(amount, f'Transfer from {self.name}')
      
      return True
    else:
      
      return False
      
  
  def check_funds(self, amount):
    if amount > self.get_balance():
      
      return False
    else:
      
      return True


def create_spend_chart(categories):
  title = 'Percentage spent by category\n'
  total_spents = []
  
  for c in categories:
    amount = 0
    for i in c.ledger:
      if i['amount'] < 0:
        amount += i['amount'] * -1

    total_spents.append(amount)

  sum_of_spents = round(sum(total_spents), 2)

  percentages = [int((((s / sum_of_spents) * 10) // 1) * 10) for s in total_spents]

  chars = ''
  for i in reversed(range(0, 101, 10)):
    chars += str(i).rjust(3) + '|'

    for p in percentages:
      if p < i:
        chars += '   '
      else:
        chars += ' o '
     
    chars += ' \n'

  dashes = 4 * ' ' + ((3 * len(categories)) + 1) * '-' + '\n'
  
  names = [c.name for c in categories]
  
  max_len = -1
  for n in names:
      if len(n) > max_len:
          max_len = len(n)
          length = len(n)

  names = [n.ljust(length) for n in names]

  for x in zip(*names):
        dashes += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"
  

  return (title + chars + dashes).rstrip('\n') 