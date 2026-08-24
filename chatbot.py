name=input("What is your name:")
print(f"GOOD MORNING!{name}")
while True:
    a=input("How are you?:")
   
    if a=="fine" or a=="I am good" or a=="I am great":
        print ("I am very happy to hear that:")
        break
    elif a=="bad" or a=="not good" or a=="very bad":
        print("I am really sorry to here that...")
        break
    else:
        print("I am not able to understand your feelings use words like fine, I am good, I am great, bad, not good, very bad")
    
while True:
   age=int(input("What is your age?:"))
   if age<18:      
        print("We can give you a good hair cut")
        break
   elif age>=18 and age<90:    
        print("pursue our salon services.\nIt will give you a GLOW UP")
        break
   else:
       print("This age is not valid to enter in this program")
while True:
    order=input("Do you want to book our salon services?:")
    list=["medicure","pedicure","haircut","makeup","spa","facial"]    
    if order=="yes" or order=="yeah" or order=="sure":
        print(f"These are services we provide:") 
        i=0
        for i in list:
           print(i)
      
        break
    else:
        print("No problem,You can comeback any time") 
        break  
Ress =input("Enter the service you want:")   
print("Your oppointment has done.\nWe will wait for you on Thursday 1 pm.\nHAVE A GOOD DAY!")
