#using comparisom  operator create a quessing game where 
#the user will input a value and use it to compare the values 
#if the input is amongst your value input,print lottery but
# but if it isnt try again
#Example =lottery numbers =[2, 3,6,12,67,89]

lis = [1,3,4,5]
water = input('please insert the number:')


int_water = int(water)

if (int_water in lis):
  print("i won the game")
else:
  print('you did\'nt  win')



  

  
  