# step 1: get the input
timbitsLeft = int(input()) 
# To see what the value of the input is i used the print assignment in comment
#print('the input is', timbitsLeft)

# step 2: initialize the total cost
totalCost = 0              
bigBoxes = 0
mediumBoxes = 0
smallBoxes = 0

# step 3: buy as many large boxes as you can
if timbitsLeft >=40:
  bigBoxes = int(timbitsLeft / 40)
  totalCost = totalCost + bigBoxes * 6.19    # update the total price
  timbitsLeft = timbitsLeft - 40 * bigBoxes  # calculate timbits still needed
if timbitsLeft >=20:
  mediumBoxes = int(timbitsLeft / 20)
  totalCost = totalCost + mediumBoxes * 3.39    # update the total price
  timbitsLeft = timbitsLeft - 20 * mediumBoxes  # calculate timbits still needed
if timbitsLeft >=10:
  smallBoxes = int(timbitsLeft / 10)
  totalCost = totalCost + smallBoxes * 1.99    # update the total price
  timbitsLeft = timbitsLeft - 10 * smallBoxes  # calculate timbits still needed
if timbitsLeft >0:
   totalCost = totalCost + timbitsLeft * 0.20
print(totalCost)

#To see what the values are i have the print assignments in comment
#print('bigBoxes equals', bigBoxes)
#print('mediumBoxes equels', mediumBoxes)
#print('smallBoxes equals', smallBoxes)
#print('totalCost equals', totalCost)
#print('now timbitsLeft equals', timbitsLeft)
