import logging
LOGGER = logging.getLogger('DemoPackage')


class DemoPackageObj:
    def __init__(self, str_val='None', int_val=0):
        LOGGER.debug("Init Demo Package")
        self.str_val = str_val
        self.int_val = int_val

    def execute(self):
        LOGGER.debug("Start loop")
        for idx in range(min(len(self.str_val), self.int_val)):
            LOGGER.info("str_val (%d) = %s", idx, self.str_val[:idx])
        LOGGER.debug("Wow that was anti-climatic")
