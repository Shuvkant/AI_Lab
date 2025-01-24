
import tkinter as tk
from tkinter import filedialog, messagebox
import pickle
import pandas as pd

# Load the trained model
model_filename = "salary_category_model.pkl"
with open(model_filename, "rb") as file:
    model = pickle.load(file)

# Function to predict salary category based on user input
def predict_salary_category():
    try:
        # Gather user input
        age = int(entry_age.get())
        education = int(entry_education.get())
        experience = int(entry_experience.get())
        hours = int(entry_hours.get())
        
        # Create input DataFrame
        input_data = pd.DataFrame([[age, education, experience, hours]],
                                  columns=["Age", "Education Level", "Years of Experience", "Annual Working Hours"])
        
        # Predict and display result
        prediction = model.predict(input_data)[0]
        category = ["Low", "Medium", "High"][prediction]
        messagebox.showinfo("Prediction", f"Predicted Salary Category: {category}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the GUI window
window = tk.Tk()
window.title("Salary Category Predictor")

# Add input fields
tk.Label(window, text="Age:").grid(row=0, column=0, padx=10, pady=5)
entry_age = tk.Entry(window)
entry_age.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Education Level (1-4):").grid(row=1, column=0, padx=10, pady=5)
entry_education = tk.Entry(window)
entry_education.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Years of Experience:").grid(row=2, column=0, padx=10, pady=5)
entry_experience = tk.Entry(window)
entry_experience.grid(row=2, column=1, padx=10, pady=5)

tk.Label(window, text="Annual Working Hours:").grid(row=3, column=0, padx=10, pady=5)
entry_hours = tk.Entry(window)
entry_hours.grid(row=3, column=1, padx=10, pady=5)

# Add Predict button
predict_button = tk.Button(window, text="Predict", command=predict_salary_category)
predict_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the GUI event loop
window.mainloop()
    