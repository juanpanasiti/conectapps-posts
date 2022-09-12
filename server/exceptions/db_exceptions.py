import logging


logger = logging.getLogger()


class PopulatedDBError(Exception):
    def __init__(self, msg, *args):
        super().__init__(args)
        logger.error(msg)
        self.msg = msg

    def __str__(self):
        return f'{self.msg}'


class ConnectionDBError(Exception):
    def __init__(self, msg, *args):
        super().__init__(args)
        logger.error(msg)
        self.msg = msg

    def __str__(self):
        return f'{self.msg}'
