# program that deterines the total amount of energy required to
# change the temperature of the water using heat capacity
# also calcu;ating the cost of providing this energy #

# Heat capacity of water
HC_H20 = 4.186
CENTS_PER_KWH = 8.9
J_TO_KWH = 2.77778e-7

# User inputs
delta_T = float(input("Please input the change in temperature in degrees C:"))
m = float(input("Please input the volume of water in ml: "))

# Calculating energy required and cost to supply
q = m * HC_H20 * delta_T
cost_cents = q * J_TO_KWH * CENTS_PER_KWH
cost_dollars = cost/100
print(cost)
print("The total energy required is %.2f J" % q)
print("This would cost approximately %.2f $" % cost_dollars)
