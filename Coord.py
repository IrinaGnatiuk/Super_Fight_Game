import requests

APP_ID = 'AIzaSyCecPWyeBgzhtFMKtQvOVQtZeq4FVL2KcI'


class CoordApi():
    latlng = None
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    address = None

    def get_location(self, address=None, latlng=None):
        response = requests.get(self.url, {
            'key': APP_ID,
            'address': address,
            'latlng':  latlng,
        })
        return response.json()

    def get_coord_by_address(self, address):
        return self.get_location(address=address)

    def get_address_by_coords(self, latlng):
        return self.get_location(latlng)


request1 = CoordApi()
print(request1.get_coord_by_address(address="1600 Amphitheatre Parkway, Mountain View, CA"))
print(request1.get_address_by_coords(latlng='40.714224,-73.961452'))
print(request1.get_coord_by_address(address="Odesa, Odessa Province, Ukraine"))
print(request1.get_address_by_coords(latlng='46.469391, 30.740883'))
print(request1.get_coord_by_address(address="Kyiv, Kyiv Capital City Area, Ukraine"))
print(request1.get_address_by_coords(latlng='50.450001, 30.523333'))
print(request1.get_coord_by_address(address="Deribasovska street,25"))
print(request1.get_coord_by_address(address="Fontanska doroga street,4"))