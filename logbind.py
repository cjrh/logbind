"""
Mystique
========

Ever-changing loggers

"""

import logging


__version__ = '2017.7.1'


def adapt(logger, prefix):
    # type: (logging.Logger, Any)
    return _Adapter(logger, prefix)


class _Adapter(logging.LoggerAdapter):
    def __init__(self, logger, prefix_data, **kwargs):
        super(_Adapter, self).__init__(logger, kwargs)
        self.prefix_data = str(prefix_data)

    def process(self, msg, kwargs):
        prefix = str(self.prefix_data)
        return '%s %s' % (prefix, msg), kwargs
