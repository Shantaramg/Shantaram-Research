# Import pandas
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def chart(occurance_list):
    hour_list = [t.hour for t in occurance_list]
    print hour_list
    numbers=[x for x in xrange(0,24)]
    labels=map(lambda x: str(x), numbers)
    plt.xticks(numbers, labels)
    plt.xlim(0,24)
    plt.hist(hour_list,rwidth=0.8)
    plt.title("Accident Report Hourly")
    plt.xlabel("Hour of the day")
    plt.ylabel("Number of Accidents")
    plt.yticks(np.arange(0,36,1))
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
Timedata = ((df1.loc[:]['Time']))
Timedata_array = np.array(Timedata)
chart(Timedata_array)
#print(Timedata)
#print(Timedata_array)
#indexarray = np.array(df1.index.values)
#plt.scatter(indexarray,Timedata_array)
#bins = [0,05,10,15,20,23]
#plt.hist(Timedata_array,bins,histtype='bar',rwidth=0.8)
#plt.show()



