name: Run

on:
  push:
    branches:
      - main  # Trigger the workflow on push to the main branch
  pull_request:
    branches:
      - main  # Trigger the workflow on pull request to the main branch

jobs:
  run-python-file:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'  # Specify the Python version you need

    - name: Run script
      run: python script.py
