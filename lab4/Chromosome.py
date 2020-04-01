from random import randint, seed, uniform, sample, random, shuffle


# integer representation

class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.curentNodes = problParam["noNodes"]
        self.__repres=[]
        list=[]

        self.__repres.append(int(problParam["startNode"]))
        if problParam["startNode"] == problParam["finalNode"]:
            for i in range(problParam["noNodes"]):
                if i != problParam["startNode"]:
                    list.append(i)

            shuffle(list)
            self.__repres.extend(list)
            self.curentNodes +=1

        else:
            self.curentNodes = randint(0,self.problParam["noNodes"] - 2)
            for i in range(self.problParam["noNodes"]):
                if i != problParam["startNode"] and i != problParam["finalNode"]:
                    list.append(i)
            shuffle(list)

            for i in range(self.curentNodes):
                self.__repres.append(list[i])

            self.curentNodes += 2

        self.__repres.append(problParam["finalNode"])
        self.__fitness = 99999

    @property
    def problParam(self):
        return self.__problParam

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        offspring = Chromosome(self.__problParam)

        if c.repres[0] == c.repres[-1]:
            pos1 = randint(1, self.curentNodes - 2)
            pos2 = randint(1, self.curentNodes - 2)

            if pos1 > pos2:
                pos1, pos2 = pos2, pos1

            newRepres = self.__repres[pos1:pos2 + 1]
            newRepres.insert(0, self.__problParam["startNode"])

            aux = []
            pozAux = 0
            for node in c.repres:
                if node not in newRepres:
                    aux.append(node)

            for _ in range(pos2 + 1, self.__problParam["noNodes"]):
                newRepres.append(aux[pozAux])
                pozAux += 1

            for i in range(1, pos1):
                newRepres.insert(i, aux[pozAux])
                pozAux += 1

            newRepres.append(self.__problParam["startNode"])
            offspring.repres = newRepres

        return offspring

    def mutation(self):
        if randint(1,100) <= 75:

            if self.curentNodes > 2:
                if self.curentNodes == self.__problParam["noNodes"] or self.curentNodes == self.__problParam["noNodes"]+1:
                    pos1 = randint(1, self.curentNodes - 2)
                    while True:
                        pos2 = randint(1, self.curentNodes - 2)
                        if pos1 != pos2:
                            break

                    self.__repres[pos1], self.__repres[pos2] = self.__repres[pos2], self.__repres[pos1]

                else:
                    pos = randint(1, self.curentNodes - 2)
                    while True:
                        aux = randint(0, self.__problParam["noNodes"] - 1)
                        if aux not in self.__repres :
                            break
                    self.__repres[pos] = aux



    def __str__(self):
        return "\nChromo: " + str(self.__repres) + " has fit: " + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness