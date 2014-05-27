"""Singleton decorator function."""

def singleton(klass):
    instances = {}

    def get_instance(*args, **kwargs):
        key = unicode(klass) + unicode(args) + unicode(kwargs)
        if key not in instances:
            instances[key] = klass(*args, **kwargs)

        return instances[key]

    return get_instance

@singleton
class C(object):
    ...
