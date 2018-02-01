#!/usr/bin/env python3
import sys


def calculator(salary):

	a=salary-3500-(salary*0.165)
	if a<=1500:
		b=salary-salary*0.165-a*0.03
		c=format(b,'0.2f')
	elif a>1500 and a<=4500:
		b=salary-salary*0.165-a*0.1-105
		c=format(b,'0.2f')
	elif a>4500 and a<=9000:
		b=salary-salary*0.165-a*0.2-555
		c=format(b,'0.2f')
	elif a>9000 and a<=35000:
		b=salary-salary*0.165-a*0.25-1005
		c=format(b,'0.2f')
	elif a>35000 and a<=55000:
		b=salary-salary*0.165-a*0.3-2755
		c=format(b,'0.2f')
	elif a>55000 and a<=80000:
		b=salary-salary*0.165-a*0.35-5505
		c=format(b,'0.2f')
	elif a>80000:
		b=salary-salary*0.165-a*0.45-13505
		c=format(b,'0.2f')
	return c

numberlist=[]
salarylist=[]
for arg in sys.argv[1:]:

	
	number,salary=arg.split(':')
	numberlist.append(number)
	try:
		salary=int(salary)

	except Exception :
			print('Parameter Error')

	else:
		finalsalary=calculator(salary)
		salarylist.append(finalsalary)

dic=dict(zip(numberlist,salarylist))
for key,value in dic.items():
	print(key+":"+value)	
