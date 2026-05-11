try:
    from Pilot.pilotTools import CommandBase
except ImportError:
    from pilotTools import CommandBase


class GreenHello(CommandBase):

    def __init__(self, pilotParams):
        super(GreenHello, self).__init__(pilotParams)

    def execute(self):
        self.log.info("HELLO FROM GREENHELLO")
        return True
