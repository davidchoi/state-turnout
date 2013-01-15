from numpy import genfromtxt, where
from numpy.random import rand
import matplotlib.pyplot as plt
import matplotlib.colors as colors

#read csv file using numpy.genfromtxt
rawdata = genfromtxt('turnout.csv', delimiter=',', 
			names = ['year','state_code', 'alphanum_code', 'state_name', 
					 'VEP_turnout', 'VEP_totalballots', 'VAP_turnout', 
					 'VAP', 'PCT_noncitizen', 'prison', 'probation', 'parole', 
					 'ineligible', 'overseas', 'VEP', 'high_turnout', 
				 	 'total_turnout'],
			dtype = None)
		
#note to self: rawdata is now a _structured_ ndarray.

#years of interest
years = [2012, 2008, 2004, 2000, 1996, 1992, 1988, 1984, 1980]
#note: this array is arranged in descending order due to the plotting, i think..
		 
#state postal abbreviations
state_abbrev = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 
				'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME',
				'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 
				'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI',
				'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI',
				'WY']
				
fig = plt.figure(figsize=(11,14))
ax = fig.add_subplot(111)
ax.set_xlabel('Year')
ax.set_ylabel('Percent Turnout')
ax.set_xticks([1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012])
ax.set_xlim(1979, 2013)
ax.set_ylim(35, 80)
ax.set_title('Voter Turnout, 1980-2012')

#plot national average
loc = where((rawdata['year'] % 4 == 0) & (rawdata['alphanum_code'] == 0))
ax.plot(years, 100.*rawdata[loc]['VEP_turnout'], lw=1.5)

for j in range(9):
	ax.annotate('USA', xy=(years[j]-0.7, 
		100.*rawdata[loc]['VEP_turnout'][j]-0.25), color='red')

for i in range(1,52):

	r = rand()
	g = rand()
	b = rand()
	c = (r,g,b)

#determine indices for every presidential election for each state
	loc = where((rawdata['year'] % 4 == 0) & (rawdata['alphanum_code'] == i))

#plot line at 25% gray, 0.5 linewidth
	ax.plot(years, 100.*rawdata[loc]['VEP_turnout'], '0.25', lw=0.25)

#not sure if scatter will work when state abbreviation string is desired marker	
	#ax.scatter(map(int,years[1:]), 
	#		   100.*rawdata[loc]['VEP_turnout'][1:],
	#		   s=2, marker=)
	
	
	
#text annotations
	for j in range(9):
		ax.annotate(state_abbrev[i-1], xy=(years[j]-0.4, 
			100.*rawdata[loc]['VEP_turnout'][j]-0.25), color=c)

fig.show()

#loc = where(rawdata['year'] == 1980)
#data[loc]['VEP_turnout']		
#loc = where(rawdata['year'] % 4 == 0)

#what I'd like to do
#have line colored in the purple shade corresponding to red/blue split of state
#would likely have to be static (fixed at most recent election), but
#perhaps could evolve with time?

		
#need to download basemap for map visualization