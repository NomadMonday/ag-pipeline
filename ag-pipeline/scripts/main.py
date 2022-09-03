import os
from zipfile import ZipFile


def main():
    inputs_path = os.path.join(os.getcwd(), "..", "inputs")
    inputs_file = os.path.join(inputs_path, "inputs.zip")
    with ZipFile(inputs_file, "r") as zip_ref:
        zip_ref.extractall(inputs_path)

    files = [os.path.join(inputs_path, file) for file in
             ["crop.csv", "soil.csv", "spectral.csv", "weather.csv"]]
    [os.remove(file) for file in files]


if __name__ == "__main__":
    main()
