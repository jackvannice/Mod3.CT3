#Write a program that calculates the total amount of a meal purchased at a restaurant.
#The program should ask the user to enter the charge for the food
#and then calculate the amounts with an 18 percent tip and 7 percent sales tax.
#Display each of these amounts and the total price.

charge_input = float(input("Enter the charge for your meal: "))
tip = charge_input * 0.18
tax = charge_input * 0.07
total = charge_input + tip + tax
print('Original charge: {:.2f} \nTip: {:.2f} \n tax: {:.2f}'.format(charge_input, tip, tax))
print('Total charge: {:.2f}'.format(total))

