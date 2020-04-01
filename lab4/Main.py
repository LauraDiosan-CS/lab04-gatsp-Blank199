import os
import networkx as nx
from Chromosome import Chromosome
from GA import GA


# read the network details
def readNet(fileName):
    problParam = {}
    matrix = []
    input = open(fileName, "r")
    lines = input.readlines()
    problParam["noNodes"] = int(lines[0])

    for i in range(problParam["noNodes"]):
        line = lines[i+1].split("\n")
        line = line[0].split(",")
        aux = [int(x) for x in line]
        matrix.append(aux)

    problParam["matrix"] = matrix

    problParam["startNode"] = 1
    problParam["finalNode"] = 1

    return problParam


def fcEval(c):
    list  = c.repres
    fitness = 0

    matrix = c.problParam["matrix"]
    for i in range(c.curentNodes - 1):
        fitness += matrix[list[i]][list[i+1]]

    return fitness


def main():
    network = readNet("C:\\Users\\pc\\Desktop\\AI\\Lab5\\hard.txt")

    print(network["matrix"])

    gaParam = {"popSize": 5, "noGen": 100}

    problParam = {'function': fcEval,
                  'noNodes': network["noNodes"],
                  'matrix': network["matrix"],
                  'startNode': network["startNode"],
                  'finalNode': network["finalNode"],
                  }

    globalBest = Chromosome(problParam)
    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()
    contor = 1

    while contor <= gaParam['noGen']:
        #ga.oneGeneration()
        ga.oneGenerationElitism()
        #ga.oneGenerationSteadyState()

        bestChromo = ga.bestChromosome()
        if bestChromo.fitness < globalBest.fitness:
            globalBest = bestChromo

        print("-"*200)
        print('gen: ', contor)
        print('Local  worst fit: ', ga.worstChromosome()[0].fitness)
        print('Local  Best fit: ', bestChromo.fitness)
        print('Global Best fit: ', globalBest.fitness)


        contor += 1

    print([i+1 for i in globalBest.repres])

main()

