import pandas as pd
from base_csv_processor import BaseCSVProcessor


class SoilProcessor(BaseCSVProcessor):
    def transform(self) -> None:
        self._df["hz_layer_weights"] = abs(self._df.hzdept - self._df.hzdepb) / self._df.hzdepb
        self._df.om = self._df.om * (self._df.comppct / 100) * self._df.hz_layer_weights
        self._df.cec = self._df.cec * (self._df.comppct / 100) * self._df.hz_layer_weights
        self._df.ph = self._df.ph * (self._df.comppct / 100) * self._df.hz_layer_weights
        self._df = self._df.groupby("mukey").agg({
            "mukey_geometry": "max",
            "om": "sum",
            "cec": "sum",
            "ph": "sum"
        })
        