# Программа принимает на вход csv файл и выводит в консоль значения по заданным параметрам

В файле requirements.txt хранятся необходимые библиотеки

Установка:

`pip install -r requirements.txt`

Флаги и аргументы:

`--file filename` - Путь к файлу csv. Обязательный параметр. Если передать не csv, выдаст обработанную ошибку

`--where [название_колонки=значение]` - Фильтр значений. Необязательный параметр. Вместо `=` также принимает `< >`

`--aggregate [название_колонки=avg]` - Агрегация числовых значений. Необязательный параметр. Вместо `avg` также принимает `min max`

Примеры:

Передача только файла

![image](https://github.com/user-attachments/assets/4c768faa-bac6-4f0c-92e7-819f40f2e635)

Использование фильтра

![image](https://github.com/user-attachments/assets/7e2f7cde-a884-411e-8326-d46423c773f0)

Использование агрегации

![image](https://github.com/user-attachments/assets/cde30503-4fef-4124-be0e-24fc07cbffef)

Агрегация с фильтром

![image](https://github.com/user-attachments/assets/c5205351-958e-4108-9a59-c9b1691a8b23)

Сортировка по убыванию

![order-rating-desc](https://github.com/user-attachments/assets/6bc091ab-1022-435d-9bf5-ac5504f8a8e5)

Сортировка по возрастанию с фильтром

![where-order-name-asc](https://github.com/user-attachments/assets/e662646c-fca3-4c71-957a-b2e1ba5b621a)

Передача пустого файла, с другим расширением, несуществующего файла соответственно

![image](https://github.com/user-attachments/assets/0f7e0267-1cc4-4766-b5d7-135d5f47abc7)
