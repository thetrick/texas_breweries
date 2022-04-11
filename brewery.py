import json


class Brewery:
    def __init__(self, id, name, brewery_type, street, addr2, addr3, city, state,
                 county_province, zip_code, country, longitude, latitude, phone, website_url,
                 updated_at, created_at):
        self.bid = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.addr2 = addr2
        self.addr3 = addr3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.zip_code = zip_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        return self.__str__()

    @staticmethod
    def from_json(json_dct):
        return Brewery(json_dct['id'], json_dct['name'], json_dct['brewery_type'], json_dct['street'],
                       json_dct['address_2'], json_dct['address_3'], json_dct['city'], json_dct['state'],
                       json_dct['county_province'], json_dct['postal_code'], json_dct['country'],
                       json_dct['longitude'], json_dct['latitude'], json_dct['phone'], json_dct['website_url'],
                       json_dct['updated_at'], json_dct['created_at'])
