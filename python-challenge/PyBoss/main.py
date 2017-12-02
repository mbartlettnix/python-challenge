# The Name column should be split into separate First Name and Last Name columns.
# The DOB data should be re-written into DD/MM/YYYY format.
# The SSN data should be re-written such that the first five numbers are hidden from view.
# The State data should be re-written as simple two-letter abbreviations.
# PyBoss

import os
import csv
import datetime #library for date/time formatting
import us #library for US state naming

inputfile = 'employee_data2'
outputfile = inputfile+'results.csv'

inpath= os.path.join(inputfile+'.csv')
outpath= os.path.join(outputfile)

employeeid =[]
firstname =[]
lastname = []
dobedit = []
ssnedit = []
state = []

with open (inpath,newline='') as csvfile: 
    csvreader = csv.reader(csvfile)  

    next (csvreader) # skip header row
    
    for row in csvreader:
        
        #gather employee ID
        employeeid.append(row[0])
        
        #gather name in split
        splitname = (row[1].split())
        firstname.append(splitname[0])
        lastname.append(splitname[1])
        
        #gather DOB in corrected format
        dobedit.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%-m/%d/%y'))
        #split ssn and replace
        ssn = (row[3]).split('-')
        ssnedit.append("###-##-"+ssn[2])
        # look up state abbr
        state.append(us.states.lookup(row[4]).abbr)
        
cleanheader = [('Emp ID','First Name','Last Name','DOB','SSN','State')]
cleanedData= zip(employeeid, firstname, lastname, dobedit, ssnedit, state)


with open(outpath, mode='w', newline='') as output:
    writer = csv.writer(output)

    writer.writerows(cleanheader)
    writer.writerows(cleanedData)