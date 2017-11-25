import abc


class RadioModel(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def urls(self):
        pass

    @abc.abstractmethod
    def target(self):
        pass

    @abc.abstractmethod
    def multiple_target(self):
        pass

    @abc.abstractmethod
    def info_to_song(self):
        pass

    @abc.abstractmethod
    def multiple_info_to_song(self):
        pass

    @abc.abstractmethod
    def name(self):
        pass
