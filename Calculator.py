'''Calculator with Python'''

#enter input
data_input1 = float(input("enter number : "))
operation = input("select one (+,-,/,*) :")
data_input2 = float(input("enter number : "))



    #
if operation == "+":
    result = data_input1 + data_input2
    print(f"the result is {result}")
        
    
    #
elif operation == "-":
    result = data_input1 - data_input2
    print(f"the result is {result}")

    #    
elif operation == "*":
    result = data_input1 * data_input2
    print(f"the result is {result}")
    #
else:
    result = data_input1 / data_input2
    print(f"the result is {result}")
