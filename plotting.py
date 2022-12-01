from matplotlib import pyplot as plt
from create_genetic_algorithm import rankRoutes, nextGeneration
from createFirstPopulation import createFirstPopulation


def plotting(population, populationSize, eliteSize, mutationRate, generations):
    progress = []
    pop = createFirstPopulation(populationSize, population)
    progress.append(1 / rankRoutes(pop)[0][1])

    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        progress.append(1 / rankRoutes(pop)[0][1])

    plt.plot(progress)
    plt.ylabel('Distance')
    plt.xlabel('Generation')
    plt.show()
