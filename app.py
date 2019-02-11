import sys
sys.path.append('./modules')
import httpclient, logging, errors, operator as op, json, config_loader
from flask import Flask

Format = '%(asctime)-15s:%(name)s:%(levelname)s--> %(message)s'
logging.basicConfig (format=Format, filename="weather-service.log", level="INFO", filemode="a")
log = logging.getLogger(__name__)
app = Flask(__name__)

def _weather_url(weather,city,state):
    return weather['weather.host']+weather['weather.token']+weather['weather.query']+"/"+state+"/"+city+".json"    

@app.route('/')
def index():
    return 'Index Page'

@app.route('/weather/<string:city>/<string:state>',methods=['GET'])
def main(city,state):
    """
    Gets weather response for given location.

    Response returned is full json body. 
    """
    try:
        log.info("Weather service is being invoked.")
        log.info("Getting weather for %s,%s" %(city,state) )
        configLoader = config_loader.ConfigurationLoader()
        configLoader.set_configsection('Weather_API')
        weather = configLoader.getconfig()
        log.info("Get weather for location %s,%s " % (city,state))
        weather_url = _weather_url(weather,city,state)
        log.info("Weather url for current location is: %s " % weather_url)
        client = httpclient.HttpClient()
        client.set_url(weather_url)
        w_resp=client.get_request()
        log.info("Weather response: %s" %w_resp)
        return json.dumps(w_resp)
    except errors.Error as err:
        log.error("Distance response could not be retrieved: %s" % err)

    
if __name__=="__main__":
    app.run(host='0.0.0.0',port=50003)