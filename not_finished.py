"""
Have multiple environments and need to pass in a config file based on the environment?

Use this, so you don't pass the wrong config.

Use:

#!/usr/bin/python
import enviro_check
class Main:
    def __init__(self, configFile):
        pass
 
    def process(self):
        print "ok"
 
if __name__ == "__main__":
    m = Main(entryscript.CONFIGFILE)
    m.process()

"""



#!/usr/bin/python
import os
import sys
ENVIRONMENT = "development"
CONFIGFILE = None
 
def getConfigFileForEnv():
    directory = os.path.dirname(__file__)
    return {
        "development" : "%s/../config/development.cfg" % directory,
        "staging" : "%s/../config/staging.cfg" % directory,
        "production" : "%s/../config/production.cfg" % directory
    }.get(ENVIRONMENT, None)
 
CONFIGFILE = getConfigFileForEnv()
if CONFIGFILE is None:
    sys.exit("Configuration error! Unknown environment set. \
              Edit configurations.py and set appropriate environment")
print "CONFIGFILE : %s" % CONFIGFILE
if not os.path.exists(CONFIGFILE):
    sys.exit("Configuration error! Config file does not exist")
print "configurations ok ......"
