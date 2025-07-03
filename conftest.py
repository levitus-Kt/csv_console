import pytest
import csv
from .csv_console import parse

@pytest.fixture
def data_fill():
    data = []
    with open('products.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data
