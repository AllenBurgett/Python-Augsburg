from bokeh.plotting import figure, show
from bokeh.models import HoverTool, ColumnDataSource
import itertools
import shapefile
import pandas as pd
import datetime
import requests
import zipfile
try:
    from StringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO
import os

# Get FIPS data
state_fips = pd.read_csv('http://www2.census.gov/geo/docs/reference/state.txt', sep='|')
state_fips.drop('STATE', axis=1, inplace=True)
county_fips = pd.read_csv('http://www2.census.gov/geo/docs/reference/codes/files/national_county.txt', header=None)
county_fips.columns = ['STATE', 'STATEFP', 'COUNTYFP', 'COUNTYNAME', 'CLASSFP']
all_fips = pd.merge(county_fips, state_fips, left_on='STATE', right_on='STUSAB')

# Get USA map data
# https://www.census.gov/geo/maps-data/data/cbf/cbf_counties.html
shp = None
dbf = None
last_year = datetime.datetime.now().year - 1
url = 'http://www2.census.gov/geo/tiger/GENZ{}/shp/cb_{}_us_county_20m.zip'.format(last_year, last_year)  # Lowest
#url = 'http://www2.census.gov/geo/tiger/GENZ{}/shp/cb_{}_us_county_5m.zip'.format(last_year, last_year)
#url = 'http://www2.census.gov/geo/tiger/GENZ{}/shp/cb_{}_us_county_500k.zip'.format(last_year, last_year)  #Highest
response = requests.get(url)
with zipfile.ZipFile(StringIO(response.content)) as z:
    for fname in z.namelist():
        name, ext = os.path.splitext(fname)
        if ext == '.shp':
            shp = StringIO(z.read(fname))
            #shp = z.open(fname)
        elif ext == '.dbf':
            #dbf = z.open(fname)
            dbf = StringIO(z.read(fname))
        else:
            pass
sf = shapefile.Reader(shp=shp, dbf=dbf)

# Munge map data for bokeh
lats = []
lons = []
county = []
state = []
for shprec in sf.shapeRecords():
    statefp = int(shprec.record[0])
    countyfp = int(shprec.record[1])
    fip = all_fips.loc[(all_fips['STATEFP'] == statefp) & (all_fips['COUNTYFP'] == countyfp)]
    county.append(fip['COUNTYNAME'])
    state.append(fip['STATE_NAME'])
    lat, lon = map(list, zip(*shprec.shape.points))
    lat = [l if l < 0 else l-360 for l in lat]
    indices = shprec.shape.parts.tolist()
    lat = [lat[i:j] + [float('NaN')] for i, j in zip(indices, indices[1:]+[None])]
    lon = [lon[i:j] + [float('NaN')] for i, j in zip(indices, indices[1:]+[None])]
    lat = list(itertools.chain.from_iterable(lat))
    lon = list(itertools.chain.from_iterable(lon))
    lats.append(lat)
    lons.append(lon)

# Plot with bokeh
df = pd.DataFrame({'x': lats, 'y': lons, 'county': county, 'state': state})
cds = ColumnDataSource(df)
p = figure(width=800)
county_patches = p.patches('x', 'y', source=cds, line_color='white')
hover = HoverTool(renderers=[county_patches], tooltips=[("County, State", "@county, @state")])
p.add_tools(hover)
show(p)