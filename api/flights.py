#!/usr/bin/python
import os
import requests
import json

class Flight(object):
    def __init__(self, origin, to, depart, passengers=1):
        self.origin = origin
        self.to = to
        self.depart = depart
        self.passengers = passengers
        data = self._serialize()
        flights = self._request(data)
        self.price = flights['trips']['tripOption'][0]['saleTotal']

    def _serialize(self):
        """
        Should take flight parameters and return them in clean json format
        """
        return json.dumps({
            'request': {
                'passengers': {
                    'adultCount': self.passengers   
                },
                'slice': [
                    {
                        'origin': self.origin,
                        'destination': self.to,
                        'date': self.depart
                    }    
                ]
            }
        })

    def _request(self, data):
        """
        Should take serialized data, hit the QPX API, and return the 
        minimum price of a flight with the given parameters
        """

        url = 'https://www.googleapis.com/qpxExpress/v1/trips/search'
        key = os.environ.get('QPX_API_KEY')
        r = requests.post(
            url = url,
            params = {'key': key},
            data = data,
            headers = {'Content-Type': 'application/json'},
        )
        return json.loads(r.text)

    def __str__(self):
        return self.price
