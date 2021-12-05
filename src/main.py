from IpinfoHelper import IpinfoHandler
from LogParser import LogParser

if __name__ == "__main__":
    logs = LogParser()
    iphandler = IpinfoHandler()

    ips = logs.getIPsParsed()
    countryList = []
    for ip in ips:
        iphandler.readIP(ip)
        countryList.append(iphandler.getCountry())

    countryCount = {}
    for country in countryList:
        if country in countryCount:
            countryCount[country] = countryCount.get(country) + 1
        else:
            countryCount[country] = 1

    print(countryCount)
    
   