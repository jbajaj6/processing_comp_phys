class Shot:
    def __init__(self, vel, fitness, id):
        self.vel = vel
        self.fit = fitness
        self.id = id
        
    
population = []

st = 8.0

def fitness(shots):
    global st
    import random as rand
    above = [i for i in shots if i.fit > 100000]
    above.sort(key = lambda s: s.vel)
    print("Lowest Velocity:",above[0].vel)
    print("Range:", above[0].fit)
    if len(above) >= 10:
        above = above[:10]
        dis = [15,10,7,4,4,3,3,2,1,1]
        tr = 0
        del population[:]
        for i in range(10):
            for _ in range(dis[i]):
                x = Shot(rand.gauss(above[i].vel,st),0, tr)
                population.append(x)
                tr += 1
    else:
        tr = 0
        for i in above:
            for _ in range(5):
                x = Shot(rand.gauss(i.vel,st),0, tr)
                population.append(x)
                tr += 1
        for i in range(50 - len(population)):
            s = Shot(rand.random()*70000, 0,tr)
            population.append(s)
    st /= 1.5

def populations(n, gen):
    print("Generation:", gen)
    global generation
    global population
    import random as rand
    if gen == 0:
        for i in range(n):
            s = Shot(rand.uniform(45000.0,46000.0), 0,i)
            population.append(s)
    else:
        mutate()    
   
        
def mutate():
    global population
    global st
    import random as rand
    fitness(population)



    
            
            
            
        
        
    
