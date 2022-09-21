import pandas as pd
from abc import abstractmethod
from abc_etl_processor import ABC_ETLProcessor


class BaseCSVProcessor(ABC_ETLProcessor):
    def __init__(self, input_file: str, output_file: str) -> None:
        self._input_file = input_file
        self._output_file = output_file
        self._df: pd.DataFrame = None

    def extract(self) -> None:
        self._df = pd.read_csv(self._input_file)

    @abstractmethod
    def transform(self) -> None:
        pass

    def load(self) -> None:
        self._df.to_csv(self._output_file, index=False)
