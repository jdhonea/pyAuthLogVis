import ipinfo
import yaml

class IpinfoHandler:
    def __init__(self):
        self.access_token = self.readAccessToken()
        self.handler = ipinfo.getHandler(self.access_token)
        print(self.access_token)

    def readIP(self, ip):
        if self.handler is not null:
            self.details = self.handler.getDetails(ip)

    def getDetails(self):
        if self.details is not null:
            return self.details
    
    def getCountry(self):
        if self.details is not null:
            return self.details.country_name

    def readAccessToken(self):
        with open("resources/config.yml", "r") as yamlConfig:
            config = yaml.safe_load(yamlConfig)
    
        authToken = config['ipinfo']['access_token']
        yamlConfig.close()
        return authToken