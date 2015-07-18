#!/usr/bin/env python

import sys

# initialize counter
c = 0
# input comes from STDIN (standard input)
for line in sys.stdin:
    try:
	# remove leading and trailing whitespace
	line = line.strip()
	# extract station id from data
	sid = line[4:10]
	# extract year from data
	yr = line[15:19]
	# extract month from data
    	month = int(line[19:21])
	# extract date from data
    	date = int(line[21:23])
	# extract hour from data
    	hour = int(line[23:25])
	# extract wind speed from data
    	ws1 = line[65:69]
	# if corrupted wind speed value, then skip the line
    	if ws1 == "9999":
            continue
	# apply scaling factor of 10 on wind speed
    	wspeed = str(float(ws1) / 10)
	# extract temperature from data
    	t1 = line[87:92]
	# if corrupted temperature value, then skip the line
    	if t1 == "+9999":
            continue
	# apply scaling factor of 10 on temperature
    	temp = str(float(t1) / 10 ) 
	# extract temperature from data
    	p1 = line[99:104]
	# if corrupted pressure value, then skip the line
    	if p1 == "99999":
            continue
	# apply scaling factor of 10 on pressure
        pressure = str(float(p1) / 10 )
    	c += 1
	#key = sid + str(yr) + str(month)
    	# write the results to STDOUT (standard output);
    	# what we output here will be the input for the reduce step, i.e. the input for reducer.py
	key = sid + ".|." + str(yr) + ".|." + str(month)
    	print '%s\t%s\t%s\t%s\t%s\t%s' % (key,str(date),str(hour),wspeed,temp,pressure)

    except Exception as e:
	print "Exception occured: " + str(e)

# end all 
