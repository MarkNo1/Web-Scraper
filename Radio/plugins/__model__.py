import abc


class RadioModel(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        print('Abstract Model')

    @abc.abstractmethod
    def urls(self):
        pass

    @abc.abstractmethod
    def target(self):
        pass

    @abc.abstractmethod
    def info_to_song(self):
        pass

    @abc.abstractmethod
    def name(self):
        pass
