import ipinfo
import yaml

class IpinfoHandler:
    def __init__(self):
        self.access_token = self.readAccessToken()
        self.handler = ipinfo.getHandler(self.access_token)

    def readIP(self, ip):
        if self.handler != None:
            self.details = self.handler.getDetails(ip)

    def getDetails(self):
        if self.details != None:
            return self.details
    
    def getCountryName(self):
        if self.details != None:
            return self.details.country_name

    def getCountryCode(self):
        if self.details != None and self.details.country_name != None:
            return self.details.country
        else:
            return None

    def readAccessToken(self):
        with open("resources/config.yml", "r") as yamlConfig:
            config = yaml.safe_load(yamlConfig)
    
        authToken = config['ipinfo']['access_token']
        yamlConfig.close()
        return authToken