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
    bins=[10.5,11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5,19.5,20.5]
    plt.hist(occurance_list,bins,rwidth=0.8)
    #locs,labels = plt.xticks()
    #plt.xticks(arange(12))
    x=np.array(range(10,21,1))
    #y = np.array(range(0, 26, 1))
    plt.xticks(np.arange(min(x), max(x) + 1, 1.0))
    #plt.yticks(np.arange(min(y), max(y) + 1, 1.0))
    plt.xlabel("Weather \n"
               "11:FogSmogSmoke\n"
               "12:rain\n"
               "13:SleetHail\n"
               "14:Snow\n"
               "15:BlowingSnow\n"
               "16:SevereCrosswinds\n"
               "17:BlowingSandSoilDirt\n"
               "18:Clear\n"
               "19:Coudy")
    plt.ylabel("Number of Accidents")
    plt.title("First Crash Report on number of Accidents")
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
Timedata = ((df1.loc[:]['WEATHER']))
Timedata_array = np.array(Timedata)
chart(Timedata_array)
#print(Timedata)
#print(Timedata_array)
#indexarray = np.array(df1.index.values)
#plt.scatter(indexarray,Timedata_array)
#bins = [0,05,10,15,20,23]
#plt.hist(Timedata_array,bins,histtype='bar',rwidth=0.8)
#plt.show()



