import math

# The potential felt by an atom in a sodium-chloride lattice is
# 
#                              e     
# V(i, j, k) = ---------------------------------  Volts
#              4 pi ep_0 a sqrt(i^2 + j^2 + k^2)
# 
# where a is the space between the atoms in the lattice and i, 
# j, and k are integer coordinates. Sodium ions are present when 
# (i + j + k) % 2 = 0 , and hold a charge of e, while chlorine
# ions are present when (i + j + k) % 2 = 1, and hold a charge 
# of -e.

e  = 1.60217663 * 10**(-19) # C
ep = 8.85418781 * 10**(-12) # F/m
a  = 2.82 * 10**(-10)       # m (2.82 Angstrom)

shell = int(input("Number of shells to compute (integer): "))

# a shell value of zero will only compute the origin, and return 
# zero.

def potential(i, j, k):
    # from formula above
    V = e / (4 * math.pi * ep * a * math.sqrt(i**2 + j**2 + k**2)) 

    if (i + j + k) % 2 == 0: # sodium ion : positive charge
        return V

    else: return -V # chlorine ion : negative charge

total_potential = 0

# iterate over the 3-D shell and add up potentials
for i in range(-shell, shell + 1):
    for j in range(-shell, shell + 1):
        for k in range(-shell, shell + 1):
            if i == 0 and j == 0 and k == 0: # ignore origin
                continue

            total_potential += potential(i, j, k)

# multiply over to solve for madelung const.
madelung = total_potential * (4 * math.pi * ep * a / e) 

print(f"Madelung Constant for {shell} shells: {madelung}")
print(f"Total Potential for {shell} shells: {total_potential} V")
