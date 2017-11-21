# Import pandas
import pandas as pd
import numpy as np
#from matplotlib import pyplot as plt
import gmplot

def chart(Lat,Long,Summary):
    #plt.scatter(Lat,Long,marker="x")
    #x = Lat
    #plt.xticks(np.arange(min(x),19,0.01))
    #plt.xlabel("Latitude")
    #plt.ylabel("Longtitude")
    #plt.title("Location Report on Accidents")
    #plt.show()
    gmap = gmplot.GoogleMapPlotter(18.71441,73.56099, 16)
    #gmap.heatmap(Lat,Long)
    #gmap.scatter(Lat,Long,'k',marker=True)
    #caseid=[]
    for lat, lng, summary in zip(Lat, Long, Summary):
        gmap.marker(lat, lng, title=summary)
        caseid=[]
    gmap.draw("mymap.html")

# Assign spreadsheet filename to `file`
file = '/home/shantaram/PycharmProjects/AccidentResearch/Excel Sheets/Accident.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df = xl.parse('Accident')

#filter only rollover accidents
#df1=df.loc[df['FIRSTCRA'] == 9]
df1 = df
#print(df1)
GPSLat= np.array((df1.loc[:]['GPS_LAT']))
GPSLong= np.array((df1.loc[:]['GPS_LONG']))
caseidlist = ["Case ID"]*len(df)
Summary = (df1.loc[:]['CASEID'])

chart(GPSLat,GPSLong,Summary)
#print(Timedata)
#print(Timedata_array)
#indexarray = np.array(df1.index.values)
#plt.scatter(indexarray,Timedata_array)
#bins = [0,05,10,15,20,23]
#plt.hist(Timedata_array,bins,histtype='bar',rwidth=0.8)
#plt.show()



