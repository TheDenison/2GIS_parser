import json


def table_json(outputs):
    keys = ["ID", "Категория", "Название", "Филиалы", "Адрес", "Сайт", "ИП/ИНН", "Ссылка", "Рейтинг",
            "Оценок", "Телефоны", "Email"]
    data_json = [dict(zip(keys, output)) for output in outputs]

    with open("Excels/data.json", "w", encoding="utf-8") as f:
        json.dump(data_json, f, ensure_ascii=False, indent=4)
