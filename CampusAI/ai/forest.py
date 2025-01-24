
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
import joblib

# Load the trained pipeline
pipeline_path = 'trained_pipeline.pkl'
try:
    pipeline = joblib.load(pipeline_path)
except FileNotFoundError:
    messagebox.showerror(
        "Error", "Trained model pipeline not found. Make sure 'trained_pipeline.pkl' exists.")
    exit()

# Define the GUI application


def predict_area():
    try:
        # Collect user input from entry fields
        input_data = {
            'X': int(x_entry.get()),
            'Y': int(y_entry.get()),
            'month': month_entry.get(),
            'day': day_entry.get(),
            'FFMC': float(ffmc_entry.get()),
            'DMC': float(dmc_entry.get()),
            'DC': float(dc_entry.get()),
            'ISI': float(isi_entry.get()),
            'temp': float(temp_entry.get()),
            'RH': int(rh_entry.get()),
            'wind': float(wind_entry.get()),
            'rain': float(rain_entry.get())
        }

        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])

        # Make prediction
        prediction = pipeline.predict(input_df)[0]
        result_label.config(text=f"Predicted Burned Area: {prediction:.2f} ha")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create the main window
root = tk.Tk()
root.title("Forest Fire Burned Area Prediction")

# Create input fields and labels
fields = ["X", "Y", "month", "day", "FFMC", "DMC",
          "DC", "ISI", "temp", "RH", "wind", "rain"]
entries = {}

for idx, field in enumerate(fields):
    label = tk.Label(root, text=field)
    label.grid(row=idx, column=0, padx=10, pady=5, sticky='w')
    entry = tk.Entry(root)
    entry.grid(row=idx, column=1, padx=10, pady=5)
    entries[field] = entry

x_entry = entries['X']
y_entry = entries['Y']
month_entry = entries['month']
day_entry = entries['day']
ffmc_entry = entries['FFMC']
dmc_entry = entries['DMC']
dc_entry = entries['DC']
isi_entry = entries['ISI']
temp_entry = entries['temp']
rh_entry = entries['RH']
wind_entry = entries['wind']
rain_entry = entries['rain']

# Create the predict button
predict_button = tk.Button(root, text="Predict", command=predict_area)
predict_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.grid(row=len(fields) + 1, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
