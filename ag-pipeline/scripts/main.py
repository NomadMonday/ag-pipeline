import factory
import os
import re
from input_file_manager import InputFileManager


def main():
    files = ["crop.csv", "soil.csv", "spectral.csv", "weather.csv"]
    base_path = re.sub(r"(.+(?:/|\\))scripts(?:/|\\)main.py", r"\1", __file__)
    input_path = f"{base_path}inputs{os.sep}"
    input_filepath = f"{input_path}inputs.zip"
    output_path = f"{base_path}outputs{os.sep}"

    with InputFileManager(input_filepath, files):
        crop_input_file = f"{input_path}crop.csv"
        crop_output_file = f"{output_path}crop.csv"
        crop_processor = factory.create_crop_processor(crop_input_file, crop_output_file, 2021)
        crop_processor.extract()
        crop_processor.transform()
        crop_processor.load()

        spectral_input_file = f"{input_path}spectral.csv"
        spectral_output_file = f"{output_path}spectral.csv"
        spectral_processor = factory.create_spectral_processor(spectral_input_file, spectral_output_file, 2021)
        spectral_processor.extract()
        spectral_processor.transform()
        spectral_processor.load()

        soil_input_file = f"{input_path}soil.csv"
        soil_output_file = f"{output_path}soil.csv"
        soil_processor = factory.create_soil_processor(soil_input_file, soil_output_file)
        soil_processor.extract()
        soil_processor.transform()
        soil_processor.load()

        weather_input_file = f"{input_path}weather.csv"
        weather_output_file = f"{output_path}weather.csv"
        weather_processor = factory.create_weather_processor(weather_input_file, weather_output_file, 2021)
        weather_processor.extract()
        weather_processor.transform()
        weather_processor.load()


if __name__ == "__main__":
    main()
