import pandas as pd
from base_csv_processor import BaseCSVProcessor


class SpectralProcessor(BaseCSVProcessor):
    def __init__(self, input_file: str, output_file: str, year_filter: int) -> None:
        super().__init__(input_file, output_file)
        self._year_filter = year_filter

    def extract(self) -> None:
        super().extract()
        self._df.date = pd.to_datetime(self._df.date, format="%Y-%m-%d")

    def transform(self) -> None:
        self._df = self._df[self._df.date.dt.year == self._year_filter]
        self._df["ndvi"] = (self._df.nir - self._df.red) / (self._df.nir + self._df.red)

        self._df = self._df.loc[self._df.groupby("tile_id")["ndvi"].idxmax(),
                                ["tile_id", "tile_geometry", "ndvi", "date"]]
        self._df.rename(columns={"ndvi": "pos", "date": "pos_date"}, inplace=True)
        