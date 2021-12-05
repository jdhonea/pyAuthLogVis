import yaml
import os
import re
from os.path import isfile, join

class LogParser:
    ips = []

    def __init__(self):
        self.logDir = self.readLogDirFromConfig()
        self.authLogs = self.listAuthLogs()
        self.parseLogs()
    
    def getLogDir(self):
        return self.logDir

    def getIPsParsed(self):
        return self.ips

    def readLogDirFromConfig(self):
        with open("resources/config.yml", "r") as yamlConfig:
            config = yaml.safe_load(yamlConfig)

        logDir = config['ipinfo']['auth_log_dir']
        yamlConfig.close()
        return logDir

    def listAuthLogs(self):
        files = os.listdir(self.logDir)
        authLogs = []
        for file in files:
            if re.match(r'^auth\.log\.*[0-9]*$', file):
                authLogs.append(file)
            elif re.match(r'^fail2ban\.log\.*[0-9]*$', file):
                authLogs.append(file)
        return authLogs

    def readLog(self, log):
        lines = []
        if (isfile(join(self.logDir, log))):
                with open(join(self.logDir, log), "r") as file:
                    lines = file.readlines()
                file.close()
        return lines

    def parseLogs(self):
        for log in self.authLogs:
            lines = self.readLog(log)
            for line in lines:
                ipParsed = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
                for ip in ipParsed:
                    if ip not in self.ips:
                        self.ips.append(ip)
            
    
