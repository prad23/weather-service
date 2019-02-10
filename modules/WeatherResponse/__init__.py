class WeatherResponse(object):
    """
        Class to build weather response mapping.

        params: city(str), state(str), temperature_f(num), temperature_string(str), wind(num), feels_like_string(str)
                precp_today(str), icon_url(str), forecast_url(str)
    """
    def __init__(self,city=None,state=None,temperature_f=None,temperature_string=None,wind=None,feels_like_string=None,precp_today=None,icon_url=None,forecast_url=None):
        self.city=city
        self.state=state
        self.temperature_f=temperature_f
        self.temperature_string=temperature_string
        self.wind=wind
        self.feels_like_string=feels_like_string
        self.precp_today=precp_today
        self.icon_url=icon_url
        self.forecast_url=forecast_url 

    @property
    def _city(self):
        return self.city
    @_city.setter
    def _city(self,city):
        self.city=city

    @property
    def _state(self):
        return self.state
    @_state.setter
    def _state(self,state):
        self.state=state

    @property
    def _temperature_f(self):
        return self.temperature_f
    @_temperature_f.setter
    def _temperature_f(self, temperature_f):
        self.temperature_f=temperature_f

    @property
    def _temperature_string(self):
        return self.temperature_string
    @_temperature_string.setter
    def _temperature_string(self, temperature_string):
        self.temperature_string=temperature_string

    @property
    def _wind(self):
        return self.wind
    @_wind.setter
    def _wind(self,wind):
        self.wind=wind
    
    @property
    def _feels_like_string(self):
        return self.feels_like_string
    @_feels_like_string.setter
    def _feels_like_string(self, feels_like_string):
        self.feels_like_string=feels_like_string
    
    @property
    def _precp_today(self):
        return self.precp_today
    @_precp_today.setter
    def _precp_today(self, precp_today):
        self.precp_today=precp_today
    
    @property
    def _icon_url(self):
        return self.icon_url
    @_icon_url.setter
    def _icon_url(self, icon_url):
        self.icon_url=icon_url
    
    @property
    def _forecast_url(self):
        return self.forecast_url
    @_forecast_url.setter
    def _forecast_url(self, forecast_url):
        self.forecast_url=forecast_url

    def BuildMapping(self,response):
        self.city=response['current_observation']['display_location']['city']
        self.state=response['current_observation']['display_location']['state']
        self.temperature_f=response['current_observation']['temp_f']
        self.temperature_string=response['current_observation']['temperature_string']
        self.wind=response['current_observation']['wind_mph']
        self.feels_like_string=response['current_observation']['feelslike_string']
        self.precp_today=response['current_observation']['precip_today_string']
        self.icon_url=response['current_observation']['icon_url']
        self.forecast_url=response['current_observation']['forecast_url']