import sys
import json
from cement.core import handler, output

class FlightJSONOutputHandler(output.CementOutputHandler):
    """
    A custom JSON output handler
    """
    class Meta:
        label = 'json'

    def render(self, data):
        print 'HEY THERE'
        json.dump(
            data,
            sys.stdout,
        )

def load(app):
    handler.register(FlightJSONOutputHandler)
