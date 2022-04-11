import json
import sqlite3
import requests
import logging
from brewery import Brewery

logging.basicConfig(level=logging.INFO)

texas_breweries = []
page_number = 1
state = "texas"
page_size = 50

stop = False
while not stop:
    r = requests.get(f"https://api.openbrewerydb.org/breweries?by_state={state}&page={page_number}&per_page={page_size}")
    breweries = r.json()
    if breweries:
        for b in breweries:
            texas_breweries.append(b)
        page_number += 1
    else:
        stop = True

connection = sqlite3.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())
cur = connection.cursor()

for b in range(len(texas_breweries)):
    brewery = texas_breweries[b]
    breweryAsJson = json.dumps(brewery)
    breweryAsObj = json.loads(breweryAsJson, object_hook=Brewery.from_json)
    cur.execute("INSERT INTO breweries (bid, name, brewery_type, street, "
                "addr2, addr3, city, state, "
                "county_province, postal_code, country, longitude, "
                "latitude, phone, website_url, updated_at, created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (breweryAsObj.bid, breweryAsObj.name, breweryAsObj.brewery_type, breweryAsObj.street,
                 breweryAsObj.addr2, breweryAsObj.addr3, breweryAsObj.city, breweryAsObj.state,
                 breweryAsObj.county_province, breweryAsObj.zip_code, breweryAsObj.country, breweryAsObj.longitude,
                 breweryAsObj.latitude, breweryAsObj.phone, breweryAsObj.website_url, breweryAsObj.updated_at,
                 breweryAsObj.created_at))
    connection.commit()

connection.close()
