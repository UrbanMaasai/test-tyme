#Seek user input
target = int(input("Enter the number fibonacci sequence : "))

#print a list of fibonnaci numbers based on input
def fibonacci(target):
	fiboarray = [0,1];
	for i in range(2,target):
		fiboarray.append(fiboarray[i-1] + fiboarray[i-2]);
		
	print("Your Fibonacci numbers are" , fiboarray)

 	
fibonacci(target)	