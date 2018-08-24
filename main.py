from api_key import KEY
from geolocation.main import GoogleMaps

class GeoLocation(object):
    def __init__(self, city):
        self.mycity = city
        self.gmap = GoogleMaps(api_key=KEY)
        self.location = self.gmap.search(location=city).first()
        print('Your lat,long: {},{}'.format(self.location.lat, self.location.lng))
    def get_distance_to(self, dest):
        return self.gmap.distance(self.mycity, dest).first().distance.kilometers

if __name__=='__main__':
    blr = GeoLocation('Bangalore')
    print('Hyderbad is {} KMs from Bangalore'.format(blr.get_distance_to('Hyderabad')))

