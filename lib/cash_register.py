#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
    self.discount =  discount
    self.total = 0
    self.items = []
    
  def add_item(self,item,price, quantity=1):
    self.last_price = price
    self.last_quantity = quantity
    self.total += price*quantity
    for count in range (0,quantity):
      self.items.append(item)

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = (100-self.discount)/100 * self.total
      print(f"After the discount, the total comes to ${self.total:.0f}.")
  
  def void_last_transaction(self):
      pass
      self.total -= self.last_price * self.last_quantity
  
    
    


  
