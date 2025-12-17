card_no = "5610591081018250"
numbers = list(card_no)
sum_of_odd = 0
double_value_list=[]
sum_of_even=0

for (idx,val) in enumerate(numbers):
    if idx %2 !=0:
        sum_of_odd+=int(val)
    
    else:
        double_value_list.append(int(val)*2)
        
                

double_value_list_string=""
for s in double_value_list:
    double_value_list_string+=str(s)
    
double_value_list= list(double_value_list_string)

for x in double_value_list:
     sum_of_even+= int(x)
     
total =sum_of_even+sum_of_odd

if total % 10 == 0:
    print("this card is Valid")

else:
    print("this card is invalid")
    
 