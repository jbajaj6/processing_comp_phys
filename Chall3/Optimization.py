class Shot:
    def __init__(self, dis, fitness, id):
        self.dis = dis
        self.fit = fitness
        self.t = 0
        self.id = id
        
    
population = []

st = 8.0

def populations(n, gen):
    print("Generation:", gen)
    global generation
    global population
    import random as rand
    if gen == 0:
        for i in range(n):
            s = Shot(rand.random()*170, 0,i)
            population.append(s)
    else:
        mutate()    

# def std_dev(popu):
#     import math
#     mean = sum(popu)/len(popu)
#     top = sum([pow(x-mean,2) for x in popu])
#     sigma = math.sqrt(top/len(popu))
#     return sigma     
        
def mutate():
    global population
    global st
    import random as rand
    ranked = sorted(population, key=lambda s: s.fit)
    best = ranked[:10]
    st /= 1.5
    print("Fitness:",1 - best[0].fit)
    print("Time:", best[0].dis/60.0)
    dis = [15,10,7,4,4,3,3,2,1,1]
    tr = 0
    del population[:]
    for i in range(10):
        for _ in range(dis[i]):
            x = Shot(rand.gauss(best[i].dis,st),0, tr)
            population.append(x)
            tr += 1

    
            
            
            
        
        
    
