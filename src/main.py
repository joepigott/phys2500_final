import math

# The potential felt by an atom in a sodium-chloride lattice is
# 
#                              e     
# V(i, j, k) = ---------------------------------  Volts
#              4 pi ep_0 a sqrt(i^2 + j^2 + k^2)
# 
# where a is the space between the atoms in the lattice. Sodium 
# atoms are present when (i + j + k) % 2 = 0 , and hold a charge 
# of e, while chlorine atoms are present when (i + j + k) % 2 = 1,
# and hold a charge of -e.

e  = 1.60217663 * 10**(-19) # C
ep = 8.85418781 * 10**(-12) # F/m
a  = 2.82 * 10**(-10)       # m (2.82 Angstrom)

shell = int(input("Number of shells to compute (integer): "))

# a shell value of zero will only compute the origin, and return zero.

def madelung(i, j, k):
    if (i + j + k) == 0:
        return 0

    constant = 1 / (a * math.sqrt(i**2 + j**2 + k**2))

    return constant

def potential(madelung):
    V = (e / (4 * math.pi * ep)) * madelung

    if (i + j + k) % 2 == 0:
        return V

    elif (i + j + k) % 2 == 1:
        return -V

total_potential = 0

for i in range(shell + 1):
    for j in range(shell + 1):
        for k in range(shell + 1):
            mad = madelung(i, j, k)

            total_potential += potential(mad)

print(f"Computed electric potential: {total_potential} V")
