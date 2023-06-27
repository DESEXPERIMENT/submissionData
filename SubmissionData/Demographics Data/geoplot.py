
import json # reading geojson files
data = json.load(open("nyc-neighbourhoods.geojson"))
import matplotlib.pyplot as plt # plotting data
fig = plt.figure() # create a figure to contain the plot elements
ax = fig.gca(xlabel="Longitude", ylabel="Latitude")


from shapely.geometry import asShape # manipulating geometry
from descartes import PolygonPatch
count = 0
for feat in data["features"]:
# convert the geometry to shapely
    geom = asShape(feat["geometry"])
    x, y = geom.centroid.x, geom.centroid.y
    # plot the centroids
    ax.plot(x, y)
    # ax.text(x,y,str(count))
    count+=1
    # ax.text(x, y, feat["properties"]["ward"], fontsize=6, bbox = dict(fc='w', alpha=0.3))
    # plot the polygon features: type help(PolygonPatch) for more args
    ax.add_patch(PolygonPatch(feat["geometry"], fc='grey', ec='blue',
                alpha=0.6, lw=2, ls='-', zorder=2))

ax.clear # clear the axes memory
plt.savefig("NYC.png")
plt.show()
