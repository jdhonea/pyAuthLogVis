import yaml

class LogParser:
    def __init__(self):
        self.logDir = self.readLogDirFromConfig()
        print(self.logDir)

    def readLogDirFromConfig(self):
        with open("resources/config.yml", "r") as yamlConfig:
            config = yaml.safe_load(yamlConfig)

        logDir = config['ipinfo']['auth_log_dir']
        yamlConfig.close()
        return logDir

    def getLogDir():
        return self.logDir