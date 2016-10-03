from functools import wraps
import logging

logger = logging.getLogger(__name__)


def logged(logger=logger):

    def inner(func):
        logger.info(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.debug('{} of {} with {}'.format(func.func_name, args[0].__class__.__name__, kwargs))
            return func(*args, **kwargs)

        return wrapper
    return inner


def log_methods(cls):
    for entry in filter(lambda item: callable(item[1]), list(vars(cls).iteritems())):
        setattr(cls, entry[0], logged(logger)(entry[1]))
    return cls