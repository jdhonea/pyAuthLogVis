import yaml

def readAccessToken():
    with open("resources/config.yml", "r") as yamlConfig:
        config = yaml.safe_load(yamlConfig)
    
    authToken = config['ipinfo']['access_token']
    yamlConfig.close()
    return authToken

def readLogDir():
    with open("resources/config.yml", "r") as yamlConfig:
        config = yaml.safe_load(yamlConfig)

    logDir = config['ipinfo']['auth_log_dir']
    yamlConfig.close()
    return logDir

if __name__ == "__main__":
    access_token = readAccessToken()
    log_dir = readLogDir()
    
    