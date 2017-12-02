## PyBank 

import os
import csv

#for sustainability, could make directory to sort into files
print("Please ensure your file is within your current working directory.")
inputfile = input("What file would you like to analyze? Please print exact file name ex:'RawData' ")


#auto create output file name
outputfile = inputfile+"_results.txt"

inpath= os.path.join(inputfile+".csv")
outpath= os.path.join(outputfile)

with open (inpath,newline="") as csvfile: 
		csvreader = csv.reader(csvfile, delimiter=',')  
		
		rowcounter = 0
		revenue = 0
		change = 0
		prevmonth = 0 
		increase = 0
		decrease = 0 
		greatestinc = " "
		greatestdec = " "
		next (csvreader) # skip header row

		for row in csvreader:
			# sum revenue
			revenue = float(row[1])+ (revenue)
			
			# total the months
			rowcounter = rowcounter +1
			
			#running average change
			change = (float(row[1])-prevmonth+change)
			
			# find greatest increase
			if float(row[1])-prevmonth > increase:
				increase = float(row[1])-prevmonth
				greatestinc = row[0]
			
			# find greatest decrease
			if float(row[1])-prevmonth < decrease:
				decrease = float(row[1])-prevmonth
				greatestdec = row[0]
			prevmonth = float(row[1])

change=change/rowcounter
print (" ")
print ("Financial Analysis")
print ("----------------------------------------------------")
print ("Total Months: "+str(rowcounter))
print ("Total Revenue: $" + format(revenue, ',.2f'))
print ("Average Revenue Change: $" + format(change, ',.2f'))
print ("Greatest Increase in Revenue: " + greatestinc + "($" + format(increase, ',.2f')+")")
print ("Greatest Decrease in Revenue: " + greatestdec + "($" + format(decrease, ',.2f')+")")

# open/create text file with results
with open(outpath, 'w', newline='') as output:
     txtwriter = csv.writer(output)
 
     txtwriter.writerows([     #remember commas to seperate
		["Financial Analysis"],
		["----------------------------------------------------"],
		["Total Months: "+str(rowcounter)],
		["Total Revenue: $" + format(revenue, ',.2f')],
		["Average Revenue Change: $" + format(change, ',.2f')],
		["Greatest Increase in Revenue: " + greatestinc + "($" + format(increase, ',.2f')+")"],
		["Greatest Decrease in Revenue: " + greatestdec + "($" + format(decrease, ',.2f')+")"]
		])

		