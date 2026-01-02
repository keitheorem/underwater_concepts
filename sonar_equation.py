import numpy as np

# The purpose of this code is to rearrange the sonar equation to find the maximum 
# transmission range of a passive sonar given the operational and ambient conditions 

# The RHS of the sonar equation where RHS = SL - NL + DI - DT is a known value 

# Where the LHS is a non-linear equation 18 log (R) + alpha * R, 
# where R is the unknown 
# alpha is known (calculated)

# Known variables
SL = 150       # Source Level - Intensity of sound of sonar transducer, can be found on sonar spec sheet
NL = 60        # Noise Level - Ambient noise, measured data or from published ambient noise data
DI = 10        # Directivity Index - How directional a receiver is, from sonar spec sheet
DT = 10        # Detection Threshold - The minimum signal excess required to reliably detect a target, from operational requirement 
alpha = 0.054   # Absorption coefficient - Sound absorption in the medium, from published tables or calculated from environmental parameters

# RHS of Sonar Equation
x = SL - NL + DI - DT

# Initialisation of variables 
R = 0.001 # Range
epi = 1e-6 # Tolerance 
function = 18*np.log10(R) + alpha * R
error = x - function 

# Newton Raphson Iteration 
while error > epi: 
  derivative = 18/R + alpha 
  R = R + error/derivative
  function = 18*np.log10(R) + alpha * R
  error = x - function 

print("The Sonar Range is:", R, "metres")
