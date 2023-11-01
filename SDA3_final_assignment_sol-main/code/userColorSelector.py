import tkinter as tk

def SelectColor(colorList):
    # Define a dictionary to map color names to their corresponding color codes
    colorMapping = {
        "Red": "Red",
        "Blue": "Blue",
        "Yellow": "Yellow",
        "Green": "Green"
    }

    # Function to handle button click
    def onButtonClick(selectedColor):
        selectedColorVar.set(selectedColor)
        root.destroy()
        root.quit()  # Close the app

    # Create the main application window
    root = tk.Tk()
    root.title("Color Selector")

    # Create a StringVar to store the selected color
    selectedColorVar = tk.StringVar()
    selectedColorVar.set("")

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
    return selectedColorVar.get()

if __name__ == "__main__":
    while True:
        colorList = ["Blue","Yellow", "Red", "Green"]
        selectedColor = SelectColor(colorList)
        print("Selected color:", selectedColor)
