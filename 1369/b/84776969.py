import sys
# from collections import deque
# from collections import Counter
# from math import sqrt
# from math import log
# from math import ceil

# alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# mod=10**9+7
# mod=998244353

fast_reader=sys.stdin.readline
fast_writer=sys.stdout.write

def input():
	return fast_reader().strip()

def print(*argv):
	fast_writer(' '.join((str(i)) for i in argv))
	fast_writer('\n')

#____________________________________________________________________________________________________________________________________

for _ in range(int(input())):
	n=int(input())
	s=input()
	f1=0
	x=-1
	y=-1
	for i in range(n):
		if(s[i]=='1' and f1!=1):
			f1=1
			x=i
		elif(s[i]=='0'):
			y=i
	if(x==-1 or y==-1):
		print(s)
	elif(x>y):
		print(s)
	else:
		print(s[:x]+s[y:])