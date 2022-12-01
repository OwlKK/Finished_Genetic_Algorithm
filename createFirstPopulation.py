import random


def createRoute(cityList):
    route = random.sample(cityList, len(cityList))
    return route


def createFirstPopulation(popSize, cityList):
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population
