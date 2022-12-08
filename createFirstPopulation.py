import random


# random.sample(sequence, k)
# Returns a k length list of unique elements chosen from the population sequence.
# Used for random sampling without replacement.
def createRoute(cityList):
    route = random.sample(cityList, len(cityList))
    return route


def createFirstPopulation(populationSize, cityList):
    population = []

    for i in range(0, populationSize):
        population.append(createRoute(cityList))
    return population
