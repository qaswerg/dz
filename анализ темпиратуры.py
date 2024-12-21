import csv

def find_max_temperature(filename):
    max_temp = float('-inf')
    max_date = None
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if float(row['temperature']) > max_temp:
                max_temp = float(row['temperature'])
                max_date = row['date']
    print(f"Самая высокая температура: {max_temp}°C, Дата: {max_date}")


import matplotlib.pyplot as plt

def plot_histogram(filename):
    temperatures = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            temperatures.append(float(row['temperature']))
    
    plt.hist(temperatures, bins=10, edgecolor='black')
    plt.title('Гистограмма температур')
    plt.xlabel('Температура (°C)')
    plt.ylabel('Количество дней')
    plt.show()



def plot_filtered_histogram(filename):
    temperatures = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            temp = float(row['temperature'])
            if temp >= 13:
                temperatures.append(temp)
    
    plt.hist(temperatures, bins=10, edgecolor='black')
    plt.title('Гистограмма температур (выше 13°C)')
    plt.xlabel('Температура (°C)')
    plt.ylabel('Количество дней')
    plt.show()
 

plot_histogram('file.csv')
plot_filtered_histogram('file.csv')