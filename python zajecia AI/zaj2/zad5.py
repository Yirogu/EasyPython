from pyeasyga import pyeasyga
def fitness (individual, data):
    sum1 = 0
    sum2 = 0
    for (selected, (bit,value)) in zip(individual, data):
        if selected:
            sum1 = sum1 + value
        else :
            sum2 = sum2 + value
    return sum1-sum2


data = [("1",1),("2", 4),("3", 6),("4", 11),("5", 13),("6",20),("7", 35)]
ga = pyeasyga.GeneticAlgorithm(data)

ga.fitness_function = fitness
ga.run()
simple = ga.create_individual(data)
print(simple)
