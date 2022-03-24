import csv
import pandas as pd
import matplotlib.pyplot as plt

def plot():

    df = pd.read_csv("spreadsheet/data.csv", delimiter=";")
    df.columns = [column.replace(' ', '') for column in df.columns]

    plotting_data = df[['Number_Of_Processes', 'Time']]

    plt.plot(plotting_data['Number_Of_Processes'], plotting_data['Time'])
    plt.xlabel("Number of processes")
    plt.ylabel("Time (s)")
    plt.savefig("plot_images/plot.png")

plot()
