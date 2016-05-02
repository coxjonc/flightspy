#!/usr/bin/python
from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose

from flightspy.api.flights import Flight

class FlightspyBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Get and process flight information'
        arguments = [
            (['origin'], dict(
                nargs='*',
                action='store',
                help='IATA code of departure airport (e.g. "LAX")'
            ))
        ]
