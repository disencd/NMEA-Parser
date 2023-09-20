"""
Base class for the inlet files
"""
from abc import ABC, abstractmethod



class InletBot(ABC):

    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def read(self):
        raise NotImplementedError
