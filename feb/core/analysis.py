"""
This modules hold the analysis logic.
"""
from abc import ABCMeta, abstractmethod


class Session(metaclass=ABCMeta):
    """
    A binary analysis session. Used to perform analysis actions on an open binary.
    """

    @property
    @abstractmethod
    def binary(self):
        """
        The open binary of this analysis session.
        :return: The Binary object of this session.
        """
        raise NotImplementedError()

    @abstractmethod
    def close(self):
        """
        Close a session.
        """
        raise NotImplementedError()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, trace):
        self.close()


class Analyzer(metaclass=ABCMeta):
    """
    A binary analyzer. Can load multiple sessions.
    Analyzer options are global for all sessions.
    """

    @abstractmethod
    def load(self, path) -> Session:
        """
        Loads a binary.

        :param path: The path to the binary.
        :return: A Session instance of the binary being analyzed.
        """
        raise NotImplementedError()
