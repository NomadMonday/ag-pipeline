import pandas as pd
from base_csv_processor import BaseCSVProcessor


class WeatherProcessor(BaseCSVProcessor):
    def __init__(self, input_file: str, output_file: str, year_filter: int) -> None:
        super().__init__(input_file, output_file)
        self._year_filter = year_filter

    def transform(self) -> None:
        self._df = self._df[self._df.year == self._year_filter] \
            .groupby("fips_code").agg({"precip": "sum", "temp": ["min", "max", "mean"]}) \
            .reset_index()
        self._df.columns = ["fips_code", "total_precip", "min_temp", "max_temp", "mean_temp"]
        # TODO: Cross-reference fips_code to field_id using field_geometry in crop.csv.
