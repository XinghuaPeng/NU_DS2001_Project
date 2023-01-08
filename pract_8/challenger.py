"""

Xinghua Peng
DS 2001: Intro to Programming with Data

Filename: challenger.py
    
Description: This program analyze temperature data for weather stations near 
            the NASA facility.This program reads temperature and weather station 
            data to determine the average reported temperature on that fateful day.
             
Program Outputs: 
    - Identify all weather stations within 100km of Capr Canaveral
        Ans: ['722011', '722011', '722040', '722040', '722045', '722045', 
              '722046', '722046', '722050', '722051', '722053', '722053', 
              '722056', '722057', '722057', '722058', '722361', '722361', 
              '747930', '747930', '747940', '747940', '747945', '747946', 
              '747946', '747950', '747950', '749047', '994951', '995450', 
              '997354', '997806', '998275']
    - The final average temperature estimate: 32.96666666666667
    - The temperature was close to freezing!!!
    - How might this have affected the Space Shuttle's O-Ring seals?
        Ans: Since within the almost freezing average temperature, as mentioned
        in YouTube video the Space Shuttle's O-Ring seals shows no resilience, 
        and can't strech back when you put pressure on it, under the situation 
        that it's at a temperature of 32 degrees F / in the Iced water. 
    - What do you notice about January 28th?
        Ans: The temperature at January 28th is the lowest during the month (14.1 degrees F).
        and the temperature was close to freezing. 
    - Had they pushed back the launch by a single day or two, would it have made a difference?
        Ans: If they pushed back the launch by a single day or two, it wouldn't have made a difference.
        Please refer to the following analysis for more informatin. 
        - single day - 27 (24.1 degrees F) or 29 (16.4 degrees F) - both lower than 32 degrees F --> No difference
        - two day - 26 (30.6 degrees F) or 31 (31.3 degrees F) - both lower than 32 degrees F --> No difference
      
"""


import math
import matplotlib.pyplot as plt


def distance(alat, alon, blat, blon):
    """ Get the distance in kilometers between two geographical points.
    Your calculation can ignore the curvature of the earth. Use
    euclidean distance. 1 degree of distance = 1/360 the circumference of
    the Earth. Radius of Earth = 6371 km """
   
    R_earth = 6371
    euclidean = ((alat - blat)**2 + (alon - blon)**2)**0.5
    circumference = 2 * math.pi * R_earth
    distance = euclidean * circumference / 360
    
    return distance
    

def nearby_stations(lat, lon, max_dist):
    """ Fetch the station ids for all stations that are within max_dist
    of the specified latitude (lat) and longitude (lon) 
    Ignore stations with missing ID, latitude or longitude. 
    (and don't forget the newline at the end of each line!) 
     
    lat - target latitude
    lon - target longitude
    max_dist - the maximum distance in kilometers
    
    """
    near = []

    with open("stations.csv") as infile:
        
        data = infile.readlines()
        for i in range(len(data)):
            vals = data[i].strip().split(",")
            
            station_id = vals[0]
            lat_compare = vals[2]
            lon_compare = vals[3]
            
            if station_id != "" and lat_compare != "" and lon_compare != "":
                lat_compare = float(lat_compare)
                lon_compare = float(lon_compare)
                dist = distance(lat,lon,lat_compare,lon_compare)
            
                if dist < max_dist:
                    near.append(station_id)
             
    return near

def stations_temp_data(year, stations):
    
    weather = []
    filename = str(year)+".csv"
    
    with open(filename, 'r') as infile:
        data = infile.readlines() 
        for i in range(len(data)):
             vals = data[i].strip().split(",")
             stations_id = vals[0]
             if stations_id in stations:
                 weather.append([vals[0], int(vals[2]), int(vals[3]), float(vals[4])])
    
    return weather

def average_temp_at_stations(month, day, year, station_weather, stations):
    """ Average temperature on the specified month, day, year 
    Note: We re-read the data every time we call this function.
    This is simple but not efficient.  Better would be to
    read the data once into a list of lists or a list of dictionaries.
    
    month - the month we are filtering for
    day - the day of the month
    year - the year: filename is year.csv
    stations - the list of stations to include in our average """
    
    filename = str(year)+".csv"
    temps = []
    
    for data in station_weather:
        if data[1] == month:
            if data[2] == day:
                temps.append(data[3])
            
    return sum(temps) / len(temps)

    # Alternative method - TBD
    #with open(filename, 'r') as infile:
        #data = infile.readlines()
        #for i in range(len(data)):
            #vals = data[i].strip().split(",")
             
            #if int(vals[2]) == month and int(vals[3]) == day and vals[0] in stations:
                #temps.append(float(vals[4]))
               
    return sum(temps) / len(temps)



def plot_results(days, avg_temps):
    """ Plot average temperature over month of january """
    
    # Create a canvas and plot the results
    plt.plot(days, avg_temps)
 
    # Plot Customization
    plt.title("Averge Temperature (F) at Cape Canaveral Over Month of January (1986)")
    plt.xlabel("day")
    plt.ylabel("Temperature (Degrees F)")
    plt.grid()
    plt.savefig("jan1986_temps.png", bbox_inches='tight')
    plt.show()
    
    
def main():
 
    # Find stations within 100km of Cape Canaveral
    near = nearby_stations(28.3922, -80.6077, 100.0)
    print(near)
    
    # Find the Average temperature for Jan 28th, 1986
    station_weather = stations_temp_data(1986, near)
    temp = average_temp_at_stations(1, 28, 1986, station_weather, near)
    print("The average temperature for Jan 28th, 1986:", temp)
    
    # For each day of the month, find the average temperature
    # at stations near Cape Canaveral
    jan_temps = []
    for i in range(1, 32):
        temp = average_temp_at_stations(1, i, 1986, station_weather, near)
        jan_temps.append(temp)
    
    # Plot the average daily temperature for January, 1986
    plot_results(range(1,32), jan_temps)



if __name__ == "__main__":
    main()
