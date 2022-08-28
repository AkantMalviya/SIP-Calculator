import math

print("\t**Mutual Fund & SIP Calculator**\n")
print("* 100 RS To 100000 RS")
P = int(input("Monthly Investment(RS): "))
print("\n* 5% To 30%")
R = float(input("Expected Return Rate(%) : "))
print("\n* 1year To 50year")
T = int(input("Time Period (Years) : "))

# total number of payments you made in time period
N = (T * 12)
print(f"Total Monthly Payments : {N}")
# Monthly Rate of interest for 12 months
# reduce percentage of rate
MR = ((R / 12) / 100)
# compound money (total value)
# Total claim amount
TCA = P * ((pow(1 + MR, N) - 1) / MR) * (1 + MR)

print(f"\nInvested Amount : {P * N}")
# compound value - total value
Interest = (TCA - (P * N))
print(f"Estimate Returns : {round(Interest, 2)}")
print(f"Total Claim Amount : {round(TCA, 2)}")

