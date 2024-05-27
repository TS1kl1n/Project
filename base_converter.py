import abc

class BaseConverter(metaclass=abc.ABCMeta):
    def __init__(self, input_path):
        self.input_path = input_path

    @abc.abstractmethod
    def convert(self):
        pass
