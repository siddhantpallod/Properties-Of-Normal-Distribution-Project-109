import plotly.figure_factory as pf
import pandas as pd
import csv
import plotly.graph_objects as pg
import statistics
import random

df = pd.read_csv('StudentsPerformance.csv')
data = df["reading score"].tolist()

mean = sum(data) / len(data)
stdDev = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

first_std_deviation_start, first_std_deviation_end = mean - stdDev, mean + stdDev
second_std_deviation_start, second_std_deviation_end = mean - (2 * stdDev), mean + (2 * stdDev)
third_std_deviation_start, third_std_deviation_end = mean - (3 * stdDev), mean + (3 * stdDev)

fig = pf.create_distplot([data] , ["reading scores"], show_hist = False)
fig.show()

list_of_data_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

per1 = format(len(list_of_data_1_std_deviation) * 100 / len(data))
per2 = format(len(list_of_data_2_std_deviation) * 100 / len(data))
per3 = format(len(list_of_data_3_std_deviation) * 100 / len(data))

print('Mean is', mean)
print("Median is", median)
print("Mode is ", mode)
print("Standard Deviation is ", stdDev)
print(per1)
print(per2)
print(per3)