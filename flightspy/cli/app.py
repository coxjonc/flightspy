#!/usr/bin/python
from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose

class BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Cool times with this app'
        arguments = [
            (['-f', '--foo'],
                dict(action='store', help='foo'))
        ]

    @expose(hide=True)
    def default(self):
        self.app.log.info('Inside BaseController.default()')
        if self.app.pargs.foo:
            print('Received option foo => {foo}'.format(foo=self.app.pargs.foo))

    @expose(help='Useless command')
    def command1(self):
        self.app.log.info('command1() called')

class App(CementApp):
    class Meta:
        label = 'myapp'
        base_controller = 'base'
        handlers = [BaseController]

def main(): 
    with App() as app:
        app.run()
