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
    if len(rows) > 7:
        raise ValueError("Форма рассчитана максимум на 7 строк разнарядки.")

    wb = SpreadsheetFile.import_xlsx(Blob.load(source_file))
    ws = wb.worksheets.get_or_add(sheet_name)

    ws.get_range("A1:G17").clear({"contents": True})
    try:
        ws.unmerge_cells("A1:G1")
    except Exception:
        pass
    ws.merge_cells("A1:G1")

    ws.get_range("A1").values = [[f"Разнарядка самосвалов на {date_text}"]]
    ws.get_range("A3:G3").values = [[
        "Гос. номер", "Колёсная формула", "Грузоподъёмность, т",
        "Место погрузки", "Материал", "Количество рейсов",
        "Плановый объём, т",
    ]]

    end_row = 3 + len(rows)
    ws.get_range(f"A4:G{end_row}").values = rows
    ws.get_range("G4").formulas = [["=C4*F4"]]
    ws.get_range(f"G4:G{end_row}").fill_down()

    material_rows = {"Щебень": [], "Песок": [], "Гравий": []}
    for excel_row, record in enumerate(rows, start=4):
        material = str(record[4]).lower()
        if "щебень" in material:
            material_rows["Щебень"].append(excel_row)
        elif material == "песок":
            material_rows["Песок"].append(excel_row)
        elif material == "гравий":
            material_rows["Гравий"].append(excel_row)

    ws.get_range("A14:A17").values = [
        ["Итого щебень"], ["Итого песок"], ["Итого гравий"], ["Общий итог"]
    ]

    for total_row, category in [(14, "Щебень"), (15, "Песок"), (16, "Гравий")]:
        ws.get_range(f"F{total_row}").formulas = [[_sum_formula(material_rows[category], "F")]]
        ws.get_range(f"G{total_row}").formulas = [[_sum_formula(material_rows[category], "G")]]

    ws.get_range("F17").formulas = [["=SUM(F14:F16)"]]
    ws.get_range("G17").formulas = [["=SUM(G14:G16)"]]

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
    ws.get_range("A4:G10").format = {
        "font": {"size": 11},
        "vertical_alignment": "center",
        "wrap_text": True,
        "borders": border,
    }
    ws.get_range("A4:C10").format.horizontal_alignment = "center"
    ws.get_range("D4:E10").format.horizontal_alignment = "left"
    ws.get_range("F4:G10").format.horizontal_alignment = "center"

    for row in [4, 6, 8, 10]:
        ws.get_range(f"A{row}:G{row}").format.fill = "#D9EAF7"
    for row in [5, 7, 9]:
        ws.get_range(f"A{row}:G{row}").format.fill = "#FFFFFF"

    for row in [14, 15, 16]:
        ws.get_range(f"A{row}:G{row}").format = {
            "fill": "#E2F0D9",
            "font": {"bold": True, "size": 11},
            "vertical_alignment": "center",
            "borders": border,
        }
    ws.get_range("A17:G17").format = {
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
    ws.get_range("A14:E17").format.horizontal_alignment = "left"
    ws.get_range("F14:G17").format.horizontal_alignment = "center"

    for column, width in {
        "A:A": 13.71, "B:B": 11.71, "C:C": 15.43,
        "D:D": 22.29, "E:E": 28.14, "F:F": 14.86, "G:G": 15.86,
    }.items():
        ws.get_range(column).format.column_width = width

    for row, height in {
        1: 28, 3: 54, 4: 40.5, 5: 27, 6: 27,
        7: 40.5, 8: 40.5, 9: 27, 10: 27,
    }.items():
        ws.get_range(f"{row}:{row}").format.row_height = height

    ws.get_range("C4:C10").format.number_format = "0"
    ws.get_range("F4:G17").format.number_format = "0"

    SpreadsheetFile.export_xlsx(wb).save(output_file)
