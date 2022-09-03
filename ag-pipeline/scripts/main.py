import os
import re
from input_file_manager import InputFileManager


def main():
    files = ["crop.csv", "soil.csv", "spectral.csv", "weather.csv"]
    input_file = re.sub(r"(.+(?:/|\\))scripts(?:/|\\)main.py", rf"\1inputs{os.sep}inputs.zip", __file__)
    with InputFileManager(input_file, files):
        test = "test"


if __name__ == "__main__":
    main()
