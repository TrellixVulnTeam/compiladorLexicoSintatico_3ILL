from goto import with_goto
@with_goto
def main():
	msm=True
	print(msm)
	_t1=4%3
	_t2=55/2
	_t3=_t1+_t2
	_t4=_t3-55
	print(_t4,end='')
	_t5=4//3
	_t6=_t5%3
	_t7=_t6%4
	print(_t7)
	print("oi")
	_t8=-2
	print(_t8)
	_t9=+2
	print(_t9)
	_t10=4**2
	_t11=5+_t10
	_t12="oi"+"s"
	_t13=_t12+"joao"
	print(_t11,_t13)
	print(True,False)
	print(4>3,'34'>'2')
	x=input()
	x=int(x)
	a=input()
	a=str(a)
	n=input()
	n=float(n)
main()
