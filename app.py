import sys
sys.path.append('./modules')
import httpclient, logging, errors, operator as op, json, config_loader
from flask import Flask, request

Format = '%(asctime)-15s:%(name)s:%(levelname)s--> %(message)s'
logging.basicConfig (format=Format, filename="weather-service.log", level="INFO", filemode="a")
log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/weather',methods=['GET','POST'])
def main():
    """
    Gets weather response for given location.

    Response returned is full json body. 
    """
    try:
        loop_var = request.args.getlist('city')
        log.info("Number of arguments in Weather service: %s" % len(loop_var))
        response_body = []
        for city in loop_var:
            log.info("Weather service is being invoked")
            configLoader = config_loader.ConfigurationLoader()
            configLoader.set_configsection('Weather_API')
            weather = configLoader.getconfig()
            log.info("Get weather for location %s" % (city))
            weather_url = weather['weather.host']+weather['weather.resource']+"/"+str(city)
            log.info("Weather url for current location is: %s " % weather_url)
            client = httpclient.HttpClient()
            client.set_url(weather_url)
            queryString = {"apikey": weather['weather.token'],"details":"false"}
            client.set_params(queryString)
            log.info("Weather url after construction %s,%s " %(client.get_url(),client.get_params()))
            w_resp=client.get_request()
            log.info("Weather response: %s" %w_resp)
            response_body.append(w_resp)
        return_response = app.response_class(
            response=json.dumps(response_body),
            status = 200,
            mimetype = 'application/json'
            )
        return return_response
    except errors.Error as err:
        log.error("Distance response could not be retrieved: %s" % err)

    
if __name__=="__main__":
    app.run(host='0.0.0.0',port=50003)