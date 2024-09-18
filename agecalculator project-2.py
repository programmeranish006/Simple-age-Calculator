# This is a python mini project on Age calculaator

'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

#created by: Anish M
#modified date:18-09-2024
#modified time:11:50 AM

''' this a simple demonstration of age calculator created on python 3 . in this code the user inputs his year of birth .and the console will output his age with his name as well.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''


import datetime


current_year = datetime.date.today().year



#user input


print("enter your name in Block letters:")

name=str(input())


if name.isupper():
    print("Your name is :",name)

    
else:

    print("Invalid input!")
    
    
    exit()



print("Enter your year of birth:")


your_year=int(input())


while your_year !=0 and your_year<100:
    

    if your_year.isinstance():
        print("Your year of birth is:",your_year)
    

    else:
        print("Invalid input!")
        
    

#calculation of age


age=current_year-your_year

print("Your current age is:",age)


          


