#!/usr/bin/python
from flightspy.api import flights
from flightspy.cli.hooks import add_flight_hook
from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose

class FlightspyBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Get and process data from Google\'s flight API'
        arguments = [
           (['-d', '--date'],
                dict(action='store', 
                    help='Specify departure date')),
           (['-t', '--to'],
                dict(action='store', 
                    help='Specify the IATA code of destination airport')),
           (['-o', '--origin'],
                dict(action='store', 
                    help='Specify the IATA code of origin airport')),
        ]

    @expose(hide=True)
    def default(self):
        self.app.args.print_help()

    @expose(help='Get flight data from QPX')
    def get(self):
        """
        ``flightspy get -f <from> -t <to> -d <date>``

        Returns flight data for the given parameters

        Command:

        ..code:: bash
            
            flightspy get LAX CLT 2016-08-10

        Example output:

        .. csv-table:
            carrier,flightnumber,departuretime,arrivaltime,price,route
            Delta,1234,2016-08-10T17:17:42Z,410USD,LAX-IAD-CLT
        """
        print self.app.flight.price

class FlightApp(CementApp):
    class Meta:
        label = 'app'
        base_controller = FlightspyBaseController
        hooks = [
            ('post_argument_parsing', add_flight_hook),        
        ]

def main(): 
    with FlightApp() as app:
        app.run()
