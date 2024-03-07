#list= [1,2,3,4,5,]
#vars["pls insert the number"]
#print(vars)
#man= input('enter your year:')

#man = int(man)
#current_age =2022-man
#print(current_age)

#using a for loop with a list that seperates negative 
#from positive
Eso = [3, 2, 4, 6, 5, -6, -6, -7, -9]
positive =[]

negative =[]#anything less than zero is a negetive numbers and anything
#than zero is postive
for i in Eso:
    if i < 0:
        negative.append(i)
    else:
        positive.append(i)

print(f'positive numbers {positive}')
print(f'negative numbers {negative}')



# -5 -4 -3 -2 -1 0 1 2 3 4 5

