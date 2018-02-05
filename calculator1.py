#!/usr/bin/env python3

import sys

import csv

import os
class Args(object):

	def __init__(self):

		self.args=sys.argv[1:]

		for args in self.args:
			print(args)
			if index=args.index('-c'):
				configfile=args[index+1]
				try:
					path=os.path.exists(configfile)
				except Exception :
					print('File is not exists')
				else:
					return os.path.dirname(configfile)

			else if index=args.index('-d'):
				configfile=args[index+1]

				try:
					path=os.path.exists(configfile)

				except Exception :
					print('File is not exists')

				else:
					return os.path.dirname(cofigfile)


			else if index=args.index('o'):

				configfile=args[index+1]
				try:
					path=os.path.exists(cofigfile)

				except Exception:
					print('File is not exists')

				else:
					return os.path.dirname(configfile)



if __name__=='__main':

args=Args()
print (args)
