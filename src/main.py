import pygal
from IpinfoHelper import IpinfoHandler
from LogParser import LogParser

if __name__ == "__main__":
    logs = LogParser()
    iphandler = IpinfoHandler()

    ips = logs.getIPsParsed()
    countryList = []
    for ip in ips:
        iphandler.readIP(ip)
        code = iphandler.getCountryCode()
        if code != None:    
            countryList.append(code.lower())

    countryCount = {}
    for country in countryList:
        if country in countryCount:
            countryCount[country] = countryCount.get(country) + 1
        else:
            countryCount[country] = 1

    print(countryCount)
    
    map = pygal.maps.world.World()
    map.title = "Log Hits by Country"
    map.add('Data', countryCount)
    map.render_to_file('DataVisualization.svg')
    print('Done!')
  