import shapefile
from descartes import PolygonPatch
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.colors
import pandas as pd
import numpy as np

direc = "C:/Users/codyg/Onedrive/Desktop/UMAP_work/UMAP_Exploration/Data/"
shape = "Help_Shape/nh_noshore_29Jan13/nh_noshore_29Jan13.shp"
edi = "HELP_EDI_data.xlsx"
sf = shapefile.Reader(direc+shape)
data = pd.ExcelFile(direc+edi)
neighbor_data = pd.read_excel(data, 'Neighbourhood', skiprows=6, idex_col = 'N_CODE')


### Choose your variable of interest here
edi_var = 'PCTPHYRI_2'

# Janky plotting - make a fake plot with a color bar that takes defined percentage steps

plt.figure()
min, max = (0, 1)
step = .02
viridis = cm.get_cmap('viridis')
# Using contourf to provide my colorbar info, then clearing the figure
Z = [[0,0],[0,0]]
levels = np.arange(min,max+step,step)
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
    edi_row_idx = np.where(neighbor_data['N_CODE'] == N_code)[0]
    if len(edi_row_idx> 0):
        edi_row_idx = int(edi_row_idx)
        val = neighbor_data.iloc[edi_row_idx][edi_var]
        color_rgb = viridis(val/100)
        color_hex = matplotlib.colors.rgb2hex(color_rgb)
    else:
        color_hex = '#ffffff'
    poly_geo=poly.__geo_interface__
    ax.add_patch(PolygonPatch(poly_geo, fc=color_hex, ec='#000000', alpha=0.5, zorder=2 ))
    N_codes.append(N_code)
    neighborhoods.append(neighborhood)
    citys.append(city)
plt.colorbar(CS3)
ax.axis('scaled')
plt.title(f'EDI dist for {edi_var}')
plt.show()