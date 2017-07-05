import sys
import logging
import mystique


def test_mystique(capsys):
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    cap = capsys
    logger = logging.getLogger('a')
    logger.info('Hello')
    output, err = cap.readouterr()
    assert 'Hello' in output

    l2 = mystique.adapt(logger, '[id=12345]')
    l2.info('Hello again')
    output, err = cap.readouterr()
    assert '[id=12345] Hello again' in output
