import tkinter as tk

def SelectColor(colorList):
    # Define the list of color names

    # Define a dictionary to map color names to their corresponding color codes
    colorMapping = {
        "Red": "red",
        "Blue": "blue",
        "Yellow": "yellow",
        "Green": "green"
    }

    # Function to handle button click
    def onButtonClick(selectedColor):
        selectedColor.set(selectedColor)
        root.quit()  # Close the app

    # Create the main application window
    root = tk.Tk()
    root.title("Color Selector")

    # Create a StringVar to store the selected color
    selectedColor = tk.StringVar()
    selectedColor.set("")

    # Create buttons for each color in the colorList list
    for selectedColor in colorList:
        if selectedColor in colorMapping:
            selectedColor = colorMapping[selectedColor]
            button = tk.Button(root, text=selectedColor, background=selectedColor, command=lambda c=selectedColor: onButtonClick(c))
            button.pack()

    # Label to display the selected color
    colorLabel = tk.Label(root, text="Selected Color: ", background="white")
    colorLabel.pack()

    # Label to display the selected color's name
    selectedColorLabel = tk.Label(root, textvariable=str(selectedColor), background="white")
    selectedColorLabel.pack()

    # Start the GUI event loop
    root.mainloop()

    # When the GUI event loop ends, return the selected color
    return selectedColor.get()

if __name__ == "__main__":
    selectedColor = SelectColor()
    print("Selected color:", selectedColor)
