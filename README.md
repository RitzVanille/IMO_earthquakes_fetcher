# Easy retrival of the Iceland Meteorological Office eqrthquake catalogue 

The [IMO](https://vedur.is/) curates the earthquake bulletin for Iceland with the SIL catalogue (South Iceland Lowland, extended to the whole country since).

## Data coverage

1994-present, archived weekly

## Usage

The script can be ran directly by using:
```
python3 get_IMO_earthquakes.py
```
If you want to change the name of the output file, you can do so by altering the variable called `CATALOGUE_FILE_NAME` inside the script.

## Dependencies

This script needs the python [`requests` package](https://docs.python-requests.org/en/latest/) to run.
If the package is not already installed on your system, you can install it in a virtual environment 
1. Create virtual environment (for example by storing the venv as a `.venv`)
```
python3 -m venv <PathToVenv>
```
2. activate it 
```
source <PathToVenv>/bin/activate
```
3. Install needed packages:
```
pip3 install requests 
```

The virtual environment is now set up and you can activate it before running the script with the command: 
```
source <PathToVenv>/bin/activate
```

## Licence

This project is free software: You can redistribute it and/or modify it under the terms of the European Union Public Licence (EUPL v.1.2) or – as soon they will be approved by the European Commission - subsequent versions of the EUPL (the "Licence"); You may not use this work except in compliance with the Licence.

The project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the Licence for the specific language governing permissions and limitations under the Licence.
