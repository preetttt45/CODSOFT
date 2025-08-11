import os          # Used to clear the console screen when starting a new calculation

# Define basic arithmetic operation functions
def sum(a,b) :         
    return a+b           
def difference(a,b):    
    return a-b
def multiply(a,b):     
    return a*b
def divide(a,b):        
    return a/b

# Map arithmetic symbols to their corresponding functions
operations_dict= {             
    "+" : sum,
    "-" : difference,
    "*" : multiply,
    "/" : divide
}

def calculator() :                                              
    number1=int(input("Enter first operand : "))               

     # Display available operators
    for symbol in operations_dict :                             
        print(symbol)
    
    continue_flag= True
    while continue_flag:   
        operatorr= input("Pick an operator : ")                 
        number2=int(input("Enter second operand : "))            
        calculator_function = operations_dict[operatorr]
        output = calculator_function(number1,number2)
        print(f"{number1} {operatorr} {number2} = {output}")     
    
     # Prompt for next action
        should_continue=input(f"Enter 'y' to continue calculation with {output} or 'x' to exit or 'n' to start a new calculation : ").lower()
        if should_continue=='y' : 
            number1=output
        elif should_continue=='n' :
            continue_flag=False
            os.system('cls')            # Clear the screen
            calculator()                       
        else :
            continue_flag=False
            print("Bye")
calculator()                                 

