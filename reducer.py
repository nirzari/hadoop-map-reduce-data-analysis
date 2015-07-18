#!/usr/bin/env python

from operator import itemgetter
import sys

current_key = None
current_year = None
wspeed = 0.0
temp = 0.0
pressure = 0.0
c = 0
cspring = 0
swspeed = 0.0
stemp = 0.0
spressure = 0.0
csummer = 0
sumwspeed = 0.0
sumtemp = 0.0
sumpressure = 0.0
cfall = 0
fwspeed = 0.0
ftemp = 0.0
fpressure = 0.0
cwinter = 0
wwspeed = 0.0
wtemp = 0.0
wpressure = 0.0
ywspeed = 0.0
ytemp = 0.0
ypressure = 0.0
ycount = 0.0
# input comes from STDIN
for line in sys.stdin:
    try:
	# remove leading and trailing whitespace
	line = line.strip()
	# parse the input we got from mapper.py
	output = line.split('\t')
	key = output[0]	

	if current_key == key:	    
	    wspeed += float(output[3])
	    temp += float(output[4])
            pressure += float(output[5])
            c += 1   
	else:
            if current_key:
		#print current_key
		wspeed = wspeed / c		
		temp = temp / c
		pressure = pressure /c
		# write result to STDOUT 
                print '%s\t%s\t%s\t%s' % (current_key,"windspeed " + str(wspeed),"temp " + str(temp),"pressure " + str(pressure))
		year = current_key[9:13]
		if current_key[16:18] == "1" or current_key[16:18] == "2" or current_key[16:18] == "3":
		    cspring += 1
		    swspeed += wspeed
		    stemp += temp
		    spressure += pressure
		    if cspring == 3:
			swspeed = swspeed / cspring
			stemp = stemp / cspring
			spressure = spressure / cspring
			season = "Spring" + year 
		        print '%s\t%s\t%s\t%s' % (season,"windspeed " + str(swspeed),"temp " + str(stemp),"pressure " + str(spressure))
			cspring = 0
			swspeed = 0
			stemp = 0
			spressure = 0
		elif current_key[16:18] == "4" or current_key[16:18] == "5" or current_key[16:18] == "6":
		    csummer += 1
		    sumwspeed += wspeed
		    sumtemp += temp
		    sumpressure += pressure
		    if csummer == 3:
			sumwspeed = sumwspeed / 3
			sumtemp = sumtemp / 3
			sumpressure = sumpressure / 3 
			season = "Summer" + year		        
			print '%s\t%s\t%s\t%s' % (season,"windspeed " + str(sumwspeed),"temp " + str(sumtemp),"pressure " + str(sumpressure))
			csummer = 0
			sumwspeed = 0
			sumtemp = 0
			sumpressure = 0
		elif current_key[16:18] == "7" or current_key[16:18] == "8" or current_key[16:18] == "9":
		    cfall += 1
		    fwspeed += wspeed
		    ftemp += temp
		    fpressure += pressure
		    if cfall == 3:
		        cfall = 0
			fwspeed = fwspeed / 3
			ftemp = ftemp / 3
			fpressure = fpressure / 3 
			season = "Fall" + year
		        print '%s\t%s\t%s\t%s' % (season,"windspeed " + str(fwspeed),"temp " + str(ftemp),"pressure " + str(fpressure))
			fsummer = 0
			fwspeed = 0
			ftemp = 0
			fpressure = 0
		elif current_key[16:18] == "10" or current_key[16:18] == "11" or current_key[16:18] == "12":
		    cwinter += 1
		    wwspeed += wspeed
		    wtemp += temp
		    wpressure += pressure
		    if cwinter == 3:
			cwinter = 0
			wwspeed = wwspeed / 3
			wtemp = wtemp / 3
			wpressure = wpressure / 3 
			season = "Winter" + year
		        print '%s\t%s\t%s\t%s' % (season,"windspeed " + str(wwspeed),"temp " + str(wtemp),"pressure " + str(wpressure)) 
	    		wsummer = 0
			wwspeed = 0
			wtemp = 0
			wpressure = 0  
	    c = 1
            current_key = key
    	    wspeed = float(output[3])
	    temp = float(output[4])
            pressure = float(output[5])

    	year = current_key[9:13]
	if current_year == year:	    
	    ywspeed += float(output[3])
            ypressure += float(output[5])
	    ytemp += float(output[4])
            cyear += 1   
	else:
    	    if current_year:		
        	# write result to STDOUT
        	ywspeed = ywspeed / cyear
		ytemp = ytemp / cyear
		ypressure = ypressure / cyear 
        	print '%s\t%s\t%s\t%s' % (current_year,"windspeed " + str(ywspeed),"temp " + str(ytemp),"pressure " + str(ypressure))
		print ""
    	    cyear = 1
            current_year = year
    	    ywspeed = float(output[3])
	    ytemp = float(output[4])
	    ypressure = float(output[5])

    except Exception as e:
	print "Eception occured as: " + str(e)
 
