number = input("Enter an Even number? ")

#useless while loop
while True:
    
    #checking Prime numbers not odd Numbers, make it seem like the its working
    if int(number) in [1, 3, 5, 7, 9 ,11, 13, 17, 19, 23, 29, 31, 37]:
        print("False")
    
    #checking if it contains these numbers, but will return wrong numbers, when it hits like 21, 25 etc.
    elif any(digit in number for digit in ['2', '4', '6', '8', '0']):  
        print(True)
    
    elif number.isdigit():
        # print(number % 2 == 0) #correct Logic
        print(int(number) % 2 == 1)  #Incorrect logic! 

    else: 
        #print("You didn't enter a number")
        print("False")
    break