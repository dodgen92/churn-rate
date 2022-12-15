import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Churn Calculator")

# Create the input fields
lost_customers_label = tk.Label(root, text="Lost Customers:")
lost_customers_entry = tk.Entry(root)
total_customers_label = tk.Label(root, text="Total Customers at start:")
total_customers_entry = tk.Entry(root)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate")

# Create the output field
churn_label = tk.Label(root, text="Churn:")
churn_output = tk.Label(root)

# Define the calculate button callback function
def calculate_churn():
    lost_customers = float(lost_customers_entry.get())
    total_customers = float(total_customers_entry.get())
    churn = (lost_customers / total_customers) * 100
    churn_output.config(text=str(churn))

# Set the calculate button's command to the callback function
calculate_button["command"] = calculate_churn

# Position the widgets using the grid layout manager
lost_customers_label.grid(row=0, column=0)
lost_customers_entry.grid(row=0, column=1)
total_customers_label.grid(row=1, column=0)
total_customers_entry.grid(row=1, column=1)
calculate_button.grid(row=2, column=0, columnspan=2)
churn_label.grid(row=3, column=0)
churn_output.grid(row=3, column=1)

# Start the main loop
root.mainloop()
