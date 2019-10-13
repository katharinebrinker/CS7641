import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_headers = ['Trial Time', 'Optimum Fitness']

# traveling salesman
hill_climbing_data_salesman = pd.read_csv("../Assignment2/salesman_hill_climbing.csv", names=csv_headers)
annealing_data_salesman = pd.read_csv("../Assignment2/salesman_annealing.csv", names=csv_headers)
genetic_data_salesman = pd.read_csv("../Assignment2/salesman_genetic.csv", names=csv_headers)
mimic_data_salesman = pd.read_csv("../Assignment2/salesman_mimic.csv", names=csv_headers)

# flipflop
hill_climbing_data_flipflop = pd.read_csv("../Assignment2/flipflop_hill_climbing.csv", names=csv_headers)
annealing_data_flipflop = pd.read_csv("../Assignment2/flipflop_annealing.csv", names=csv_headers)
genetic_data_flipflop = pd.read_csv("../Assignment2/flipflop_genetic.csv", names=csv_headers)
mimic_data_flipflop = pd.read_csv("../Assignment2/flipflop_mimic.csv", names=csv_headers)

# continuous peaks
hill_climbing_data_peaks = pd.read_csv("../Assignment2/peaks_hill_climbing.csv", names=csv_headers)
annealing_data_peaks = pd.read_csv("../Assignment2/peaks_annealing.csv", names=csv_headers)
genetic_data_peaks = pd.read_csv("../Assignment2/peaks_genetic.csv", names=csv_headers)
mimic_data_peaks = pd.read_csv("../Assignment2/peaks_mimic.csv", names=csv_headers)



# print salesman run times
plt.figure()
plt.plot(hill_climbing_data_salesman['Trial Time'], label="Hill Climbing")
plt.plot(annealing_data_salesman['Trial Time'], label="Simulated Annealing")
plt.plot(genetic_data_salesman['Trial Time'], label="Genetic Algorithms")
plt.plot(mimic_data_salesman['Trial Time'], label="MIMIC")
plt.title("Traveling Salesman Run Time")
plt.xlabel("Trial")
plt.ylabel("Time (Seconds)")
plt.legend(loc=0)
plt.savefig("../Assignment2/salesman_time.png")

# print salesman optima
plt.figure()
plt.plot(hill_climbing_data_salesman['Optimum Fitness'], label="Hill Climbing")
plt.plot(annealing_data_salesman['Optimum Fitness'], label="Simulated Annealing")
plt.plot(genetic_data_salesman['Optimum Fitness'], label="Genetic Algorithms")
plt.plot(mimic_data_salesman['Optimum Fitness'], label="MIMIC")
plt.title("Traveling Salesman Fitness")
plt.xlabel("Trial")
plt.ylabel("Fitness (1 / distance)")
plt.legend(loc=0)
plt.savefig("../Assignment2/salesman_fitness.png")

# print flipflop run times
plt.figure()
plt.plot(hill_climbing_data_flipflop['Trial Time'], label="Hill Climbing")
plt.plot(annealing_data_flipflop['Trial Time'], label="Simulated Annealing")
plt.plot(genetic_data_flipflop['Trial Time'], label="Genetic Algorithms")
plt.plot(mimic_data_flipflop['Trial Time'], label="MIMIC")
plt.title("Flip Flop Run Time")
plt.xlabel("Trial")
plt.ylabel("Time (Seconds)")
plt.legend(loc=0)
plt.savefig("../Assignment2/flipflop_time.png")

# print flipflop optima
plt.figure()
plt.plot(hill_climbing_data_flipflop['Optimum Fitness'], label="Hill Climbing")
plt.plot(annealing_data_flipflop['Optimum Fitness'], label="Simulated Annealing")
plt.plot(genetic_data_flipflop['Optimum Fitness'], label="Genetic Algorithms")
plt.plot(mimic_data_flipflop['Optimum Fitness'], label="MIMIC")
plt.title("Flip Flop Fitness")
plt.xlabel("Trial")
plt.ylabel("Fitness (Flip Flops)")
plt.legend(loc=0)
plt.savefig("../Assignment2/flipflop_fitness.png")




# print continuous peaks run times
plt.figure()
plt.plot(hill_climbing_data_peaks['Trial Time'], label="Hill Climbing")
plt.plot(annealing_data_peaks['Trial Time'], label="Simulated Annealing")
plt.plot(genetic_data_peaks['Trial Time'], label="Genetic Algorithms")
plt.plot(mimic_data_peaks['Trial Time'], label="MIMIC")
plt.title("Continuous Peaks Run Time")
plt.xlabel("Trial")
plt.ylabel("Time (Seconds)")
plt.legend(loc=0)
plt.savefig("../Assignment2/continuous_peaks_time.png")

# print continuous peaks optima
plt.figure()
plt.plot(hill_climbing_data_peaks['Optimum Fitness'], label="Hill Climbing")
plt.plot(annealing_data_peaks['Optimum Fitness'], label="Simulated Annealing")
plt.plot(genetic_data_peaks['Optimum Fitness'], label="Genetic Algorithms")
plt.plot(mimic_data_peaks['Optimum Fitness'], label="MIMIC")
plt.title("Continuous Peaks Fitness")
plt.xlabel("Trial")
plt.ylabel("Fitness (Maximum Reached)")
plt.legend(loc=0)
plt.savefig("../Assignment2/continuous_peaks_fitness.png")
