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
                # Reuse "extra" from the given logger, if present.
                extra.update(logger.extra)
            except AttributeError:
                pass

            super().__init__(logger, extra)
            # This below is for Python < 3.6
            if not hasattr(self, 'manager'):
                self.manager = logger.manager

    return Adapter(logger, kwargs)
