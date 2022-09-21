import pandas as pd
from base_csv_processor import BaseCSVProcessor


class CropProcessor(BaseCSVProcessor):
    def __init__(self, input_file: str, output_file: str, year_filter: int) -> None:
        super().__init__(input_file, output_file)
        self._year_filter = year_filter

    def transform(self) -> None:
        self._df = self._df[self._df.year == self._year_filter] \
                       .loc[:, ["field_id", "field_geometry", "crop_type"]]
