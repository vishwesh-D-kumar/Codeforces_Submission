import sys
# from collections import deque
# from collections import Counter
# from math import sqrt
# from math import log
# from math import ceil
# from bisect import bisect_left, bisect_right

# alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# mod=10**9+7
# mod=998244353

# def BinarySearch(a,x): 
# 	i=bisect_left(a,x) 
# 	if(i!=len(a) and a[i]==x): 
# 		return i 
# 	else: 
# 		return -1

# def sieve(n): 
# 	prime=[True for i in range(n+1)]
# 	p=2
# 	while(p*p<=n): 
# 		if (prime[p]==True): 
# 			for i in range(p*p,n+1,p): 
# 				prime[i]=False
# 		p+=1
# 	prime[0]=False
# 	prime[1]=False
# 	s=set()
# 	for i in range(len(prime)):
# 		if(prime[i]):
# 		s.add(i)
# 	return s

# def gcd(a, b):
# 	if(a==0):
# 		return b 
# 	return gcd(b%a,a)

fast_reader=sys.stdin.readline
fast_writer=sys.stdout.write

def input():
	return fast_reader().strip()

def print(*argv):
	fast_writer(' '.join((str(i)) for i in argv))
	fast_writer('\n')

#____________________________________________________________________________________________________________________________________

# for _ in range(1):
# 	n=int(input())
# 	ans=0
# 	s=set()
# 	for i in range(1,n):
# 		for j in range(i,n):
# 			if(i^j>n):
# 				continue
# 			a=i
# 			b=j
# 			c=i^j
# 			p=sorted([a,b,c])
# 			t=(p[0],p[1],p[2])
# 			if(a+b>c and a+c>b and b+c>a and t not in s):
# 				ans+=1
# 				s.add(t)
# 	print(ans)

for _ in range(1):
	n=int(input())
	l=list(map(int, input().split()))
	if(l.count(1)<=1):
		print(l.count(1))
	else:
		s=''.join(str(i) for i in l)
		s=s.split('1')
		s=s[1:-1]
		ans=1
		for i in range(len(s)):
			ans=ans*(len(s[i])+1)
		print(ans)