list_log = [] 

def loop_function():
    enter_string = input("Enter John? ")

    if enter_string.lower() == "john":
        print("Incorrect names:", list_log)  
        exit() 

    # print("user entered "+ enter_string)
    list_log.append(enter_string)  

while True: 
    loop_function()
