import tkinter as tk

def select_color(colorList):
    # Define the list of color names

    # Define a dictionary to map color names to their corresponding color codes
    color_mapping = {
        "Red": "red",
        "Blue": "blue",
        "Yellow": "yellow",
        "Green": "green"
    }

    # Function to handle button click
    def on_button_click(color_name):
        selected_color.set(color_name)
        root.quit()  # Close the app

    # Create the main application window
    root = tk.Tk()
    root.title("Color Selector")

    # Create a StringVar to store the selected color
    selected_color = tk.StringVar()
    selected_color.set("")

    # Create buttons for each color in the colorList list
    for color_name in colorList:
        if color_name in color_mapping:
            color_code = color_mapping[color_name]
            button = tk.Button(root, text=color_name, background=color_code, command=lambda c=color_name: on_button_click(c))
            button.pack()

    # Label to display the selected color
    color_label = tk.Label(root, text="Selected Color: ", background="white")
    color_label.pack()

    # Label to display the selected color's name
    color_name_label = tk.Label(root, textvariable=selected_color, background="white")
    color_name_label.pack()

    # Start the GUI event loop
    root.mainloop()

    # When the GUI event loop ends, return the selected color
    return selected_color.get()

if __name__ == "__main__":
    selected_color = select_color()
    print("Selected color:", selected_color)
