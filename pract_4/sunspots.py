"""
Xinghua Peng
DS 2000: Intro to Programming with Data


Date: Thu Sep 29 11:49:35 2022
    
File: sunspots.py
    
Description:

Record my calculations and estimates: 
# divide number of years by the number of intervals during those years
# 2022 - 1749 = 273
# peaks = 25
# cycle lengths = 273 / 25 = 10.92

Use 11.5 for question 2 - sunspot_cycle.png

"""

import matplotlib.pyplot as plt

def main():

##Question 1 - sunspot_history.png

    # Read all lines into a list of lines
    # Use a loop to extract the data
    months = []
    num_sunspots = []
    
    with open("sunspots.csv", "r") as infile:
        header = infile.readline()
        lines = infile.readlines()

    index = 0
    while index < len(lines):
        vals = lines[index].split(",")
        months.append(float(vals[0]))
        num_sunspots.append(float(vals[1]))
        index += 1
    
    #print(months)
    #print(num_sunspots)
    
    # Create a canvas/figure
    plt.figure(figsize=(10,2), dpi=200)
    
    ## Plot Customization
    
    # Set the x-axis and y-axis label for the graph1
    plt.xlabel("Years")
    plt.ylabel("Average Daily Sunspots Numbers")
    
    # Set the title for the graph1
    plt.title("Number of Sunspots from 1749 to 2022")
    
    # Save the graph and exclude extra whitespace around the graph
    plt.scatter(months, num_sunspots, marker = ".", s = 10)
    plt.savefig("sunspot_history.png", bbox_inches = "tight")
    
    # Display the current graph
    plt.show()
   
# Determine the Estimate - divide # of years by the number of intervals during those years

#cycle_length = (2022 - 1749) / 25
#print("Cycle length:", cycle_length)

##Question 2 - sunspot_cycle.png
 
    cycle = 11.5
    index = 0
    transform_cycles = []
    while index < len(months):
        transform_cycles.append(months[index] % cycle)
        index += 1
    
    # Create a canvas/figure
    plt.figure(figsize=(5,5), dpi=200)
    
    # Set the x-axis and y-axis label for the graph1
    plt.xlabel("Cycles")
    plt.ylabel("Average Daily Sunspots Numbers")
    
    # Set the title for the graph1
    plt.title("Sunspots Cycle Visualization") 
    plt.scatter(transform_cycles, num_sunspots, marker = ".", s = 10)   
    plt.savefig("sunspot_cycle.png", bbox_inches = "tight")
    
    # Display the current graph
    plt.show()


main()