# For loop 
#  we use the to iterate overa sequence (list,tuple,string,range,etc..,)
for i in range(1,101):
     print(i)

fruits =["apple","banna","orange"]

for fruit in fruits:
     print(fruit)

# #while loop 
# count = 1
# while i <=5:
#      print(i)
#      count +=1

# Break loop 
# break the loops 
for i in range (1,9):
     if i ==5:
          break
     print(i)

#continue loop : skip the loops
for i in range(1,5):
     if i == 3:
          continue
     print(i)           
# Nested loop 
# we use multi for loops 
for i in range(3):
     for j in range(2):
          print(i,j)

# multiplications using for loops 
for i in range(1,11):
     print(f"5 x {i}={i*5}")
# 1st question begginner
for i in range(1,101):
     print(i) 
#2nd even numbers 
for i in range(2,101,2):
     print(i)

#3rd odd numbers
for i in range(1,101,1):
     print(i)

# 4th reverse number 100 to 1
for i in range(101,1,-1):
     print(i) 

#5th find sum all numbes 1 to 100 
num = 100
total = 0
for i in range(1,num+1):
     total += i
print(total)

# 6th factorial 
num = 5
fact = 1
for i in range(1,num+1):
     fact *= i
     print(fact)

#7th count number of digits
# num = 12345
# count =0
# for i in range(num):
#      count += i
#      print(count)     

# 8th palindrome 

     

                       