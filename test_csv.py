import pytest
from csv_console import parse, argument_with_equal, dict_to_list, \
    filter_csv, aggregate_csv, order_csv


@pytest.mark.parametrize("parse_args, expected_result", [
    (['--file', 'products.csv'], None),
    (['--file', 'products.csv', 
      '--where', 'brand=apple'], None),
    (['--file', 'products.csv', 
      '--where', 'brand=apple',
      '--aggregate', 'rating=max'], None),
    (['--file', 'products.png', 
      '--aggregate', 'rating=max'], 1),
    (['--file', 'p.csv'], 1),
    (['--file'], ""),
])
def test_parse_args(capsys, parse_args, expected_result):
    try:
        # expected_result = parse(parse_args)
        assert parse(parse_args) == expected_result
    except SystemExit:
        out, err = capsys.readouterr()
        assert out == expected_result

        

@pytest.mark.parametrize("args, expected_result", [
    ('brand=samsung', 'brand=samsung'),
    ('b=ssg', 'b=ssg'),
    ('brand=apple', 'brand=apple'),
    ('rating=max', 'rating=max'),
    ('rating=avg', 'rating=avg'),
    ('rating=min', 'rating=min'),
    ('s=s', 's=s'),
])
def test_right_argument_with_equal(args, expected_result):
    assert argument_with_equal(args) == expected_result


@pytest.mark.parametrize("args", [
    'brand=',
    'b=',
    '=a',
    '=samsung',
    '=',
    '',
])
def test_wrong_argument_with_equal(capsys, args):
    with pytest.raises(SystemExit):
        argument_with_equal(args)
    out, err = capsys.readouterr()
    assert out == 'Неправильно задан аргумент(-ы). Используйте -h, чтобы узнать больше\n'


def test_file():
    assert parse(['--file', 'products.csv']) == None
    assert parse(['--file', 'csv.csv']) == 1


def test_dict_to_list(data_fill, source_dict):
    assert dict_to_list(data_fill) == source_dict
    with pytest.raises(AttributeError):
        dict_to_list([1, 2])
        dict_to_list(['a', 'b'])


@pytest.mark.parametrize("args, expected_result", [
    ('brand=apple', None),
    ('b=xiaomi', "Заголовка b нет в файле\n"),
    ('rating=4', "Нет данных в этом столбце с такими параметрами\n"),
    ('rating>4', None),
    ('price>0', None),
    ('price<0', "Нет данных в этом столбце с такими параметрами\n"),
    ('p<0', "Заголовка p нет в файле\n"),
])
def test_filter(args, data_fill, expected_result, capsys):
    try:
        expected_result = filter_csv(args, data_fill)
        assert filter_csv(args, data_fill) == expected_result
    except SystemExit:
        out, err = capsys.readouterr()
        assert out == expected_result



@pytest.mark.parametrize("name_column, aggregate_type, expected_result", [
    ('rating', 'max', None),
    ('brand', 'xiaomi', "В столбце brand не все значения числовые\n"),
    ('rating', '4', None),
    ('rating', 'min', None),
    ('rating', 'avg', None),
    ('price', 'avg', None),
    ('price', 'min', None),
    ('price', 'max', None),
    ('p', 'max', "Заголовка p нет в файле\n"),
])
def test_aggregate(name_column, aggregate_type, data_fill, expected_result, capsys):
    try:
        expected_result = aggregate_csv(name_column, aggregate_type, data_fill)
        assert aggregate_csv(name_column, aggregate_type, data_fill) == expected_result
    except SystemExit:
        out, err = capsys.readouterr()
        assert out == expected_result


@pytest.mark.parametrize("name_column, order_type, expected_result", [
    ('price', 'desc', None),
    ('price', 'asc', None),
    ('brand', 'asc', None),
    ('name', 'desc', None),
    ('p', 'asc', "Заголовка p нет в файле\n"),
    ('price', 'min', "Неправильно указан параметр сортировки\n"),
    ('name', 'max', "Неправильно указан параметр сортировки\n"),
    ('p', 'max', "Заголовка p нет в файле\n"),
])
def test_order(name_column, order_type, data_fill, expected_result, capsys):
    try:
        expected_result = order_csv(name_column, order_type, data_fill)
        assert order_csv(name_column, order_type, data_fill) == expected_result
    except SystemExit:
        out, err = capsys.readouterr()
        assert out == expected_result
