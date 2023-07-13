import configparser


config = configparser.RawConfigParser()
config.read("./configurations/Config.ini") 

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=(config.get("commonInfo", 'baseURL'))
        return url
    @staticmethod
    def getUserEmail():
        email = (config.get("commonInfo", 'email'))
        return email
    @staticmethod
    def getUserPassword():
        password = (config.get("commonInfo", 'password'))
        return password
