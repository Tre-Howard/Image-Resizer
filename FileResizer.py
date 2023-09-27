import PySimpleGUI as sg
from PIL import Image
import os

# Define the layout
layout = [
    [sg.Text('Select image files:')],
    [sg.Input(key='-FILES-', enable_events=True), sg.FilesBrowse()],
    [sg.Text('Enter the desired pixel size:')],
    [sg.Input(key='-WIDTH-', size=(6, 1)), sg.Text('x'), sg.Input(key='-HEIGHT-', size=(6, 1)),
     sg.Button('1280x720'), sg.Button('1920x1080'), sg.Button('2560x1440'), sg.Button('3840x2160')],
    [sg.Button('Resize Images')]
]

# Create the window
window = sg.Window('Image Resizer', layout)

# Event loop to process events
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Resize Images':
        # Get the selected file paths and desired sizes from the input fields
        file_paths = values['-FILES-'].split(';')
        width = int(values['-WIDTH-'])
        height = int(values['-HEIGHT-'])

        for file_path in file_paths:
            # Open the image file
            image = Image.open(file_path)

            # Resize the image to the desired size
            new_size = (width, height)
            resized_image = image.resize(new_size)

            # Save As dialog to choose the output file path
            save_path = sg.popup_get_file('Save As', save_as=True, default_extension=".jpg")

            if save_path:
                # Save the resized image with the chosen file path
                resized_image.save(save_path)
                sg.popup(f"Image resized and saved as {os.path.basename(save_path)}")

    if event == '1280x720':
        window['-WIDTH-'].update(1280)
        window['-HEIGHT-'].update(720)
    elif event == '1920x1080':
        window['-WIDTH-'].update(1920)
        window['-HEIGHT-'].update(1080)
    elif event == '2560x1440':
        window['-WIDTH-'].update(2560)
        window['-HEIGHT-'].update(1440)
    elif event == '3840x2160':
        window['-WIDTH-'].update(3840)
        window['-HEIGHT-'].update(2160)

# Close the window
window.close()
