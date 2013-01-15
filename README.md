State Turnout Project
=========

Abstract
--------

What state has the best voter turnout percentage? This collection of python code aims to answer that.

Description
-----------

Simple code for reading in data from the [United States Elections Project](http://elections.gmu.edu/voter_turnout.htm), and visualizing it.

Methodology
-----------

For this project, I am only concerned with Presidential election years. I use the "VEP Highest Office Turnout Rate" (VEP: Voting-Eligible Population), as this is the recommended statistic.

I converted [this spreadsheet](http://elections.gmu.edu/Turnout%201980-2012.xls) into csv. Note: Before conversion, I modified spreadsheet cells by removing comma thousands separators, converting percentages into decimals, and removing header rows.

I then wrote various scripts to parse the data, and visualize it as maps or line graphs.

Notes
-----

Shapefile is from [geocommons.com](http://geocommons.com/overlays/21424).

Related reading: <http://www.csmonitor.com/USA/Elections/2012/1106/Voter-turnout-the-6-states-that-rank-highest-and-why/Oregon>

Copyright: David S. Choi, 2013

Comments and suggestions for improvement are welcome! 
I'd love to hear from you.
Contact: david@davidchoi.org

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>