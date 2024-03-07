#using loops create a loop where a user will input 
# 10 different values and you will print all the user'input 
# in an array order ie alpbetical order .if its integar input
#or the value should be added in a list 

#m =input('enter the values  of different numbers of{precious +1}: ')
#m =(int)
#best =0
#for i in range(10):
 #  if(x.isalph()):
  #      best.append(x)
   # sort.best = best
#print(best)

#Assignment 3
#using loops create a loop where a user will input
#(10) different values and you will print all the user's 
#input in an arranged order ie alpabetical order.if its is an 
#integar input you should create a list for integer input and 
#aphabet input,and ,make sure the values 
#values in the list are unique meaning no word or value should 
#repeat itself for example:user derek 


total_int = []
total_alpha= []
for i in range(10):
    y = input(f'enter the number of values:{i +1 }of 10')
    if(y.isalpha()):
        total_alpha.append(y)
    elif(y.isnumeric()):
        total_int.append(int(y))   

total_alpha.sort()
print(f'the sorted lists:{total_int}{total_alpha}')





