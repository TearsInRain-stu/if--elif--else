# Use the input statement to get the height entered from the keyboard,
# determine whether the height exceeds 120 cm, and output prompt information through the print statement.

print("welcome to HeiMa zoo")
height = input("Please enter your height: ")
"""
   a if statement to judge condition
   >= 120 cm you need to pay 20 dallors
   <  120 cm you are free
"""

if int(height) > 120:
    print("You need to pay 20 dallors")
else:
    print("You are free")
