LD = 0.10
LmD = 0.25

L = int(input("Number of containers holding 1 Litre or less: "))
Lm = int(input("Number of containers holding more than 1 Litre: "))

Refund = str((L*LD) + (Lm*LD))
print("Refunded amount: $" + Refund
