"""
Implementation of randomized hill climbing, simulated annealing, and genetic algorithm to
find optimal weights to a neural network that is classifying abalone as having either fewer
or more than 15 rings.
Based on AbaloneTest.java by Hannah Lau

adapted from https://github.com/pushkar/ABAGAIL/blob/master/jython/abalone_test.py
"""
import os
import csv
import sys
import time

sys.path.append(os.path.join(sys.path[0], 'ABAGAIL.jar'))

from func.nn.backprop import BackPropagationNetworkFactory
from shared import SumOfSquaresError, DataSet, Instance
from opt.example import NeuralNetworkOptimizationProblem

import opt.RandomizedHillClimbing as RandomizedHillClimbing
import opt.SimulatedAnnealing as SimulatedAnnealing
import opt.ga.StandardGeneticAlgorithm as StandardGeneticAlgorithm

INPUT_FILE = 'normalized_wine_train.csv'

INPUT_FILE_TEST = 'normalized_wine_test.csv'

INPUT_LAYER = 11
HIDDEN_LAYER = [3, 6, 9, 15]
OUTPUT_LAYER = 1
TRAINING_ITERATIONS = 1000


def initialize_train_instances():
    """Read the wine CSV data into a list of instances."""
    instances = []

    # Read in the CSV file
    with open(INPUT_FILE, "r") as wine_data:
        reader = csv.reader(wine_data)
        next(reader) # skip header

        for row in reader:
            instance = Instance([float(value) for value in row[:-1]])
            instance.setLabel(Instance(0 if float(row[-1]) <= 0 else 1))
            instances.append(instance)

    return instances

def initialize_test_instances():
    """Read the CSV data into a list of instances."""
    instances = []

    # Read in the CSV file
    with open(INPUT_FILE_TEST, "r") as wine_test_data:
        reader = csv.reader(wine_test_data)
        next(reader) # skip header

        for row in reader:
            instance = Instance([float(value) for value in row[:-1]])
            instance.setLabel(Instance(0 if float(row[-1]) <= 0 else 1))
            instances.append(instance)

    return instances


def train(oa, network, oaName, instances, measure, test_instances):
    """Train a given network on a set of instances.
    :param OptimizationAlgorithm oa:
    :param BackPropagationNetwork network:
    :param str oaName:
    :param list[Instance] instances:
    :param AbstractErrorMeasure measure:
    """
    # print "\nError results for %s\n---------------------------" % (oaName,)

    for iteration in xrange(TRAINING_ITERATIONS):
        oa.train()

        error = 0.00
        for instance in test_instances:
            network.setInputValues(instance.getData())
            network.run()

            output = instance.getLabel()
            output_values = network.getOutputValues()
            example = Instance(output_values, Instance(output_values.get(0)))
            error += measure.value(output, example)

        # print "%0.03f" % error


def main():
    """Run algorithms on the dataset."""
    instances = initialize_train_instances()
    test_instances = initialize_test_instances()
    factory = BackPropagationNetworkFactory()
    measure = SumOfSquaresError()
    data_set = DataSet(instances)

    networks = []  # BackPropagationNetwork
    nnop = []  # NeuralNetworkOptimizationProblem
    oa = []  # OptimizationAlgorithm
    oa_names = ["RHC", "SA", "GA"]


    for i in range(3):
        results = ""
        print "--------- " , str(HIDDEN_LAYER[i]), " HIDDEN LAYERS ---------"
        for name in oa_names:
            classification_network = factory.createClassificationNetwork([INPUT_LAYER, HIDDEN_LAYER[i], OUTPUT_LAYER])
            networks.append(classification_network)
            nnop.append(NeuralNetworkOptimizationProblem(data_set, classification_network, measure))

        oa.append(RandomizedHillClimbing(nnop[0]))
        oa.append(SimulatedAnnealing(1E11, .95, nnop[1]))
        oa.append(StandardGeneticAlgorithm(200, 100, 10, nnop[2]))

        for i, name in enumerate(oa_names):
            start = time.time()
            correct = 0
            incorrect = 0

            train(oa[i], networks[i], oa_names[i], instances, measure, test_instances)
            end = time.time()
            training_time = end - start

            optimal_instance = oa[i].getOptimal()
            networks[i].setWeights(optimal_instance.getData())

            start = time.time()
            for instance in instances:
                networks[i].setInputValues(instance.getData())
                networks[i].run()

                predicted = instance.getLabel().getContinuous()
                actual = networks[i].getOutputValues().get(0)

                if abs(predicted - actual) < 0.5:
                    correct += 1
                else:
                    incorrect += 1

            end = time.time()
            testing_time = end - start

            results += "\nResults for %s: \nCorrectly classified %d instances." % (name, correct)
            results += "\nIncorrectly classified %d instances.\nPercent correctly classified: %0.03f%%" % (incorrect, float(correct)/(correct+incorrect)*100.0)
            results += "\nTraining time: %0.03f seconds" % (training_time,)
            results += "\nTesting time: %0.03f seconds\n" % (testing_time,)

        print results


if __name__ == "__main__":
    main()