# Import pandas
import pandas as pd
import numpy as np
#from matplotlib import pyplot as plt
import gmplot

def writehtml(Lat,Long,CaseID,Summary,Time):
    myfile = "mymap_withSummary_andtime.html"
    f = open(myfile, 'w')
    f.write("<html>\n")
    f.write("<head>\n")
    f.write('<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />\n')
    f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>\n')
    f.write('<title>Google Maps - pygmaps </title>\n')
    f.write('<script type = "text/javascript" src = "https://maps.googleapis.com/maps/api/js?libraries=visualization&sensor=true_or_false"> </script>\n')
    f.write('<script type = "text/javascript">\n')
    f.write('\tfunction initialize() {\n')
    f.write('\t\tvar centerlatlng = new google.maps.LatLng(18.714410, 73.560990);\n')
    f.write('\t\tvar myOptions = {\n')
    f.write('\t\t\tzoom: 16,\n')
    f.write('\t\t\tcenter: centerlatlng,\n')
    f.write('\t\t\tmapTypeId: google.maps.MapTypeId.ROADMAP\n')
    f.write('\t\t};\n')
    f.write('\t\tvar map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);\n')
    f.write('\n')
    for lat, lng, caseid, summary, time in zip(Lat, Long, CaseID, Summary, Time):
        summary = summary.replace('"',"'")
        f.write('\t\tvar latlng = new google.maps.LatLng(%f, %f);\n' %(lat, lng))
        f.write('\t\tvar marker%s = new google.maps.Marker({\n' %caseid)
        f.write('\t\ttitle: "%s",\n'%caseid)
        f.write('\t\ticon: img,\n')
        f.write('\t\tposition: latlng\n')
        f.write('\t\t});\n')
        f.write('\t\tmarker%s.setMap(map);\n'%caseid)
        f.write('\n')
        f.write('\t\tvar infowindow%s = new google.maps.InfoWindow({\n' %caseid)
        f.write('\t\t\tcontent: "<p><strong>Case ID : %s</strong> <br/><br/><strong>Summary :</strong>%s <br/><br/><strong>Time %s</strong></p>"\n'%(caseid, summary, time))
        f.write('\t\t});\n')
        f.write('\n')
        f.write("\t\tmarker%s.addListener('click', function() {\n"%caseid)
        f.write('\t\t\tinfowindow%s.open(map, marker%s);\n'%(caseid, caseid))
        f.write('\t\t});\n')
        f.write('\n')
    #Dummy code required for javascript to show markers on google maps
    f.write('\t\tvar latlng = new google.maps.LatLng(18.828440, 73.259270);\n')
    f.write("\t\tvar img = new google.maps.MarkerImage('/usr/local/lib/python2.7/dist-packages/gmplot/markers/FF0000.png');\n")
    f.write('\t\tvar marker = new google.maps.Marker({\n')
    f.write('\t\ttitle: "useless sample mark",\n')
    f.write('\t\ticon: img,\n')
    f.write('\t\tposition: latlng\n')
    f.write('\t\t});\n')
    f.write('\t\tmarker.setMap(map);\n')
    f.write('}\n')
    f.write('</script>\n')
    f.write('</head>\n')
    f.write('<body style="margin:0px; padding:0px;" onload="initialize()">\n')
    f.write('\t<div id="map_canvas" style="width: 100%; height: 100%;"></div>\n')
    f.write('</body>\n')
    f.write('</html>\n')
    f.close()



# Assign spreadsheet filename to `file`
file = '/home/shantaram/PycharmProjects/AccidentResearch/Excel Sheets/Accident.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df = xl.parse('Accident')

#filter only rollover accidents
#df1=df.loc[df['RELINTER'] == 4]
df1 = df
#print(df1)
GPSLat= np.array((df1.loc[:]['GPS_LAT']))
GPSLong= np.array((df1.loc[:]['GPS_LONG']))
CaseID = (df1.loc[:]['CASEID'])
Summary = (df1.loc[:]['SUMMARY'])
Time = (df1.loc[:]['Time'])

writehtml(GPSLat,GPSLong,CaseID,Summary,Time)
#print(Timedata)
#print(Timedata_array)
#indexarray = np.array(df1.index.values)
#plt.scatter(indexarray,Timedata_array)
#bins = [0,05,10,15,20,23]
#plt.hist(Timedata_array,bins,histtype='bar',rwidth=0.8)
#plt.show()



