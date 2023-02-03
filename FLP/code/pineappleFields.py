# -*- coding: utf-8 -*-
"""

@author: isaldiviagonzatti
"""

import geopandas as gpd
import os
import folium
import webbrowser
import pandas as pd

os.getcwd()
os.chdir(r'C:\Users\isaldiviagonzatti\OneDrive - Wageningen University & Research\WUR\Thesis\MSc_ENR_Pineapple\Spatial_Optimization')

pinejson = gpd.read_file("pineapple2019.json")

pinejson.crs

pinejson.head()

#convert projected coordinate reference system to a 
#geographic coordinate system

pinejson = pinejson.to_crs(epsg=4326)
pinejson.crs
pinejson.head()

pinejson.plot()


#adding centroids to dataframe
#solution from https://geopandas.org/en/stable/gallery/polygon_plotting_with_folium.html
# Project to NAD83 projected crs
pinejson = pinejson.to_crs(epsg=2263)

# Access the centroid attribute of each polygon
pinejson['centroid'] = pinejson.centroid

# Project to WGS84 geographic crs

# geometry (active) column
pinejson = pinejson.to_crs(epsg=4326)

# Centroid column
pinejson['centroid'] = pinejson['centroid'].to_crs(epsg=4326)

pinejson.head()


#solution from stack to use folium with html
#https://stackoverflow.com/questions/36969991/folium-map-not-displaying

class Map:
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start
    
    def showMap(self):
        #create basemap 
        my_map = folium.Map(location=[11, -83], zoom_start=10, tiles='CartoDB positron')
        # add polygons, solution from https://geopandas.org/en/stable/gallery/polygon_plotting_with_folium.html
        for _, r in pinejson.iterrows():
            # Without simplifying the representation of each borough,
            # the map might not be displayed
            sim_geo = gpd.GeoSeries(r['geometry']) #.simplify(tolerance=0.001)
            geo_j = sim_geo.to_json()
            geo_j = folium.GeoJson(data=geo_j,
                                   style_function=lambda x: {'fillColor': 'orange'})
            geo_j.add_to(my_map)
        
        #add popup info with hectare info 
        #for _, r in pinejson.iterrows():
        #    lat = r['centroid'].y
        #    lon = r['centroid'].x
        #    folium.Marker(location=[lat, lon],
        #                  popup='area: {}'.format(r['area_ha'])).add_to(my_map)

        #Display the map
        my_map.save("map.html")
        webbrowser.open("map.html")


#Define coordinates of where we want to center our map
coords = [11, -83]
map = Map(center = coords, zoom_start = 13)
map.showMap()


import osmnx as ox
G = ox.graph_from_address("", dist=2000)
fig, ax =ox.plot_graph(G)

fig, ax = ox.plot_graph(G, filepath='cumbres2000.svg', save=True, show=False, close=True)


# Set filepath
fp = r"roadNetwork\Costa_Rica.shp"

# Read file using gpd.read_file()
data = gpd.read_file(fp)

data.plot()
data = data.to_crs(epsg=4326)

pd.set_option('display.max_columns', None)
data.head()

