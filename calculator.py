#!/usr/bin/env python3
import sys


def calculator(salary):
	if salary<=3500:
		b=salary-salary*0.165
		c=format(b,'0.2f')
	elif salary>3500:
		a=salary-(salary*0.165)-3500
		if a<=1500:
			b=salary-salary*0.165-a*0.03
			c=format(b,'0.2f')
		elif a>1500 and a<=4500:
			b=salary-salary*0.165-(a*0.1-105)
			c=format(b,'0.2f')
		elif a>4500 and a<=9000:
			b=salary-salary*0.165-(a*0.2-555)
			c=format(b,'0.2f')
		elif a>9000 and a<=35000:
			b=salary-salary*0.165-(a*0.25-1005)
			c=format(b,'0.2f')
		elif a>35000 and a<=55000:
			b=salary-salary*0.165-(a*0.3-2755)
			c=format(b,'0.2f')
		elif a>55000 and a<=80000:
			b=salary-salary*0.165-(a*0.35-5505)
			c=format(b,'0.2f')
		elif a>80000:
			b=salary-salary*0.165-(a*0.45-13505)
			c=format(b,'0.2f')
	return c

dic={}
list=[]
for arg in sys.argv[1:]:

	
	number,salary=arg.split(':')
	try:
		salary=int(salary)

	except Exception :
			print('Parameter Error')

	else:
		finalsalary=calculator(salary)
		dic[number]=finalsalary
		list.append(number)
for i in list:
	print(i+':'+dic.get(i))


