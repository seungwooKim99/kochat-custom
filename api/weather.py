class WeatherAnswerer():

    def request(self, location: str, date: str):
        try:
            return self.request_debug(location, date)
        except Exception as e:
            print("location: {0} / date: {1}".format(location, date))
            print(e)
            return "Sorry"

    def request_debug(self,location: str, date: str):
        return '{date} {location}의 날씨는 맑음 :)'\
            .format(date=date, location=location)