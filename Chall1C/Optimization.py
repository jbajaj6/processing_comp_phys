from vector import Vec


class Shot:
    def __init__(self, wind, fitness, id):
        self.wind = wind
        self.fit = fitness
        self.id = id
        
    
population = []

st = 0.5

def populations(n, gen):
    print("Generation:", gen)
    global generation
    global population
    import random as rand
    if gen == 0:
        for i in range(n):
            x = rand.random()
            s = Shot(Vec(x, 1-x, 0)*13.5, 0,i)
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
    ranked = sorted(population, key=lambda s: s.fit, reverse=True)
    best = ranked[:10]
    st /= 1.5
    print("Best Wind:", best[0].wind.x, best[0].wind.y)
    print("Range:", best[0].fit)
    dis = [15,10,7,4,4,3,3,2,1,1]
    tr = 0
    del population[:]
    for i in range(10):
        for _ in range(dis[i]):
            xd = best[i].wind.normalize().x
            xd = rand.gauss(xd, st)
            if xd > 1:
                xd = 1
            x = Shot(Vec(xd, 1-xd, 0) * 13.5, 0, tr)
            population.append(x)
            tr += 1

    
            
            
            
        
        
    
