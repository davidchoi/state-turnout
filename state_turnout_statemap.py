#state_turnout_statemap.py

from numpy import genfromtxt, where
from numpy.random import rand
from mpl_toolkits.basemap import Basemap
from math import sqrt
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.colors import rgb2hex

from numpy import array, linspace

#read csv file using numpy.genfromtxt
rawdata = genfromtxt('turnout.csv', delimiter=',', 
			names = ['year','state_code', 'alphanum_code', 'state_name', 
					 'VEP_turnout', 'VEP_totalballots', 'VAP_turnout', 
					 'VAP', 'PCT_noncitizen', 'prison', 'probation', 'parole', 
					 'ineligible', 'overseas', 'VEP', 'high_turnout', 
				 	 'total_turnout'],
			dtype = None, filling_values = 0)
		
#note to self: rawdata is now a _structured_ ndarray.

#years of interest
years = [2012, 2008, 2004, 2000, 1996,
		 1992, 1988, 1984, 1980]
		 
#state postal abbreviations
state_abbrev = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 
				'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME',
				'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 
				'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI',
				'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI',
				'WY']
				
#Some code is based on
#http://matplotlib.org/basemap/users/examples.html
#http://stackoverflow.com/questions/7586384/color-states-with-pythons-matplotlib-basemap
#http://osdir.com/ml/python.matplotlib.general/2005-10/msg00029.html
				
fig = plt.figure(figsize=(11,8.5))

# Lambert Conformal map of lower 48 states.	
m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

shp_info = m.readshapefile('usa_state_shapefile', 'states', drawbounds=True)

# choose a color for each state based on turnout percentage.
#define dictionary of colors and statenames
colors={}
statenames=[]

#define color map for figure
cmap = cm.Purples

#ranges for the voter turnout
tmin = 40
tmax = 80

#desired year
yr = 2012

#the call to readshapefile creates an attribute of m called states_info that
#contains data about the shape lines/vectors
#m.states_info is a list
for shapedict in m.states_info:
	
	#extract statename from the states_info dict
	statename = shapedict['STATE_NAME']
	
	#determine location of year+statename in rawdata
	loc = where((rawdata['year'] == yr) & (rawdata['state_name'] == statename))
	#extract turnout data
	turnout = (rawdata[loc]['VEP_turnout'])*100.

	#map turnout into the appropriate color
	
#####
#Q to address: why does cmap require re-scaling between 0 to 1?
#anyway to rescale?

#flatten array, and only take first 3 elements (to pass to rgb2hex later)	
	colors[statename] = cmap((turnout-tmin)/(tmax-tmin)).flat[:3]
	
	#append statename to the statenames list
	statenames.append(statename)

		
for nshape, seg in enumerate(m.states):

#is rgb2hex really needed here?
	xx, yy = zip(*seg)	
	color = rgb2hex(colors[statenames[nshape]])
	plt.fill(xx, yy, color, edgecolor=color)
	
#fake contour data for setting up colorbar
data = array([[40,80],[40,80]])
clevs = linspace(40,80,200)
contours = m.contourf([0,1],[0,1],data, clevs, cmap = cmap)
cbar = m.colorbar(contours, location = 'bottom', 
				  ticks = [40,45,50,55,60,65,70,75,80])
cbar.set_label('Percent')

plt.title('Voter Turnout, ' + '{0}'.format(yr)) 
#plt.title('{0}'.format(yr))
#fig.show()
fig.savefig('{0}'.format(yr)+'.png')

#NEXT STEPS:
#How to show alaska and hawaii
