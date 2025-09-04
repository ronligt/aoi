from math import factorial
import numpy as np

def zernike(n,m,x,y):
    '''
        n is the scalar radial zernike number
        m is the scalar meridional zernike number
        x is a vector of x-coordinates within the unit circle
        y is a vector of x-coordinates within the unit circle
    '''
    rho=np.sqrt(x**2+y**2)
    theta=np.arctan2(y,x)
    if m>n:
        print('Warning: |m| must be less than or equal to n')
    if (n-m)%2!=0:
        print('Warning: all n and m must differ by multiples of 2 (including 0)')    
    if any(rho>1):
        print('Warning: all x and y must be within the unit circle')
    
    Z=np.zeros(len(x))
            
    # radial function
    steps=np.linspace(0, (n-abs(m))/2, int(((n-abs(m))/2)+1), dtype=int)
    #for s in steps:
    
    if m>=0:
        if m>0:
            norm=np.sqrt(2*n+2)
        else:
            norm=np.sqrt(n+1)
            
        R=np.zeros(len(x))
        for s in steps:
            factor=factorial(n-s)/(factorial(s)*factorial(0.5*n+0.5*abs(m)-s)*factorial(0.5*n-0.5*abs(m)-s))
            R+=(-1)**s*factor*rho**(n-2*s)
            
        Z=R*norm*np.cos(m*theta)
    
        return Z
    elif m<0:
        norm=np.sqrt(2*n+2)
        R=np.zeros(len(x))
        for s in steps:
            factor=factorial(n-s)/(factorial(s)*factorial(0.5*n+0.5*abs(m)-s)*factorial(0.5*n-0.5*abs(m)-s))
            R+=(-1)**s*factor*rho**(n-2*s)
            
        Z=-R*norm*np.sin(m*theta)
    
        return Z