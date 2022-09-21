from abc import ABC
from abc import abstractmethod


class ABC_ETLProcessor(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def extract(self) -> None:
        pass

    @abstractmethod
    def transform(self) -> None:
        pass

    @abstractmethod
    def load(self) -> None:
        pass
