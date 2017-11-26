"""
logbind
=======

Much, much easier interface for ``LoggerAdapter``: bind new fields to
loggers.

"""

import logging


__version__ = '2017.11.1'


def bind(logger, **kwargs) -> logging.LoggerAdapter:

    class Adapter(logging.LoggerAdapter):
        def __init__(self, logger, extra):
            try:
                # Reuse "extra" from the given logger
                extra.update(logger.extra)
            except AttributeError:
                pass
            else:
                super().__init__(logger, extra)

    return Adapter(logger, kwargs)
