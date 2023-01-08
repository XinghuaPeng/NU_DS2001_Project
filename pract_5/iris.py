"""
Xinghua Peng
DS 2000: Intro to Programming with Data


Date: Thu Oct  6 11:58:05 2022
    
File: iris.py
    
Description: This program read the Fischer dataset, gather some summary statistics,
and perform exercise in machine learning. 

Table for Part 1: 
SPECIES 	           ATTRIBUTE 	     MIN 	 AVERAGE 	 MAX
Iris setosa 	       Sepal Length      4.3       5.0       5.8
Iris versicolor 	   Sepal Length      4.9       5.9       7.0
Iris verginica 	   Sepal Length      4.9       6.6       7.9
Iris setosa 	       Sepal Width       2.3       3.4       4.4
Iris versicolor 	   Sepal Width       2.0       2.8       3.4
Iris verginica 	   Sepal Width       2.2       3.0       3.8
Iris setosa 	       Petal Length      1.0       1.5       1.9
Iris versicolor 	   Petal Length      3.0       4.3       5.1
Iris verginica 	   Petal Length      4.5       5.6       6.9
Iris setosa 	       Petal Width       0.1       0.2       0.6
Iris versicolor 	   Petal Width       1.0       1.3       1.8
Iris verginica 	    Petal Width      1.4       2.0       2.5


"""

