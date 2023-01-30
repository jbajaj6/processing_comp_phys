class Shot:
    def __init__(self, angle, fitness, id):
        self.angle = angle
        self.fit = fitness
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
            s = Shot(rand.random()*90, 0, i)
            population.append(s)
    else:
        mutate() 
        
def mutate():
    global population
    global st
    import random as rand
    ranked = sorted(population, key=lambda s: s.fit, reverse=True)
    best = ranked[:10]
    st /= 1.5
    print("Best Angle:",best[0].angle)
    print("Range:", best[0].fit)
    dis = [15,10,7,4,4,3,3,2,1,1]
    tr = 0
    del population[:]
    for i in range(10):
        for _ in range(dis[i]):
            x = Shot(rand.gauss(best[i].angle,st),0, tr)
            population.append(x)
            tr += 1

    
            
            
            
        
        
    
