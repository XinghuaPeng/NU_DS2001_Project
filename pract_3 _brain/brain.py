"""
Xinghua Peng
DS 2000: Intro to Programming with Data


Date: Thu Sep 22 11:53:37 2022
    
File: brain.py
    
Description: This program demonstrates brain/body mass ratio in five mammals

Question 3:
Interpret my results: According to the plot, Humans have the largest brain/body mass ratio (approxiamtely 18.48) because it has the highest/steepest slope within the scatter plot.  
To put it in another way, a higher/steeper slope (y/x or Brain Mass/Body Mass) means larger brain/body mass ratio compared to the other four mammals. 
"""

import matplotlib.pyplot as plt

def main():
    
    # Open the file and read the data
    filename = "brain.txt"
    with open (filename, "r") as infile:
        infile.readline()
        infile.readline()
        infile.readline()
        infile.readline()
        infile.readline()
        infile.readline()
        
        # Read the data: name & body mass & brain mass
        name1 = infile.readline().strip()
        body1 = float(infile.readline())
        brain1 = float(infile.readline())
        
        name2 = infile.readline().strip()
        body2 = float(infile.readline())
        brain2 = float(infile.readline())
        
        name3 = infile.readline().strip()
        body3 = float(infile.readline())
        brain3 = float(infile.readline())
        
        name4 = infile.readline().strip()
        body4 = float(infile.readline())
        brain4 = float(infile.readline())
        
        name5 = infile.readline().strip()
        body5 = float(infile.readline())
        brain5 = float(infile.readline())
        
        
        
    # Create a canvas / figure for the scatter plot
    plt.figure(figsize=(6,4),dpi=150)
    
    plt.plot(body1,brain1, 'o', label = name1)
    plt.plot(body2,brain2, 'x', label = name2) # Use a distinctive marker for human
    plt.plot(body3,brain3, 'o', label = name3)
    plt.plot(body4,brain4, 'o', label = name4)
    plt.plot(body5,brain5, 'o', label = name5)
    
        
    # Plot customization
    plt.grid()
    # Give the graph a descriptive title
    plt.title("Brain/Body Mass Ratio in Mammals - Scatter Plot")
    # Label X and Y axes
    plt.xlabel("Body Mass [kilograms]")
    plt.ylabel("Brain Mass [grams]")
    
    # Add a legend identifying each animal in the plot
    plt.legend()
    
    # Use logarithmic scaling
    plt.xscale("log")
    plt.yscale("log")
    
    plt.savefig("brain.png")
    
    plt.show()
    

    ## Create a bar chart comparing the brain/body mass ratios
    plt.figure(figsize=(6,4),dpi=150)
    # Compute the each mammal's ratio
    
    ratio1 = float(brain1 / body1) # Formula: ratio = brain mass [grams] / body mass [kilograms]
    ratio2 = float(brain2 / body2)
    ratio3 = float(brain3 / body3)
    ratio4 = float(brain4 / body4)
    ratio5 = float(brain5 / body5)
    
    # Generate bars in a bar chart & Plot the data points
    
    plt.bar(name1, ratio1)
    plt.bar(name2, ratio2)
    plt.bar(name3, ratio3)    
    plt.bar(name4, ratio4)
    plt.bar(name5, ratio5)
    
    # Plot Customization
    plt.grid()
    # Descriptive title
    plt.title("Brain/Body Mass Ratio in Mammals - Bar Chart")
    # Change the axis labels & scale
    plt.xlabel("Mammals")
    plt.ylabel("Brain/Body Mass Ratios [grams/kilograms]")
    plt.ylim(0,20) 
    # Add a legend identifying each animal in the plot
    plt.legend()
    
    plt.savefig("ratio.png")
    
    plt.show()
    
    
main()