def main():
    
    # Read the iris dataset into a list of rows
    
    with open("iris.csv", "r") as infile:
        data = infile.readlines()
    
    sepal_length = []
    sepal_width = []
    petal_length = []
    petal_width = []
    species = []
    
    
    index = 0
    while index < len(data):
        
        # Split the record into five distinct values:
        vals = data[index].strip().split(",")
        sepal_length.append(float(vals[0]))
        sepal_width.append(float(vals[1]))
        petal_length.append(float(vals[2]))
        petal_width.append(float(vals[3]))
        species.append(str(vals[4]))
        index += 1

    
    # Create a summary report

    # Slice data -- Hardcode method :)
    
    # Sepal Length
    setosa_sepal_length_min = min(sepal_length[0:50])
    setosa_sepal_length_avg = sum(sepal_length[0:50]) / 50
    setosa_sepal_length_max = max(sepal_length[0:50])
    
    versicolor_sepal_length_min = min(sepal_length[50:100])
    versicolor_sepal_length_avg = sum(sepal_length[50:100]) / 50
    versicolor_sepal_length_max = max(sepal_length[50:100])
    
    verginica_sepal_length_min = min(sepal_length[100:])
    verginica_sepal_length_avg = sum(sepal_length[100:]) / 50
    verginica_sepal_length_max = max(sepal_length[100:])
    
    print("SPECIES \t ATTRIBUTE \t MIN \t AVERAGE \t MAX")
    print("Iris setosa \t Sepal Length", round(setosa_sepal_length_min,1), round(setosa_sepal_length_avg,1), round(setosa_sepal_length_max,1))
    print("Iris versicolor \t Sepal Length", round(versicolor_sepal_length_min,1), round(versicolor_sepal_length_avg,1), round(versicolor_sepal_length_max,1))
    print("Iris verginica \t Sepal Length", round(verginica_sepal_length_min,1), round(verginica_sepal_length_avg,1), round(verginica_sepal_length_max,1))
    
    # Sepal Width
    setosa_sepal_width_min = min(sepal_width[0:50])
    setosa_sepal_width_avg = sum(sepal_width[0:50]) / 50
    setosa_sepal_width_max = max(sepal_width[0:50])
    
    versicolor_sepal_width_min = min(sepal_width[50:100])
    versicolor_sepal_width_avg = sum(sepal_width[50:100]) / 50
    versicolor_sepal_width_max = max(sepal_width[50:100])
    
    verginica_sepal_width_min = min(sepal_width[100:])
    verginica_sepal_width_avg = sum(sepal_width[100:]) / 50
    verginica_sepal_width_max = max(sepal_width[100:])
    
    print("Iris setosa \t Sepal Width", round(setosa_sepal_width_min,1), round(setosa_sepal_width_avg,1), round(setosa_sepal_width_max,1))
    print("Iris versicolor \t Sepal Width", round(versicolor_sepal_width_min,1), round(versicolor_sepal_width_avg,1), round(versicolor_sepal_width_max,1))
    print("Iris verginica \t Sepal Width", round(verginica_sepal_width_min,1), round(verginica_sepal_width_avg,1), round(verginica_sepal_width_max,1))
    
    
    # Petal Length
    setosa_petal_length_min = min(petal_length[0:50])
    setosa_petal_length_avg = sum(petal_length[0:50]) / 50
    setosa_petal_length_max = max(petal_length[0:50])
    
    versicolor_petal_length_min = min(petal_length[50:100])
    versicolor_petal_length_avg = sum(petal_length[50:100]) / 50
    versicolor_petal_length_max = max(petal_length[50:100])
    
    verginica_petal_length_min = min(petal_length[100:])
    verginica_petal_length_avg = sum(petal_length[100:]) / 50
    verginica_petal_length_max = max(petal_length[100:])
    
    print("Iris setosa \t Petal Length", round(setosa_petal_length_min,1), round(setosa_petal_length_avg,1), round(setosa_petal_length_max,1))
    print("Iris versicolor \t Petal Length", round(versicolor_petal_length_min,1), round(versicolor_petal_length_avg,1), round(versicolor_petal_length_max,1))
    print("Iris verginica \t Petal Length", round(verginica_petal_length_min,1), round(verginica_petal_length_avg,1), round(verginica_petal_length_max,1))
    
    
    # Petal Width
    setosa_petal_width_min = min(petal_width[0:50])
    setosa_petal_width_avg = sum(petal_width[0:50]) / 50
    setosa_petal_width_max = max(petal_width[0:50])
    
    versicolor_petal_width_min = min(petal_width[50:100])
    versicolor_petal_width_avg = sum(petal_width[50:100]) / 50
    versicolor_petal_width_max = max(petal_width[50:100])
    
    verginica_petal_width_min = min(petal_width[100:])
    verginica_petal_width_avg = sum(petal_width[100:]) / 50
    verginica_petal_width_max = max(petal_width[100:])
    
    #print("SPECIES \t ATTRIBUTE \t MIN \t AVERAGE \t MAX")
    print("Iris setosa \t Petal Width", round(setosa_petal_width_min,1), round(setosa_petal_width_avg,1), round(setosa_petal_width_max,1))
    print("Iris versicolor \t Petal Width", round(versicolor_petal_width_min,1), round(versicolor_petal_width_avg,1), round(versicolor_petal_width_max,1))
    print("Iris verginica \t Petal Width", round(verginica_petal_width_min,1), round(verginica_petal_width_avg,1), round(verginica_petal_width_max,1))
    
    
    # Slice data - Using for loops
    # I didn't finished the for loops method in time.
    # Thank you so much for your understanding!
    
    """species_test = ["setosa","versicolor","verginica"]
    for sp in species_test:
        if sp == "setosa":
            lower = 0
            upper = 50
        
        if sp == "versicolor":
            lower = 50
            upper = 100
        
        else:
            lower = 100
            Upper = /
        
        sepal_length_new = sepal_length[lower:upper]
        petal_width_new = sepal_length[lower:upper]
        sepal_length_new = sepal_length[lower:upper]
        petal_width_new = sepal_length[lower:upper]
        
        # Sepal Length
        print("Irish", sp, min(sepal_length_new = sepal_length[lower:upper]), sum(sepal_length[lower:upper])/50, max(sepal_length[lower:upper]))
        
        # Sepal Width
        
        # Petal Length
        
        # Petal Width
        
        ## I am not sure how to go forward with this code during the lab :(
        ## Thank you so much for your understanding :)
        """
    
main()