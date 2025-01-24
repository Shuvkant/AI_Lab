import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

# Load the pretrained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Function to make predictions
def predict_species():
    try:
        # Get user inputs
        inputs = [
            float(entry_sepal_length.get()),
            float(entry_sepal_width.get()),
            float(entry_petal_length.get()),
            float(entry_petal_width.get())
        ]
        inputs = np.array(inputs).reshape(1, -1)

        # Predict using the loaded model
        prediction = model.predict(inputs)
        result = prediction[0]
        messagebox.showinfo("Prediction", f"The predicted species is: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("Iris Flower Predictor")

# Input Fields
tk.Label(root, text="Sepal Length (cm):").grid(row=0, column=0, padx=10, pady=5)
entry_sepal_length = tk.Entry(root)
entry_sepal_length.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Sepal Width (cm):").grid(row=1, column=0, padx=10, pady=5)
entry_sepal_width = tk.Entry(root)
entry_sepal_width.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Petal Length (cm):").grid(row=2, column=0, padx=10, pady=5)
entry_petal_length = tk.Entry(root)
entry_petal_length.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Petal Width (cm):").grid(row=3, column=0, padx=10, pady=5)
entry_petal_width = tk.Entry(root)
entry_petal_width.grid(row=3, column=1, padx=10, pady=5)

# Predict Button
predict_button = tk.Button(root, text="Predict Species", command=predict_species)
predict_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
