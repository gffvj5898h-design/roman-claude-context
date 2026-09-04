from artifact_tool import Blob, SpreadsheetFile


def _sum_formula(rows: list[int], column: str) -> str:
    if not rows:
        return "=0"
    refs = ",".join(f"{column}{row}" for row in rows)
    return f"=SUM({refs})"


def build_daily_dispatch(
    source_file: str,
    output_file: str,
    sheet_name: str,
    date_text: str,
    rows: list[list],
) -> None:
    """
    rows: список строк вида
    [госномер, колесная формула, грузоподъемность, место погрузки,
     материал, количество рейсов, None]
    """
    wb = SpreadsheetFile.import_xlsx(Blob.load(source_file))
    ws = wb.worksheets.get_or_add(sheet_name)

    data_start = 4
    data_end = data_start + len(rows) - 1
    totals_start = data_end + 3
    total_crushed = totals_start
    total_sand = totals_start + 1
    total_gravel = totals_start + 2
    total_all = totals_start + 3
    used_end = total_all

    # Очищаем рабочую область с запасом.
    ws.get_range(f"A1:G{max(used_end, 200)}").clear({"contents": True})

    try:
        ws.unmerge_cells("A1:G1")
    except Exception:
        pass
    ws.merge_cells("A1:G1")

    ws.get_range("A1").values = [[f"Разнарядка самосвалов на {date_text}"]]
    ws.get_range("A3:G3").values = [[
        "Гос. номер",
        "Колёсная формула",
        "Грузоподъёмность, т",
        "Место погрузки",
        "Материал",
        "Количество рейсов",
        "Плановый объём, т",
    ]]

    if rows:
        ws.get_range(f"A{data_start}:G{data_end}").values = rows
        ws.get_range(f"G{data_start}").formulas = [[f"=C{data_start}*F{data_start}"]]
        ws.get_range(f"G{data_start}:G{data_end}").fill_down()

    material_rows = {"Щебень": [], "Песок": [], "Гравий": []}
    for excel_row, record in enumerate(rows, start=data_start):
        material = str(record[4]).strip().lower()
        if "щебень" in material:
            material_rows["Щебень"].append(excel_row)
        elif material == "песок":
            material_rows["Песок"].append(excel_row)
        elif material == "гравий":
            material_rows["Гравий"].append(excel_row)

    ws.get_range(f"A{total_crushed}:A{total_all}").values = [
        ["Итого щебень"],
        ["Итого песок"],
        ["Итого гравий"],
        ["Общий итог"],
    ]

    for total_row, category in [
        (total_crushed, "Щебень"),
        (total_sand, "Песок"),
        (total_gravel, "Гравий"),
    ]:
        ws.get_range(f"F{total_row}").formulas = [[_sum_formula(material_rows[category], "F")]]
        ws.get_range(f"G{total_row}").formulas = [[_sum_formula(material_rows[category], "G")]]

    ws.get_range(f"F{total_all}").formulas = [[f"=SUM(F{total_crushed}:F{total_gravel})"]]
    ws.get_range(f"G{total_all}").formulas = [[f"=SUM(G{total_crushed}:G{total_gravel})"]]

    border = {
        "top": {"style": "thin", "color": "#A6B9C8"},
        "bottom": {"style": "thin", "color": "#A6B9C8"},
        "left": {"style": "thin", "color": "#A6B9C8"},
        "right": {"style": "thin", "color": "#A6B9C8"},
    }

    ws.get_range("A1:G1").format = {
        "fill": "#1F4E78",
        "font": {"bold": True, "color": "#FFFFFF", "size": 15},
        "horizontal_alignment": "center",
        "vertical_alignment": "center",
    }
    ws.get_range("A3:G3").format = {
        "fill": "#D9EAF7",
        "font": {"bold": True, "size": 11},
        "horizontal_alignment": "center",
        "vertical_alignment": "center",
        "wrap_text": True,
        "borders": border,
    }

    if rows:
        ws.get_range(f"A{data_start}:G{data_end}").format = {
            "font": {"size": 11},
            "vertical_alignment": "center",
            "wrap_text": True,
            "borders": border,
        }
        ws.get_range(f"A{data_start}:C{data_end}").format.horizontal_alignment = "center"
        ws.get_range(f"D{data_start}:E{data_end}").format.horizontal_alignment = "left"
        ws.get_range(f"F{data_start}:G{data_end}").format.horizontal_alignment = "center"

        for row in range(data_start, data_end + 1):
            ws.get_range(f"A{row}:G{row}").format.fill = "#D9EAF7" if row % 2 == 0 else "#FFFFFF"
            ws.get_range(f"{row}:{row}").format.row_height = 30

    for row in [total_crushed, total_sand, total_gravel]:
        ws.get_range(f"A{row}:G{row}").format = {
            "fill": "#E2F0D9",
            "font": {"bold": True, "size": 11},
            "vertical_alignment": "center",
            "borders": border,
        }

    ws.get_range(f"A{total_all}:G{total_all}").format = {
        "fill": "#FFD966",
        "font": {"bold": True, "size": 11},
        "vertical_alignment": "center",
        "borders": {
            "top": {"style": "medium", "color": "#9C7A00"},
            "bottom": {"style": "medium", "color": "#9C7A00"},
            "left": {"style": "thin", "color": "#A6B9C8"},
            "right": {"style": "thin", "color": "#A6B9C8"},
        },
    }

    ws.get_range(f"A{total_crushed}:E{total_all}").format.horizontal_alignment = "left"
    ws.get_range(f"F{total_crushed}:G{total_all}").format.horizontal_alignment = "center"

    for column, width in {
        "A:A": 13.71,
        "B:B": 11.71,
        "C:C": 15.43,
        "D:D": 22.29,
        "E:E": 28.14,
        "F:F": 14.86,
        "G:G": 15.86,
    }.items():
        ws.get_range(column).format.column_width = width

    ws.get_range("1:1").format.row_height = 28
    ws.get_range("3:3").format.row_height = 54
    ws.get_range(f"C{data_start}:C{max(data_end, data_start)}").format.number_format = "0"
    ws.get_range(f"F{data_start}:G{total_all}").format.number_format = "0"

    SpreadsheetFile.export_xlsx(wb).save(output_file)
