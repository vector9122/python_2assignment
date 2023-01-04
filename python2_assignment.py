


# Importing necessary libraries


import pandas as pd
import matplotlib.pyplot as plt


# Loading the datset

data = pd.read_csv("Grow_Locations.csv")

print(data.shape)

# By initital investigation, it seems that the longitude has been incorrectly renamed as lattitude and vice versa. Therefore renaming the two columns


data.rename(columns={"Latitude":"Longitude","Longitude":"Latitude"}, inplace= True)


# Data Cleaning

# Cleaning the data for acceptable values of latitude and longitudes and also dropping rows having null values




data = data[(data["Latitude"]>-90.681) & (data["Latitude"]<90)]
data = data[(data["Longitude"]>-180) & (data["Longitude"]<180)]


data.dropna(inplace=True)
#checking the shape of the data after dropping rows having null values of sensor's serialID

print(data.shape)


data = data[(data["Latitude"]!=0) & (data["Longitude"]!=0)]

# Checking the no. of rows left after cleaning the data

print(data.shape)

# After cleaning the data we are left with only 33648 points

# Creating the bounding box for the map

boundaries = [-10.592,1.6848,50.681,57.985]


# ## Loading the map png file



map = plt.imread('map7.png')


# ## Plotting points on the map




fig, ax = plt.subplots(figsize = (15,13))
ax.scatter(data.Longitude, data.Latitude, zorder=1, alpha= 0.2, c='r', s=10)
ax.set_title('Plotting Grow Data on UK Map')
ax.set_xlim(boundaries[0],boundaries[1])
ax.set_ylim(boundaries[2],boundaries[3])
ax.imshow(map, zorder=0, extent = boundaries, aspect= 'equal')


# ## Saving the output map image to a file

ax.figure.savefig('output.png',bbox_inches='tight')


# Please note Ahmed Qasim's article on plotting geographic data on a map has been referenced while writing the above code.
# Here is the link  https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db
