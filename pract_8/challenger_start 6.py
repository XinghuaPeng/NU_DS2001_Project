# Practicum 7
# Prof. Rachlin

import math
import matplotlib.pyplot as plt

# Earth's radius varies because the earth is not a perfect sphere.
# Use this number as it is considered the global average.
EARTH_RADIUS = 6371

def distance(lat1, long1, lat2, long2):
    """ Get the distance in kilometers between two geographical points.
    Your calculation can ignore the curvature of the earth. Use
    euclidean distance. 1 degree of distance = 1/360 the circumference of
    the Earth. Radius of Earth = 6371 km """
   
    """
    Calculates the distance in miles between two points on the earth's surface
    described by latitude and longitude.
    Parameters:

    Return:
            float - distance in miles between the two points
    """

    R_earth = 6371
    
    delta_lat = float(lat2) - float(lat1)
    delta_long = float(long2) - float(long1)
    
    dist_delta = (delta_lat ** 2 + delta_long ** 2)**.5
    circumference = 2 * math.pi * R_earth
    distance = dist_delta * circumference / 360
    
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
            
            id_val = vals[0]
            compare_lat = vals[2]
            compare_lon = vals[3]
            
            if id_val != "" and compare_lat != "" and compare_lon != "":
                compare_lat = float(compare_lat)
                compare_lon = float(compare_lon)
                dist = distance(lat, lon, compare_lat, compare_lon)
                
                if dist < max_dist:
                    near.append(id_val)

    return near

def temp_data_at_stations(year, stations):
    
    weather_data = []
    
    filename = str(year)+".csv"
    
    with open(filename, 'r') as infile:
        data = infile.readlines() 
        for i in range(len(data)):
             vals = data[i].strip().split(",")
             id = vals[0]
             if id in stations:
                 weather_data.append([vals[0], int(vals[2]), int(vals[3]), float(vals[4])])
    
    return weather_data

def average_temp_at_stations(month, day, year, station_weather, stations):
    """ Average temperature on the specified month, day, year 
    Note: We re-read the data every time we call this function.
    This is simple but not efficient.  Better would be to
    read the data once into a list of lists or a list of dictionaries.
    
    month - the month we are filtering for
    day - the day of the month
    year - the year: filename is year.csv
    stations - the list of stations to include in our average """

    temps = []
              
    for data in station_weather:
        if data[1] == month:
            if data[2] == day:
                temps.append(data[3])
            
    return sum(temps) / len(temps)

def plot_results(days, avg_temps):
    """ Plot average temperature over month of january """
    plt.plot(days, avg_temps)
    plt.title("Average temperature reported by nearby stations in January 1986")
    plt.show()

def main():

    # Find stations within 100km of Cape Canaveral
    near = nearby_stations(28.3922, -80.6077, 100.0)
    
    station_weather = temp_data_at_stations(1986, near)
    print(station_weather)
    temp_of_the_day = average_temp_at_stations(1, 28, 1986, station_weather, near)
    print("The average temperature for Jan 28th, 1986:", temp_of_the_day)
    
    # compute the average daily temperature for January, 1986
    jan_temp = []
    for i in range(1, 32):
        temp = average_temp_at_stations(1, i, 1986, station_weather, near)
        jan_temp.append(temp)
        
    # Plot the average daily temperature for January, 1986
    plot_results(range(1,32), jan_temp)


if __name__ == "__main__":
    main()
