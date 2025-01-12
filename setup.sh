#!/bin/bash

venv_name=".venv"

# Check if the virtual environment exists
if [ ! -d $venv_name ]; then
   echo "Creating VENV"
   python3 -m venv $venv_name
fi

# Source the virtual environment
echo "Activating virtual environment..."
source $venv_name/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip
