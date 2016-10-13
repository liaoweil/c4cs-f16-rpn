#!/usr/bin/env python3

import operator

import sys
from termcolor import colored, cprint

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod,
}

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function =  operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		print(stack)
	if len(stack) != 1:
		raise TypeError("Too many parameters")
	return stack.pop()

def main():
	while True:
		result = calculate(raw_input("rpn calc> "))
		print("Result: ", result)
		if result < 0:
			cprint("\nLOOKOUT ITS NEGATIVE!", 'red', attrs=['bold']) 


if __name__ == '__main__':
	main()
