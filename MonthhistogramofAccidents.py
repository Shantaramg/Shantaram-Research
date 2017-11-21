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
    bins=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5]
    plt.hist(occurance_list,bins,rwidth=0.8)
    #locs,labels = plt.xticks()
    #plt.xticks(arange(12))
    x=np.array(range(0,13,1))
    y = np.array(range(0, 26, 1))
    plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
    plt.yticks(np.arange(min(y), max(y) + 1, 1.0))
    plt.xlabel("Month of the Year")
    plt.ylabel("Number of Accidents")
    plt.title("Monthly Report on number of Accidents")
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
Timedata = ((df1.loc[:]['Month']))
Timedata_array = np.array(Timedata)
chart(Timedata_array)
#print(Timedata)
#print(Timedata_array)
#indexarray = np.array(df1.index.values)
#plt.scatter(indexarray,Timedata_array)
#bins = [0,05,10,15,20,23]
#plt.hist(Timedata_array,bins,histtype='bar',rwidth=0.8)
#plt.show()



