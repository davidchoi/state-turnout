#state_turnout.py

from numpy import genfromtxt, where
import matplotlib.pyplot as plt

#read csv file using numpy.genfromtxt
rawdata = genfromtxt('turnout2.csv', delimiter=',', 
			names = ['year','state_code', 'alphanum_code', 'state_name', 
					 'VEP_turnout', 'VEP_totalballots', 'VAP_turnout', 
					 'VAP', 'PCT_noncitizen', 'prison', 'probation', 'parole', 
					 'ineligible', 'overseas', 'VEP', 'high_turnout', 
				 	 'total_turnout', 'demvotes', 'repvotes', 'drdiff'],
			dtype = None)
		
#note to self: rawdata is now a _structured_ ndarray.

#filter out presidential election years
preselec = where(rawdata['year'] % 4 == 0)

#parse out Dem/Rep difference
x = rawdata[preselec]['drdiff']

y = 100.*rawdata[preselec]['VEP_turnout']

# 				
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('D/R Split (0 = Democratic, 1 = Republican)')
ax.set_ylabel('Percent Turnout')
ax.set_title('Dem/Rep Split vs. Turnout')
ax.set_ylim(30, 90)
ax.set_xlim(0.0, 1.0)
plt.scatter(x,y)

fig.show()
fig.savefig('demrepsplit_vs_turnout.png')