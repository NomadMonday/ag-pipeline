from process.abc_etl_processor import ABC_ETLProcessor
from process.crop_processor import CropProcessor
from process.soil_processor import SoilProcessor
from process.spectral_processor import SpectralProcessor
from process.weather_processor import WeatherProcessor


def create_crop_processor(input_file: str, output_file: str, year_filter: int) -> ABC_ETLProcessor:
    return CropProcessor(input_file, output_file, year_filter)


def create_spectral_processor(input_file: str, output_file: str, year_filter: int) -> ABC_ETLProcessor:
    return SpectralProcessor(input_file, output_file, year_filter)


def create_soil_processor(input_file: str, output_file: str) -> ABC_ETLProcessor:
    return SoilProcessor(input_file, output_file)


def create_weather_processor(input_file: str, output_file: str, year_filter: int) -> ABC_ETLProcessor:
    return WeatherProcessor(input_file, output_file, year_filter)
