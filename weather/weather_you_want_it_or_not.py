import datetime
import requests

from bs4 import BeautifulSoup

def main():
    STP_LAT = "44.9344"
    STP_LONG = "-93.1127"

    url = "http://graphical.weather.gov/xml/SOAP_server/ndfdXMLclient.php"
    params = {"whichClient" : "NDFDgen", "lat" : STP_LAT, "lon" : STP_LONG, "product" : "glance", "begin" : "", "end" : ""}

    soup = BeautifulSoup(requests.get(url, params=params).text, "xml")

    xmlblock = soup.find_all('start-valid-time')[:7]

    daylist = list()

    for line in xmlblock:
        daylist.append(Day(line['period-name']))

    xmlblock = soup.find_all('temperature')
    maxtemps = xmlblock[0].children
    mintemps = xmlblock[1].children

    i = 0
    for tmax in maxtemps:
        if tmax != '\n' and len(tmax.string) <= 3:
            if i < len(daylist):
                daylist[i].setTmax(tmax.string)
                i += 1

    if i < len(daylist):
        for j in range(i, len(daylist)):
            daylist[i].setTmax("N/A")

    i = 0
    for tmin in mintemps:
        if tmin != '\n' and len(tmin.string) <= 3:
            if i < len(daylist):
                daylist[i].setTmin(tmin.string)
                i += 1

    if i < len(daylist):
        for j in range(i, len(daylist)):
            daylist[i].setTmin("N/A")

    for day in daylist:
        print(day.name + ": " + "max temp is " + str(day.tmax) + " min temp is " + str(day.tmin))

class Day:
    def __init__(self, name):
        self.name = name

    tmax = 0
    tmin = 0

    def setTmax(self, tmax):
        self.tmax = tmax

    def setTmin(self, tmin):
        self.tmin = tmin

main()