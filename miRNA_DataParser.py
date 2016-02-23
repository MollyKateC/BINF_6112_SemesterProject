#! usr/bin/python


import os
import re



##Get GSM codes from filenames, store in a list

filenames = []

for path, subdirs, files in os.walk(r'/Users/mcrowder25/School_S16/ProgrammingII/SemesterProject/CodeTesting/Test_Dir'):
	for filename in files:
		f =(os.path.join(path, filename))
		filenames.append(f)

#filenames = tuple(filenames)

code_list = []

for word in filenames:
    codematch = re.search('Test_Dir/(GSM.......)_', word)
    if codematch:
        code = codematch.group(1)
        code_list.append(code)


## Parse Data Files

#If StopIteration Error occurs, delete the file .DS_Store and rerun


row_list = []                                                   
separated_row_list = []

for filename in os.listdir('/Users/mcrowder25/School_S16/ProgrammingII/SemesterProject/CodeTesting/Test_Dir'):
    with open(filename) as current_file:
        for file in current_file:
            print(current_file)
            for line in xrange(8):
                next(current_file)
            for line in current_file:
                var1 = line
                row_list.append(var1)



for i in row_list:
    separated_row_list.append(i.split('\t')[:])

for i in separated_row_list:
    col5 = ['G_NAME'] + [row[4] for row in separated_row_list]
    col6 = ['G_ID'] + [row[5] for row in separated_row_list]
    col7 = ['Spot_Median'] + [row[6] for row in separated_row_list]
    col8 = ['BG_Median'] + [row[8] for row in separated_row_list]

DataMatrix = [col5, col6, col7, col8]

#print(DataMatrix)

print(DataMatrix[3])


##WORKED 02.18.2016     14:36

## TO DO:

    ## Fix hidden files bug
	## Need to figure out how to associate GSM code with appropriate data lines
	## GSM code will be repeated through every line from the same file


quit()