import logging
import logbind


class CapturingHandler(logging.StreamHandler):
    def __init__(self, *args, capture=None, **kwargs):
        super(CapturingHandler, self).__init__(*args, **kwargs)
        self.capture = capture or []

    def format(self, record: logging.LogRecord):
        """Don't even need a Formatter class at all."""
        self.capture.append(record)
        return super(CapturingHandler, self).format(record)


def test_main():
    logger = logging.getLogger('a')
    capture = []
    logger.addHandler(CapturingHandler(capture=capture))
    logger.info('Hello')
    assert not hasattr(capture[-1], 'id')

    l2 = logbind.bind(logger, id=12345)
    l2.info('Hello again')
    assert capture[-1].id == 12345
