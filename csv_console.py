import argparse
import csv
import os
import sys
from statistics import mean
from tabulate import tabulate


def argument_with_equal(value):
    if '=' not in value:
        print("Неправильно задан аргумент(-ы). Используйте -h, чтобы узнать больше")
        exit()
    if not value.split('=')[0] or not value.split('=')[1]:
        print("Неправильно задан аргумент(-ы). Используйте -h, чтобы узнать больше")
        exit()
    return value


def dict_to_list(dict_after_csv):
    table_list = [list(dict_after_csv[0].keys())]
    for diction in dict_after_csv:
        table_list.append(list(diction.values()))
    return table_list


def parse(argv):
    parser = argparse.ArgumentParser(description="Обработка csv файла")
    parser.add_argument("--file", help="Исходный файл", required=True)
    parser.add_argument("--where", help="Фильтр значений вида: \"название_колонки=/</>значение\"")
    parser.add_argument("--aggregate", type=argument_with_equal, help="Агрегация числовых значений: \"название_колонки=min/max/avg\"")
    parser.add_argument("--order-by", type=argument_with_equal, help="Сортировка значений: \"название_колонки=desc/asc\"")

    args = parser.parse_args(argv)

    if os.path.splitext(args.file)[1].lower() != '.csv':
        print("Выберите файл с расширением .csv")
        return 1
    
    if not os.path.exists(args.file):
        print("Файл или папка не найдены")
        return 1
    

    data = []
    with open(args.file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        try:
            next(reader)
        except StopIteration:
            print("Предоставлен пустой файл")
            return 1

        for row in reader:
            data.append(row)

        if args.where:
            data = filter_csv(args.where, data)

        if args.order_by:
            name_column, order_type = args.order_by.split("=")
            data = order_csv(name_column, order_type, data)
    
        if args.aggregate:
            name_column, aggregate_type = args.aggregate.split("=")
            data = aggregate_csv(name_column, aggregate_type, data)

    if type(data[0]) == dict: data = dict_to_list(data)
    table = tabulate(data, headers="firstrow", tablefmt="grid")
    print(table)
    return 


def filter_csv(args, data):
    filter_list = []
    try:
        name_column, filter_value = args.split("=")
            
        for row in data:
            if row[name_column] == filter_value:
                filter_list.append(row)
    except KeyError:
        print(f"Заголовка {name_column} нет в файле")
        exit()
    except ValueError:
        try:
            try:
                name_column, filter_value = args.split(">")
                for row in data:
                    if row[name_column] > filter_value:
                        filter_list.append(row)
            except ValueError:
                name_column, filter_value = args.split("<")
                for row in data:
                    if row[name_column] < filter_value:
                        filter_list.append(row)
        except KeyError:
            print(f"Заголовка {name_column} нет в файле")
            exit()
    
    if not filter_list:
        print("Нет данных в этом столбце с такими параметрами")
        exit()
    return filter_list


def aggregate_csv(name_column, aggregate_type, data):
    aggregate_list = []
    value = 0.0

    try:
        for i in range(len(data)):
            try:
                float(data[i][name_column])
            except AttributeError and ValueError:
                print(f"В столбце {name_column} не все значения числовые")
                exit()
            aggregate_list.append(float(data[i][name_column]))
    except KeyError:
        print(f"Заголовка {name_column} нет в файле")
        exit()

    if aggregate_type == "min":
        value = min(aggregate_list)
    elif aggregate_type == "max":
        value = max(aggregate_list)
    elif aggregate_type == "avg":
        value = round(mean(aggregate_list), 1)

    data = [[aggregate_type], [value]]
    return data


def order_csv(name_column, order_type, data):
    try:
        values_list = list(map(lambda item: item[name_column], data))
    except KeyError:
        print(f"Заголовка {name_column} нет в файле")
        exit()

    try:
        values_list = list(map(float, values_list))
    except ValueError:
        pass
        
    dict1 = {i: val for i, val in enumerate(values_list)}
    if order_type == "asc":
        dict1 = sorted(dict1.items(), key=lambda item: item[1])
    elif order_type == "desc":
        dict1 = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
    else:
        print("Неправильно указан параметр сортировки")
        exit()

    result = list(map(lambda item: data[item[0]], dict1))

    return result


if __name__ == "__main__":
    try:
        parser = parse(sys.argv[1:])
    except FileNotFoundError as fnf:
        print(f"Файл или папка{str(fnf).split(':')[1]} не найдены")
