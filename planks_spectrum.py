
import matplotlib.pyplot as plt
plt.interactive(True)
import numpy as np

#Plank's formula (modification of Reley-Jeens)
#for Black body energy density
h = 6.60e-34 
k = 1.38e-23
c = 3e8
pi = 3.14159

f = lambda nu,T: 2*pi*nu**3/(c*(np.exp(h*nu/(k*T)) - 1)) 

X = np.linspace(3.e14,1.e3)      
Y=f(X,1.e3)

plt.plot(X,Y,'ro') 
plt.title('Black body energy density')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Energy density')