import random


# random.sample(sequence, k)
# Returns a k length list of unique elements chosen from the population sequence.
# Used for random sampling without replacement.
def createRoute(cityList):
    # for normal runs
    route = random.sample(cityList, len(cityList))
    return route

    # for tests
    # order = list(range(len(cityList)))
    # SEED = 2137

    # random.shuffle(order)
    #random.seed(SEED)


def createFirstPopulation(populationSize, cityList):
    population = []

    for i in range(0, populationSize):
        population.append(createRoute(cityList))
    return population
