
# -*- coding: utf8 -*-
import time
def comput():
	n =int(input('请输入要计算的长度：'))
	start_time = time.time()
	w = n+10
	b = 10**w
	x1 = b*4//5
	x2 = b// -239
	he = x1+x2
	n *= 2
	for i in range(3,n,2):
	    x1 //= -25
	    x2 //= -57121
	    x = (x1+x2) // i
	    he += x
	pai = he*4
	pai //= 10**10
	end_time = time.time()
	run_time = str(end_time - start_time)
	paistr=str(pai)
	paistr=paistr[:1] + '.' + paistr[1:]
	f=open('pai.txt','w')
	f.write(paistr)
	f.close()
	print ('运行时间：' + run_time )
	print ('\n'*1)
	comput()
comput()