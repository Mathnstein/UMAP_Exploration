import shapefile
import os
from descartes import PolygonPatch
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors
import pandas as pd
import numpy as np
import geopandas as gpd

#from ipywidgets import widgets, interactive
#import geopandas as gpd
#import pysal as ps
#from pysal.contrib.viz import mapping as maps

def _main():
    data_directory = os.path.join(os.getcwd(), 'Data')
    shape_file = os.path.join(data_directory, 'Help_Shape', 'nh_noshore_29Jan13/nh_noshore_29Jan13.shp')
    edi_file = os.path.join(data_directory, 'HELP_EDI_data.xlsx')
    sf = shapefile.Reader(shape_file)
    neighbor_data = pd.read_excel(edi_file, sheet_name='Neighbourhood', skiprows=6, index_col='N_CODE', engine='openpyxl')


    ### Choose your variable of interest here
    keys = neighbor_data.keys()
    # editot_x: 2-6,
    # edival_x: 7-11,
    # PCTPHYRI_x: 12-16,
    # PCTSOCRI_x: 17-21,
    # PCTEMORI_x: 22-26,
    # PCTLANRI_x: 27-31,
    # PCTCOMRI_x: 32-36,
    # PCT_EVERR_x: 37-41,
    # PCTEVER4_x: 42-46
    edi_var = keys[36]
    col_vals = neighbor_data[edi_var]/100
    # Janky plotting - make a fake plot with a color bar that takes defined percentage steps

    plt.figure()
    min_val, max_val = np.min(col_vals), np.max(col_vals)
    step = .05
    viridis = cm.get_cmap('viridis')
    # Using contourf to provide my colorbar info, then clearing the figure
    Z = [[0,0],[0,0]]
    levels = np.arange(min_val,max_val+step,step)
    CS3 = plt.contourf(Z, levels, cmap=viridis)
    plt.clf()

    # Here I plot the shape file, color by the predefined edi metric and then save off the nhbrhood, city and N_code for each poly
    N_codes = []
    neighborhoods = []
    citys = []
    fig = plt.figure() 
    ax = fig.gca()
    for poly, shape in zip(sf.shapes(), sf.shapeRecords()):
        N_code = shape.record[1]
        neighborhood = shape.record[2]
        city = shape.record[4]
        edi_row_idx = np.where(neighbor_data.index == N_code)[0]
        if len(edi_row_idx> 0):
            edi_row_idx = int(edi_row_idx)
            val = col_vals.iloc[edi_row_idx]
            if np.isnan(val):
                print(f' NaN: {N_code}, {neighborhood}, {city}')
                color_hex = '#000000'
            else:
                color_rgb = viridis(val)
                color_hex = matplotlib.colors.rgb2hex(color_rgb)
        else:
            #The N_code did not exist
            print(f'Not in List: {N_code}, {neighborhood}, {city}')
            color_hex = '#ffffff'
        poly_geo=poly.__geo_interface__
        ax.add_patch(PolygonPatch(poly_geo, fc=color_hex, ec='#000000', alpha=1, zorder=2 ))
        N_codes.append(N_code)
        neighborhoods.append(neighborhood)
        citys.append(city)
    plt.colorbar(CS3)
    ax.axis('scaled')
    plt.title(f'EDI dist for {edi_var}')
    plt.show()


if __name__ == "__main__":
    _main()