#!/usr/bin/python
from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose

class FlightspyBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Get and process data from Google\'s flight API'
        arguments = [
            (['-f', '--fuzzy'],
                dict(action='store', 
                    help='NOT IMPLEMENTED: Return flights within a range of 
                        the date.'))
        ]

    @expose(hide=True)
    def default(self):
        self.app.args.print_help()

    @expose(help='Get flight data from QPX')
    def get(self):
        """
        ``flightspy get <from> <to> <date>``

        Returns flight data for the given parameters

        Command:

        ..code:: bash
            
            flightspy get LAX CLT 2016-08-10

        Example output:

        .. csv-table:
            carrier,flightnumber,departuretime,arrivaltime,price,route
            Delta,1234,2016-08-10T17:17:42Z,410USD,LAX-IAD-CLT
        """
        flight = Flight()

class FlightApp(CementApp):
    class Meta:
        label = 'app'
        base_controller = FlightspyBaseController
        extensions = [
            'flightspy.cli.ext_csv'        
        ]
        output_handler = 'csv'

def main(): 
    with FlightApp() as app:
        app.run()
