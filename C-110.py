import pandas as pd
import csv
import statistics as s
import random
import plotly.figure_factory as ff

df = pd.read_csv("Data.csv")
reading_time = df["reading_time"].tolist()

population_mean = s.mean(reading_time)
print(population_mean)

def random_set_of_mean(counter):
    data_set = []

    for x in range(counter):
        random_index = random.randint(0, len(reading_time) - 1)
        val = reading_time[random_index]
        data_set.append(val)

    mean = s.mean(data_set)
    return mean

def draw_plot(mean_list):
    df_of_means = mean_list
    graph = ff.create_distplot([df_of_means], ["Reading time"], show_hist=False)
    graph.show()

def setup():
    mean_list = []

    for i in range(0, 100):
        mean = random_set_of_mean(30)
        mean_list.append(mean)
    
    draw_plot(mean_list)
    print(s.mean(mean_list))

setup()