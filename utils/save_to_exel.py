import datetime

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from utils.metro_stations import *


def table_exel(data, chat_id):
    # Создание новой книги и листа
    wb = Workbook()
    ws = wb.active

    branch_1_fill = PatternFill(start_color="EF161E", end_color="EF161E", fill_type="solid")
    branch_2_fill = PatternFill(start_color="2DBE2C", end_color="2DBE2C", fill_type="solid")
    branch_3_fill = PatternFill(start_color="006BB0", end_color="006BB0", fill_type="solid")
    branch_4_fill = PatternFill(start_color="15B4E4", end_color="15B4E4", fill_type="solid")
    branch_5_fill = PatternFill(start_color="8B4E31", end_color="8B4E31", fill_type="solid")
    branch_6_fill = PatternFill(start_color="E37822", end_color="E37822", fill_type="solid")
    branch_7_fill = PatternFill(start_color="8C3C89", end_color="8C3C89", fill_type="solid")
    branch_8_fill = PatternFill(start_color="F4C41D", end_color="F4C41D", fill_type="solid")
    branch_9_fill = PatternFill(start_color="A6A5A5", end_color="A6A5A5", fill_type="solid")
    branch_10_fill = PatternFill(start_color="B7C834", end_color="B7C834", fill_type="solid")
    branch_11_fill = PatternFill(start_color="72BDBF", end_color="72BDBF", fill_type="solid")
    branch_12_fill = PatternFill(start_color="A8B9D9", end_color="A8B9D9", fill_type="solid")
    branch_13_fill = PatternFill(start_color="006BB0", end_color="006BB0", fill_type="solid")
    branch_14_fill = PatternFill(start_color="EDA3A1", end_color="EDA3A1", fill_type="solid")
    branch_15_fill = PatternFill(start_color="E583AE", end_color="E583AE", fill_type="solid")
    branch_17_mcd_1_fill = PatternFill(start_color="EB9E00", end_color="EB9E00", fill_type="solid")
    branch_18_mcd_2_fill = PatternFill(start_color="DF6193", end_color="DF6193", fill_type="solid")
    branch_19_mcd_3_fill = PatternFill(start_color="E75A0C", end_color="E75A0C", fill_type="solid")

    branches = {
        tuple(BRANCH_19_MCD_3): branch_19_mcd_3_fill,
        tuple(BRANCH_18_MCD_2): branch_18_mcd_2_fill,
        tuple(BRANCH_17_MCD_1): branch_17_mcd_1_fill,
        tuple(BRANCH_15): branch_15_fill,
        tuple(BRANCH_14): branch_14_fill,
        tuple(BRANCH_13): branch_13_fill,
        tuple(BRANCH_12): branch_12_fill,
        tuple(BRANCH_11): branch_11_fill,
        tuple(BRANCH_10): branch_10_fill,
        tuple(BRANCH_9): branch_9_fill,
        tuple(BRANCH_8): branch_8_fill,
        tuple(BRANCH_7): branch_7_fill,
        tuple(BRANCH_6): branch_6_fill,
        tuple(BRANCH_5): branch_5_fill,
        tuple(BRANCH_4): branch_4_fill,
        tuple(BRANCH_3): branch_3_fill,
        tuple(BRANCH_2): branch_2_fill,
        tuple(BRANCH_1): branch_1_fill,
    }

    # Задание шаблона для заголовка
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill("solid", fgColor="4F81BD")
    header_alignment = Alignment(horizontal='center')
    headers = ["ID", "Категория", "Название", "Филиалы", "Адрес", "Сайт", "ИП/ИНН", "Станция", "Ссылка", "Рейтинг",
               "Оценок", "Телефоны",
               "Email"]

    for col_num, header in enumerate(headers, 1):
        col_letter = chr(64 + col_num)
        cell = ws[f"{col_letter}1"]
        cell.value = header
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_alignment

    for row_num, row_data in enumerate(data, 2):
        for col_num, cell_data in enumerate(row_data, 1):
            ws.cell(row=row_num, column=col_num, value=cell_data)

    # Выравнивание по центру
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(vertical='center')

    # Автоматическая настройка ширины столбцов
    for column in ws.columns:
        max_length = 0
        column = [cell for cell in column]
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except Exception:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column[0].column_letter].width = adjusted_width

        # Танируем ячейки
        for row in ws['H']:
            for branch, fill in branches.items():
                if any(station in row.value for station in branch):
                    row.fill = fill
                    break
    try:
        # Проверка окраски оценки
        def interpolate_color(color1, color2, fraction):
            r1, g1, b1 = color1
            r2, g2, b2 = color2

            new_r = int(r1 + (r2 - r1) * fraction)
            new_g = int(g1 + (g2 - g1) * fraction)
            new_b = int(b1 + (b2 - b1) * fraction)

            return new_r, new_g, new_b

        def get_color_for_value(value):
            RED = (255, 0, 0)
            ORANGE = (255, 165, 0)
            YELLOW = (255, 255, 0)
            LIGHT_GREEN = (124, 252, 0)
            GREEN = (0, 255, 0)

            value = float(value)

            if value <= 1.5:
                return RED
            elif value <= 2:
                return interpolate_color(RED, ORANGE, value - 1.5)
            elif value <= 2.5:
                return ORANGE
            elif value < 3:
                return interpolate_color(ORANGE, YELLOW, value - 2.5)
            elif value <= 3.5:
                return YELLOW
            elif value <= 4:
                return interpolate_color(YELLOW, LIGHT_GREEN, value - 3.5)
            elif value <= 4.5:
                return LIGHT_GREEN
            elif value < 5:
                return interpolate_color(LIGHT_GREEN, GREEN, value - 4.5)
            else:
                return GREEN

        def is_empty(cell_value):
            return cell_value is None or str(cell_value).strip() == ""

        # Пропустк заголовка и проход по столбцу "J"
        for cell in ws['J'][1:]:
            if not is_empty(cell.value):
                r, g, b = get_color_for_value(cell.value)
                fill_color = f"{r:02X}{g:02X}{b:02X}"
                cell.fill = PatternFill(start_color=fill_color, end_color=fill_color, fill_type="solid")
    except Exception as e:
        print(e)

    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M')
    # Сохраняем файл
    wb.save(f"Excels/Table_{cur_time}.xlsx")
    if chat_id != "1":
        wb.save(f"Excels/Table_{chat_id}.xlsx")
