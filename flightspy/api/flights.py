#!/usr/bin/python
import os
import requests
import json

class Flight(object):
    """
    'origin': 'from IATA code e.g. LAX',
    'to': 'to IATA code e.g. CLT',
    'date': 'departure date in format YYYY-MM-DD',
    'passengers': 'count of adult passengers'
    """
    def __init__(self, origin, to, date, passengers=1):

        self.origin = origin
        self.to = to
        self.date = date
        self.passengers = passengers

        serialized_data = self._serialize()
        self.response = self._request(serialized_data)

    def _serialize(self):
        """
        Should take flight parameters from arguments and return them in 
        json format
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
                        'date': self.date
                    }    
                ],
                'solutions': '1'
            }
        })

    def _request(self, data):
        """
        Function wrapping Python-requests for making a request to 
        Google's QPX API.

        Should take serialized data, hit the QPX API, and return the 
        json response as a Python dict.

        Before making a request, set a QPX_API_KEY environmental 
        variable to your API key.
        """
        url = 'https://www.googleapis.com/qpxExpress/v1/trips/search'
        key = os.environ.get('QPX_API_KEY')
        r = requests.post(
            url = url,
            params = {'key': key},
            data = data,
            headers = {'Content-Type': 'application/json'},
        )
        response = json.loads(r.text)
        return response
