import logging
LOGGER = logging.getLogger('DemoPackage')


class DemoPackage:
    def __init__(self, str_val='None', int_val=0):
        LOGGER.debug("Init Demo Package")
        self.str_val = str_val
        self.int_val = int_val

    def execute(self):
        for idx in range(min(len(self.str_val), self.int_val)):
            LOGGER.debug("str_val (%d) = %s", idx, self.str_val[:idx])
        LOGGER.info("Wow that was anti-climatic")
