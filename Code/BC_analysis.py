import shapefile
import matplotlib.pyplot as plt

direc = "C:/Users/codyg/Onedrive/Desktop/UMAP_work/UMAP_Exploration/Data/Help_Shape/nh_noshore_29Jan13/nh_noshore_29Jan13.shp"
sf = shapefile.Reader(direc)

plt.figure()
for shape in sf.shapeRecords():
    for i in range(len(shape.shape.parts)):
        i_start = shape.shape.parts[i]
        if i==len(shape.shape.parts)-1:
            i_end = len(shape.shape.points)
        else:
            i_end = shape.shape.parts[i+1]
        x = [i[0] for i in shape.shape.points[i_start:i_end]]
        y = [i[1] for i in shape.shape.points[i_start:i_end]]
        plt.plot(x,y)
plt.show()