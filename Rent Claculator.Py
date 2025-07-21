#INPUTS we need from the users
#Total Rent
#Total food ordered for snacking
#Electricity per unit
# Charge per unit

##OUTPUT
#Total amount you've to pay is



rents = int(input("Enter your hostel room rent = "))
food = int(input("Enter the amount food Orderd = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit= int(input("Enter  the charge per unit = "))
persons = int(input("Enter the number of persons of living in the room = "))
total_bill = electricity_spend = charge_per_unit
output = (food+ rents + total_bill ) / persons
print("Each person will pay amnt. = ",output)