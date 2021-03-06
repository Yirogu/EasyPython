#
# import gmaps
# gmaps.configure(api_key='AIzaSyAYWOnoljOTl8HpSKNDieLDbHE-NTD9x1k')
#
#
# new_york_coordinates = (40.75, -74.00)
# show = gmaps.figure(center=new_york_coordinates, zoom_level=12)
# show
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
import platform
import webbrowser
output_file("gmap.html")

map_options = GMapOptions(lat=30.2861, lng=-97.7394, map_type="roadmap", zoom=11)

# For GMaps to function, Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value below with your personal API key:
p = gmap("AIzaSyAYWOnoljOTl8HpSKNDieLDbHE-NTD9x1k", map_options, title="Austin")

source = ColumnDataSource(
    data=dict(lat=[ 30.29,  30.20,  30.29],
              lon=[-97.70, -97.74, -97.78])
)

p.circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, source=source)

if platform.system() == "Linux" :
    webbrowser.open('gmap.html')
# else :
#     show(p)
