"""
Xinghua Peng
DS 2000: Intro to Programming with Data


Date: Thu Sep 15 11:57:34 2022
    
File: spaceflight.py
    
Description: A program that takes a distance in light years, and a spacecraft speed in miles per
hour. The program ouputs how long it would take your spacecraft to reach its destination in years.

Outputs & Results: 
#EXAMPLE 1:
   Enter the spacecraft's speed [mph]: 437000

   Enter the distance [light-years]: 4.25
   Your spacecraft will reach its destination in 6512.1 years.
    
#EXAMPLE 2: 
    Enter the spacecraft's speed [mph]: 34391

    Enter the distance [light-years]: 10.3
    Your spacecraft will reach its destination in 200543.2 years.

"""

# Input parameters including spacecraft speed [mph] and distance [light-years]

spacecraft_speed_mph = float(input ("Enter the spacecraft's speed [mph]: "))
distance = float (input ("Enter the distance [light-years]: "))

## Calculate the spaceflight travel time in years, rounded to the nearest year

# Compute the total number of miles in one light-year
# Light travels 186,000 miles per second
total_distance_miles = distance * 186000 * 3600 * 24 * 365.25 # 24 hours = 1 day & Assume 365.25 days per year

# Compute spaceflight travel time in hours

time_hrs = total_distance_miles / spacecraft_speed_mph

# Convert hours to years

time_yrs = round((time_hrs / 24 / 365.25), 1)

# Result Output

print("Your spacecraft will reach its destination in", time_yrs, "years.")


