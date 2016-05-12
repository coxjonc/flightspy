from flightspy.api.flights import Flight

def add_flight_hook(app):
    """
    Cache flight API object reference after parsing arguments
    """
    app.flight = Flight(
       date = app.pargs.date,
       origin = app.pargs.origin,
       to = app.pargs.to
    )
