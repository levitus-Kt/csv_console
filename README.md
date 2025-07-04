# Программа принимает на вход csv файл и выводит в консоль значения по заданным параметрам

В файле requirements.txt хранятся названия необходимых библиотек

Установка:

`pip install -r requirements.txt`

Флаги и аргументы:

`--file filename` - Путь к файлу csv. Обязательный параметр. Если передать не csv, выдаст обработанную ошибку

`--where [название_колонки=значение]` - Фильтр значений. Необязательный параметр. Вместо `=` также принимает `< >`

`--aggregate [название_колонки=avg]` - Агрегация числовых значений. Необязательный параметр. Вместо `avg` также принимает `min max`

`--order-by [название_колонки=desc]` - Сортировка значений. Необязательный параметр. Вместо `desc` также принимает `asc`

Флаги могут указываться в любом порядке


### Примеры:

Передача только файла

![image](https://github.com/user-attachments/assets/ad167cb8-0cd2-4d3e-9bf7-e37e201f4323)

Использование фильтра

![image](https://github.com/user-attachments/assets/d013f7a6-8de6-4c49-8659-f1da587329d9)

Использование агрегации

![image](https://github.com/user-attachments/assets/3ad7dfb4-0856-4c74-bf7d-94bc4ff5dfb9)

Агрегация с фильтром

![image](https://github.com/user-attachments/assets/26a873ac-6f58-4798-a89f-fdd80ef9992f)

Сортировка по убыванию

![image](https://github.com/user-attachments/assets/e23c582a-0e26-4e33-bb6d-dd81ab6d1845)

Сортировка по возрастанию

![image](https://github.com/user-attachments/assets/8cd8227f-6f45-46e3-8c18-98a77f26bd11)

Сортировка по возрастанию с фильтром

![image](https://github.com/user-attachments/assets/28638fa0-db6e-4917-b81f-02472fe7a627)

Передача пустого файла, с другим расширением, несуществующего файла соответственно

![image](https://github.com/user-attachments/assets/73c4dbd3-9682-4607-9fbe-d209fa9a5d46)
