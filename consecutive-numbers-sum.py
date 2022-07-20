#suma liczb w zakresie (10,30)

number=10 #starting number
number_list=[]

for number in range(10,31):
    number_list.append(number)
    
print(number_list)
print(sum(number_list))
