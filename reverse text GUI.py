import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("Enter Text to reverse: ")],
          [sg.Multiline(default_text='Enter text here!', key='-INPUT-', size=(35, 4))],
          [sg.Multiline(default_text='Reversed text here after clicking OK.', key='-OUTPUT-', size=(35, 4))],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Reverse Text by Tracy V', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update(values['-INPUT-'][::-1])


# Finish up by removing from the screen
window.close()