#!/usr/bin/python

import csv
from cement.core import handler, output

class CSVOutputHandler(output.CementOutputHandler):
    """
    A custom CSV output handler
    """
    class Meta:
        label = 'csv'
    
    def render(self, data):
        writer = csv.writer(sys.stdout, lineterminator='\n')
