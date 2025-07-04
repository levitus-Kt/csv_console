import pytest
import csv
from csv_console import parse, dict_to_list

@pytest.fixture
def data_fill():
    global data
    data = []
    with open('products.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

@pytest.fixture
def source_dict():
    list_after = dict_to_list(data)
    return list_after