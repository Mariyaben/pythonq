# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O-n8xKfQs6yiUDhQPf31jbxYefAYzeRG
"""

#PAYSLIP

def employee_name():
  name=str(input("Enter employee name"))
  print(name)
  employee_name()

def employee_code():
  code=float(input("Enter employee code"))
  print(code)
  employee_code()

def basic_pay():
  bap=float(input("Enter basic pay"))
  print(bap)
  basic_pay()

def gross_salary(bp):
   if bp<10000:
    DA=(bp*5)/100
    HRA=(bp*2.5)/100
    MA=(500)

   elif bp>10000 and bp<30000:
    DA=(bp*7.5)/100
    HRA=(bp*5)/100
    MA=2500
    
  elif bp>30000 and bp<50000:
    DA=(bp*11)/100
    HRA=(bp*7.5)/100
    MA=5000

  else:
    DA=25
    HRA=11
    MA=7000

  gs = bp+DA+HRA+MA
  return gs 

def deduction(bp):
  if bp<10000:
    PT=20
    PF=(bp*8)/100
    IT=0

  elif bp <30000 and bp>10000:
    PT=60
    PF=(bp*8)/100
    IT=0

  elif bp>30000 and bp<50000:
    PT=60
    PF=(bp*11)/100
    IT=11

  else:
    PT=80
    PF=(bp*12)/100
    IT=20

  d=PT+PF+IT
  return d

def net_salary(bp):
  ns = gross_salary(bp) - deduction(bp)
  return ns

print("Gross Salary= ", gross_salary(basic_pay))
print("Deduction= ", deduction(basic_pay))
print("Net salary= ", net_salary(basic_pay))