import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox


def maxmin_normalization(column):
    formulas = {
        "num": "({cell} - 62) / 589",
        "epidemy": "({cell} - 0) / 1",
        "ffmax": "({cell} - 3) / 15",
        "ffm": "({cell} - 1) / 5",
        "tmax": "({cell} - -1) / 40",
        "tmin": "({cell} - -12) / 40",
        "tm": "({cell} - -5) / 30",
        "umax": "({cell} - 22) / 76",
        "umin": "({cell} - 6) / 89",
        "um": "({cell} - 14) / 83",
        "co": "({cell} - 12) / 47",
        "o3": "({cell} - 4) / 157",
        "no2": "({cell} - 25) / 83",
        "so2": "({cell} - 3) / 82",
        "pm10": "({cell} - 12) / 125",
        "pm2.5": "({cell} - 26) / 148",
        "rr": "({cell} - 0) / 39",
    }
    result = []
    for formula, cell in zip(formulas.values(), column):
        value = eval(formula.format(cell=cell))
        result.append(value)
    return result


def on_predict():
    """When user press predict button."""
    table_columns_data = []
    print("Predict ...............")
    for column in columns_entry:
        column_data = []
        for entry in column:
            try:
                cell_data = float(entry.get())
                column_data.append(cell_data)
            except ValueError:
                # msgbox.showerror("Value Error", "Invalid variable value entered!")
                continue
        # calculate maxmin normalization before adding table_columns_data
        normalized_column_data = maxmin_normalization(column_data)
        table_columns_data.append(normalized_column_data)

    print("Table columns data.")
    print(table_columns_data)
    model = load("sdfsdf.cdmnc")
    res = model.predict(table_columns_data)
    predict_result.config(text=predict_result["text"] + " " + str(res))


variables_string = [
    "NUM",
    "Epidemy",
    "FFMax",
    "FFM",
    "TMax",
    "TMin",
    "TM",
    "UMax",
    "UMin",
    "UM",
    "CO",
    "O3",
    "NO2",
    "SO2",
    "PM10",
    "PM2.5",
    "RR",
]

root = tk.Tk()
mainframe = ttk.Frame(root, padding=10)
mainframe.pack(fill=tk.BOTH, expand=True)

# ------------
# Header (row, column label text)
# -------------

xlabel_frame = ttk.Frame(mainframe, relief="solid", padding=(75, 10))
ylabel_frame = ttk.Frame(mainframe, relief="solid", padding=(10, 0))
xlabel_frame.grid(row=0, column=0, columnspan=13)
ylabel_frame.grid(row=1, column=0, sticky="nw", rowspan=17)
for day in range(13):
    label = ttk.Label(xlabel_frame, text=f"Day {day+1}")
    label.grid(row=0, column=day, padx=9)

for index, title in enumerate(variables_string):
    label = ttk.Label(ylabel_frame, text=f"{title}")
    label.grid(row=index, column=0, pady=8)

# ------------
# Table
# -----------
columns_entry = []
table_frame = ttk.Frame(mainframe)
for day in range(13):
    frame = ttk.Frame(table_frame)
    column_entry = []
    for var in range(17):
        textbox = ttk.Entry(frame, width=7)
        textbox.grid(row=var, pady=7)
        column_entry.append(textbox)
    frame.grid(row=0, column=day, padx=2)
    columns_entry.append(column_entry)

table_frame.grid(row=1, column=1, sticky="nw")


actionframe = ttk.Frame(mainframe, padding=(10, 10))
predict_result = ttk.Label(actionframe, text="The volumn of the next day: ")
predict = ttk.Button(actionframe, text="Predict", command=on_predict)
predict.grid(row=0, column=0, sticky="w")
predict_result.grid(row=1, column=0, sticky="w")
actionframe.grid(row=2, column=1)

root.mainloop()