# do not forget to output the last word if needed!
if current_key == key:
    wspeed = wspeed / c		
    temp = temp / c
    pressure = pressure /c
    print '%s\t%s\t%s\t%s' % (current_key,"windspeed " + str(wspeed),"temp " + str(temp),"pressure " + str(pressure))
    year = current_key[9:13]
    if current_key[16:18] == "1" or current_key[16:18] == "2" or current_key[16:18] == "3":
	cspring += 1
	swspeed += wspeed
	stemp += temp
	spressure += pressure
	if cspring == 3:
	    swspeed = swspeed / cspring
	    stemp = stemp / cspring
	    spressure = spressure / cspring
	    season = "Spring" + year 
	    print '%s\t%s\t%s\t%s' % (season,"windspeed " + str(swspeed),"temp " + str(stemp),"pressure " + str(spressure))

    elif current_key[16:18] == "4" or current_key[16:18] == "5" or current_key[16:18] == "6":
	csummer += 1
	sumwspeed += wspeed
	sumtemp += temp
	sumpressure += pressure
	if csummer == 3:
	    sumwspeed = sumwspeed / 3
	    sumtemp = sumtemp / 3
	    sumpressure = sumpressure / 3 
	    season = "Summer" + year		        
	    print '%s\t%s\t%s\t%s' % (season,"windspeed " + str(sumwspeed),"temp " + str(sumtemp),"pressure " + str(sumpressure))

    elif current_key[16:18] == "7" or current_key[16:18] == "8" or current_key[16:18] == "9":
	cfall += 1
	fwspeed += wspeed
	ftemp += temp
	fpressure += pressure
	if cfall == 3:
	    cfall = 0
	    fwspeed = fwspeed / 3
	    ftemp = ftemp / 3
	    fpressure = fpressure / 3 
	    season = "Fall" + year
	    print '%s\t%s\t%s\t%s' % (season,"windspeed " + str(fwspeed),"temp " + str(ftemp),"pressure " + str(fpressure))
    elif current_key[16:18] == "10" or current_key[16:18] == "11" or current_key[16:18] == "12":
        cwinter += 1
	wwspeed += wspeed
	wtemp += temp
	wpressure += pressure
	if cwinter == 3:
	    cwinter = 0
	    wwspeed = wwspeed / 3
	    wtemp = wtemp / 3
	    wpressure = wpressure / 3 
	    season = "Winter" + year
	    print '%s\t%s\t%s\t%s' % (season,"windspeed " + str(wwspeed),"temp " + str(wtemp),"pressure " + str(wpressure)) 

if current_year == year:	    
    ywspeed = ywspeed / cyear
    ytemp = ytemp / cyear
    ypressure = ypressure / cyear 
    print '%s\t%s\t%s\t%s' % (current_year,"windspeed " + str(ywspeed),"temp " + str(ytemp),"pressure " + str(ypressure))  
#end_all
