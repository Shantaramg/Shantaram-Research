# Import pandas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def chart(occurance_list):
    #hour_list = [t.hour for t in occurance_list]
    #print hour_list
    #numbers=[x for x in xrange(0,24)]
    #labels=map(lambda x: str(x), numbers)
    #plt.xticks(numbers, labels)
    #plt.xlim(0,24)
    bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5]
    plt.hist(occurance_list,bins,rwidth=0.8)
    #locs,labels = plt.xticks()
    #plt.xticks(arange(12))
    x=np.array(range(0,11,1))
    #y = np.array(range(0, 26, 1))
    plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
    #plt.yticks(np.arange(min(y), max(y) + 1, 1.0))
    plt.xlabel("Kind of Accident\n"
               "01 - Collision with another vehicle which starts, stops or is stationary\n"
               "02 - Collision with another vehicle moving ahead or waiting\n"
               "03 - Collision with another vehicle moving laterally in the same direction\n"
               "04 - Collision with another oncoming vehicle\n"
               "05 - Collision with another vehicle which turns into or crosses a road\n"
               "06 - Collision between vehicle and pedestrian\n"
               "07 - Collision with an obstacle in the carriageway\n"
               "08 - Leaving the carriageway to the right\n"
               "09 - Leaving the carriageway to the left\n"
               "10 - Accident of another kind")
    plt.ylabel("Number of Accidents")
    plt.title("Accident kind Report on number of Accidents")
    plt.tight_layout()
    plt.show()

# Assign spreadsheet filename to `file`
file = '/home/shantaram/PycharmProjects/AccidentResearch/Excel Sheets/Accident.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Accident')

#print(df1)
Timedata = ((df1.loc[:]['ACCKIND']))
Timedata_array = np.array(Timedata)
chart(Timedata_array)
#print(Timedata)
#print(Timedata_array)
#indexarray = np.array(df1.index.values)
#plt.scatter(indexarray,Timedata_array)
#bins = [0,05,10,15,20,23]
#plt.hist(Timedata_array,bins,histtype='bar',rwidth=0.8)
#plt.show()



