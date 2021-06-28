import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
def CtoF(x):
    return x*1.8+32

def FtoC(x):
    return (x-32)/1.8

filename="data/sitka_weather_2018_simple.csv"
#filename="data/death_valley_2018_full.csv"
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    print(header_row)
    #get col indexes
    col_indexes={}
    for index,col_name in enumerate(header_row):
        col_indexes[col_name]=index
    #print(col_indexes)

    #get high temp from file
    highs=[]
    high_index=col_indexes["TMAX"]
    dates=[]
    date_index = col_indexes["DATE"]
    lows=[]
    low_index = col_indexes["TMIN"]
    precipitations=[]
    prcp_index=col_indexes["PRCP"]
    figure_title=""
    station_index=col_indexes["STATION"]
    station_name_index=col_indexes["NAME"]
    for index,row in enumerate(reader):
        if not figure_title:
            figure_title="Station " + row[station_index]+" - "+row[station_name_index]
        current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
        try:
            high=int(row[high_index])
            low = int(row[low_index])
            prcp=float(row[prcp_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)
            precipitations.append((prcp))

plt.style.use("seaborn")
fig,ax=plt.subplots(ncols=2,figsize=(11,6))


#set first subplot
ax[0].plot(dates,highs,c="red",linestyle="-",linewidth=1)
ax[0].plot(dates,lows,c="blue",linestyle="-",linewidth=1)
secondary_yaxis=ax[0].secondary_yaxis("right",functions=(FtoC,CtoF))
secondary_yaxis.set_ylabel("Temperature (C)")
secondary_yaxis.tick_params(axis="y",which="major", color="black",width=1,length=6)
ax[0].set_xlabel("Date",fontsize=16)
ax[0].set_ylabel("Temperature (F)", fontsize=16)
ax[0].fill_between(x=dates,y1=lows,y2=highs,facecolor="blue",alpha=0.3)
ax[0].tick_params(axis="both",which="major", color="black",width=1,length=6,labelsize=8)
ax[0].set_title("Daily temperatures",fontsize=16)

#set second subplot
ax[1].scatter(dates,precipitations,c=precipitations,cmap=plt.get_cmap("Blues"))
ax[1].set_xlabel("Date",fontsize=16)
ax[1].set_ylabel("1mm/m\u00b2")
ax[1].tick_params(axis="both",which="major", color="black",width=1,length=6,labelsize=8)
ax[1].set_title("Daily precipitation",fontsize=16)

#format plot
plt.subplots_adjust(wspace=0.4) #daje odstep miedzy subplotami
fig.autofmt_xdate() #formatuje x we wszystkich subplotach jako date
fig.suptitle(figure_title,fontsize=18)

#plt.tick_params(axis="both",which="major", labelsize=8)
#plt.tick_params(axis="both",which="major", color="black",width=1,length=6)
plt.show()

