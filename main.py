import pandas as pd
import tkinter as tk
from tkinter import filedialog, scrolledtext

# Create a function to display the contents of the CSV file
def display_csv_info():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    
    if file_path:
        df = pd.read_csv(file_path)
        
        # Create a new Tkinter window
        window = tk.Tk()
        window.title('CSV File Info')

        # Create a scrolled text widget to display the CSV contents
        text_widget = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10)
        text_widget.pack()

        # Insert the CSV contents into the text widget
        text_widget.insert(tk.INSERT, df.to_string())

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
