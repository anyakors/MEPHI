import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class planet:
    def __init__(self,nm,nx,ny,nvx,nvy):
        self.x = np.zeros(1)
        self.y = np.zeros(1)
        self.vx = np.zeros(1)
        self.vy = np.zeros(1)         
        self.x[0] = nx
        self.y[0] = ny
        self.vx[0] = nvx
        self.vy[0] = nvy
        self.m=nm        
        
    
class spaceTime:
    def __init__(self):
        self.list=[]        
    
    def add(self,p):
        self.list.append(p)
        
    def __getitem__(self,i):
        return self.list[i]
    
        
    
    def timeStep(self,tau):
        for i in range(0,len(self.list)):
            Fx=0
            Fy=0
            F=0
            for j in range(0,len(self.list)):
                if (i!=j):
                    F=self[i].m*self[j].m/((0.0+(self[i].x[-1]-self[j].x[-1])**2+(self[i].y[-1]-self[j].y[-1])**2)**(1.5))
                    Fx=Fx-F*(self[i].x[-1]-self[j].x[-1])
                    Fy=Fy-F*(self[i].y[-1]-self[j].y[-1])
            self[i].x[-1]=self[i].x[-1]+tau*self[i].vx[-1]
            self[i].y[-1]=self[i].y[-1]+tau*self[i].vy[-1]
            self[i].vx[-1]=self[i].vx[-1]+tau*Fx/(self[i].m+0.0)
            self[i].vy[-1]=self[i].vy[-1]+tau*Fy/(self[i].m+0.0)
            
    def shift(self,deltaT):
        for i in range(0,len(self.list)):
            self[i].x=np.append(self[i].x,self[i].x[-1])            
            self[i].y=np.append(self[i].y,self[i].y[-1])
            self[i].vx=np.append(self[i].vx,self[i].vx[-1])
            self[i].vy=np.append(self[i].vy,self[i].vy[-1])
        
        tau=0.01
        n=int(deltaT/tau)
        for j in range(0,n):
            #for i in range(0,len(self.list)):
            self.timeStep(tau)
        
        
        
        
        
A=spaceTime()
A.add(planet(10,100,0,200,10))
A.add(planet(1000,0,10,0,30))
#A.add(planet(500,500,500,0,0))

n=1000
for i in range(0,n):
    A.shift(1)

fig, ax = plt.subplots()
ax.plot(A[0].x, A[0].y, 'b-')
ax.plot(A[1].x, A[1].y, 'r-')
#ax.plot(A[2].x, A[2].y, 'g-')
plt.show()




























