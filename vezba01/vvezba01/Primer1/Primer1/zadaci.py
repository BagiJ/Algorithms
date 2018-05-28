import sys

if len(sys.argv) < 2:
    print("Invalid number of parameters!")
    sys.exit(1)
#---------------- FUN1 ------------------#
def fun1(N):
	print("Zbir prvih ", N , " brojeva.")
	i=0
	zbir = 0
	while i<N:
		zbir += i
		i+=1
	print(zbir)
#---------------- FUN2 ------------------#
def fun2(N):
	print("Zbir kvadrata prvih ", N ," brojeva.")
	i = 0
	zbir = 0
	while i<N:
		zbir += i**i
		i+=1
	print(zbir)
#------------------ FUN3  ----------------#
def fun3(str1, str2):
	str = str1[0:3] * 2 + str2[len(str2)- 3:len(str2)]
	print("String 1: ", str1, \
		  "String 2: ", str2, \
		  "\nNovi string: ", str)

#------------------ FUN4  ----------------#
def fun4():
	#init
	l = []
	for i in range(100):
		l.append(i)
	#print(l)
	for i in range(99,0, -1):
		print(l[i])

#------------------ FUN5  ----------------#
def fun5():
	fin = open("dict_test.txt", 'r')
	d = dict()
	for key in fin:
		if key in d:
			d[key] += 1
		else:
			d[key] = 1
	fin.close()
	for x in d:
		for y in d[x]:
			print(y, ": ", d[x][y])
		
		
	
	

fun1(5)
fun2(int(sys.argv[1]))
fun3("Projektovanje", "Algoritma")
fun4()
fun5()