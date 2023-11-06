import pandas as pd
import tkinter as tk
from tkinter import filedialog, scrolledtext

# Create a function to display the contents of the CSV file
def display_csv_info():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    
    if file_path:
        # df = pd.read_csv(file_path)

        df = pd.read_csv(file_path, header=None)  # Read without header
        num_columns = df.shape[1]  # Get the number of columns

        # specific names for columns to prevent "unmatched:" phrase
        column_names = [f"Column{i+1}" for i in range(num_columns)]
        df.columns = column_names  # Assign column names to the DataFrame



        # sub empty cells
        df.fillna('', inplace=True)

        
        # Create a new Tkinter window
        window = tk.Tk()
        window.title('CSV File Info')

        # Create a scrolled text widget to display the CSV contents
        text_widget = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
        text_widget.pack()

        # Insert the CSV contents into the text widget
        # text_widget.insert(tk.INSERT, df.to_string())
        text_widget.insert(tk.INSERT, df.to_string(index=False))  # Omit the index column


        # Start the Tkinter main loop
        window.mainloop()

# Create the main window
window = tk.Tk()
window.title("CSV File Info Viewer")

# Create a button to select and display the CSV file
display_button = tk.Button(window, text="Select and Display CSV File", command=display_csv_info)
display_button.pack()

# Start the Tkinter main loop
window.mainloop()
