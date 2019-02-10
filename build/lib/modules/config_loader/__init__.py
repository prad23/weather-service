import configparser, errors, sys, os
from utils.files import get_full_path

class ConfigurationLoader(object):
    def __init__(self, configsection=None, configname=None):
        self.configsection = configsection
        self.configname = configname

    def get_configsection(self):
        return self.configsection

    def set_configsection(self, configsection):
        self.configsection = configsection

    def get_configname(self):
        return self.configname

    def set_configname(self, configname):
        self.configname = configname

    def getconfig(self):
        try:
            config = configparser.ConfigParser()
            curdir = get_full_path("config","api.properties")
            if(os.path.isfile(curdir)):
#                print(curdir)
                config.read(curdir)
            else:
                raise errors.Error("Error loading configuration file: %s", get_full_path("config","api.properties"))
            if config.has_section (self.configsection):
                return config[self.configsection]
            else:
                print("There is either no %s or %s in config file." % (self.configsection, self.configname))
        except RuntimeError as err:
            print("Error reading configurations file: %s" % err)
