import tkinter as tk
import ttkbootstrap as ttk
from PIL import ImageTk, Image
import os


def search_files(folder_path, keyword):
    results = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if keyword.lower() in file.lower():
                results.append(os.path.join(root, file))
    return results


def run_file_finder(folder_path, keyword):
    if keyword:
        search_results = search_files(folder_path, keyword)
    else :
        result_text.delete(1.0, tk.END) 
        result_text.insert(tk.END, "*** Please enter a keyword ***")

    if os.path.exists(folder_path) :
        if search_results:
            result_text.delete(1.0, tk.END) 
            result_text.insert(tk.END, "Search results:\n")
            for result in search_results:
                result_text.insert(tk.END, result + "\n")
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "No matching files found.")

    else: 
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "*** Please enter a valide path ***")




if __name__ == "__main__":

    # Window
    window = ttk.Window(themename='flatly')
    window.title('Moteur de recherche')
    window.geometry('800x700')
    window.resizable(True, True) 


    # Logo frame
    logo_frame = tk.Frame(window, width=800, height=70)
    logo_frame.grid(row=0, column=0)
    logo_frame.pack_propagate(False)
    logo_widget = tk.Label(logo_frame, text='File Finder', font=("Times", 30) )
    logo_widget.pack()


    # Image
    # script_dir = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    # image_path = os.path.join(script_dir, "folder.png")
    # original_image = Image.open('folder.png')

    # desired_size = (100, 100) 
    # resized_image = original_image.resize(desired_size)
    # logo_img = ImageTk.PhotoImage(resized_image)

    # logo_widget = tk.Label(logo_frame, image=logo_img)
    # logo_widget.image = logo_img
    # logo_widget.pack()


    # Input frame
    input_frame = ttk.Frame(master=window)

    label_path = ttk.Label(master=input_frame, text='Enter the path :')
    entry_path = ttk.Entry(master=input_frame)

    label_file = ttk.Label(master=input_frame, text='Enter the file name :')
    entry_file = ttk.Entry(master=input_frame)


    button = ttk.Button(
        master=input_frame, 
        text='Recherche',
        command=lambda: run_file_finder(entry_path.get(), entry_file.get())
    )

    label_path.grid(row=0, column=0, padx=5, pady=5)
    entry_path.grid(row=0, column=1, padx=5, pady=5)
    label_file.grid(row=1, column=0, padx=5, pady=5)
    entry_file.grid(row=1, column=1, padx=5, pady=5)
    button.grid(row=3, column=0, columnspan=2, padx=10, pady=15, sticky='nsew')
    input_frame.grid(row=1, column=0)


    # Output frame
    output_frame = ttk.Frame(master=window)
    output_frame.grid(row=3, column=0)

    result_text = tk.Text(output_frame, height=25, width=100, wrap=tk.WORD)
    result_text.pack(fill=tk.BOTH, expand=True)

    window.mainloop()


# creer le fichier executable : lire la ligne suivante dans le cmd
# C:\Users\Charles_tour\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\pyinstaller.exe --onefile --noconsole file_finder.py