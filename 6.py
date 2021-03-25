num = int(input("Enter a number: "))  
sum = 0  
temp = num  

# num = 371 


while temp > 0:  
   digit = temp % 10  
   print(digit)
   sum += digit ** 3  
   print(sum)
   temp //= 10  

   print(temp)
  
if num == sum:  
   print(num,"Yes")  
else:  
   print(num,"NO")  