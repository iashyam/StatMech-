import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
plt.style.use('seaborn-whitegrid')

class monte_carlo:
    def __init__(self, L, T,steps, initial):
        self.L = L #L is the number of lattice point on one side
        self.T = T #T is the temperature in units of J/K
        self.initial = initial #intial conditions can be all up, all down or random
        self.steps = steps #number of monte carlo steps

        self.sigma = self.initial
        self.N = self.L**2 #total spins
        
        #temperature in units of T_c

        #intialise the lattice
        self.lattice = np.zeros((self.L, self.L))

        for i in range(self.L):
            for j in range(self.L):
                self.lattice[i,j] = np.random.choice(self.sigma)

        ###lists to store values of the energy and magnetisation 
        self.energy_list = np.zeros(self.steps)
        self.m_list = np.zeros(self.steps)

    def E(self): #tota(l energy of the lattice(normalised)
        s = 0
        l= 0 #mganetica monment 
        for i in range(self.L):
            for j in range(self.L):
                s += self.H(i,j)
                l += self.lattice[i,j]
        return (s/2), l/self.N #returns total energy and magnetic moment per spin

    def H(self,i,j): #energy at one spin
        return -self.lattice[i%self.L, j%self.L]*(self.lattice[(i+1)%self.L, j%self.L] +
                        self.lattice[(i-1)%self.L, j%self.L] +
                        self.lattice[(i)%self.L, (j+1)%self.L]+
                        self.lattice[(i)%self.L, (j-1)%self.L])
    
    def flip(self,i,j):

        #energy before flipping
        E1 = self.H(i,j)

        #trial flip
        self.lattice[i,j] *= -1

        E2 = self.H(i,j) #energy after flipping 

        dE = E2-E1

        accept = 0 #flag vaiable
        
        rand = np.random.uniform(0,1)
        if dE<0 or rand<np.exp(-dE/self.T):
            accept = 1
        
        if not accept: #if not accepted then revert to the original system by fliping the spin agian
            self.lattice[i,j] *= -1

    
    #one monte carlo step is made of N randomly chosen flip  
    def mc_step(self):
        for _ in range(self.N):
            i = np.random.randint(self.L)
            j = np.random.randint(self.L)

            self.flip(i,j)

    #one experiments of steps no of monte carlo steps
    #we are appending the macrostates after every state
    def experiment(self):
        for step in tqdm(range(self.steps)):
            self.mc_step()
            e, m = self.E()
            self.m_list[step] = m
            self.energy_list[step] = e



if __name__=="__main__":
    T = float(input("Enter the value of temperatue: "))
    L = int(input("Enter the lattice size: "))
    steps = int(input("Enter the number of monte_carlo steps: "))

    object = monte_carlo(L,T, steps, (1,1))
    object.experiment()
    plt.plot(object.m_list)
    plt.ylim(-1,1)
    plt.xlabel("No of steps")
    plt.ylabel('m')
    plt.show()

