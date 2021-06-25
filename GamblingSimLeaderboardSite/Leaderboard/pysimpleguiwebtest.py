import PySimpleGUIWeb as sg
import datetime
import os

"""
  Demonstration of running PySimpleGUI code in repl.it!

  This demo program shows all of the PySimpleGUI Elements that are available for use.  New ones are being added daily.

  Now you can run your PySimpleGUI code in these ways:
  1. tkinter
  2. Qt (pyside2)
  3. WxPython
  4. Web Browser (Remi)
  5. repl.it (Remi)

  You can use repl.it to develop, test and share your code.
  If you want to run your GUI on tkinter, then change the import statement to "import PySimpleGUI".  To run it on WxPython, change it to "import PySimpleGUIWx".

  repl.it opens up an entirely new way of demonstrating problems, solutions, bugs, etc, in a way that doesn't require anything but a web browser.  No need to install a GUI package like tkinter.  No need to install Python for that matter.  Just open the repl link and have fun.

"""
print('Starting up...')

sg.ChangeLookAndFeel('LightGreen')  # set the overall color scheme

# The GUI layout
layout = [
    [sg.Text('PySimpleGUIWeb running on the web and in your browser!', size=(60, 1), font=('Comic sans ms', 20),
             text_color='red')],
    [sg.Text('This program has been running for... ', size=(30, 1)), sg.Text('', size=(30, 1), key='_DATE_')],
    [sg.Text('', size=(30, 1), key='_TEXT_')],
    [sg.Input('Single Line Input', do_not_clear=True, enable_events=True, size=(30, 1))],
    [sg.Multiline('Multiline Input', do_not_clear=True, size=(40, 4), enable_events=True)],
    # [sg.MultilineOutput('Multiline Output', size=(40,8),  key='_MULTIOUT_', font='Courier 12')],
    [sg.Output(font='Courier 11', size=(60, 8))],
    [sg.Checkbox('Checkbox 1', enable_events=True, key='_CB1_'),
     sg.Checkbox('Checkbox 2', default=True, enable_events=True, key='_CB2_')],
    [sg.Combo(values=['Combo 1', 'Combo 2', 'Combo 3'], default_value='Combo 2', key='_COMBO_', enable_events=True,
              readonly=False, tooltip='Combo box', disabled=False, size=(12, 1))],
    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(10, 3), enable_events=True, key='_LIST_')],
    [sg.Slider((1, 100), default_value=80, key='_SLIDER_', visible=True, enable_events=True)],
    [sg.Spin(values=(1, 2, 3), initial_value=2, size=(4, 1))],
    [sg.OK(), sg.Button('Exit', button_color=('white', 'red'))]
]

# create the "Window"
window = sg.Window('My PySimpleGUIWeb Window',
                   layout=layout,
                   default_element_size=(12, 1),
                   font='Helvetica 18',
                   )

start_time = datetime.datetime.now()
#  The "Event loop" where all events are read and processed (button clicks, etc)
while True:
    event, values = window.Read(timeout=10)  # read with a timeout of 10 ms
    if event != sg.TIMEOUT_KEY:  # if got a real event, print the info
        print(event, values)
        # also output the information into a scrolling box in the window
        # window.Element('_MULTIOUT_').Update(str(event) + '\n' + str(values), append=True)
    # if the "Exit" button is clicked or window is closed then exit the event loop
    if event in (None, 'Exit'):
        break
    # Output the "uptime" statistic to a text field in the window
    window.Element('_DATE_').Update(str(datetime.datetime.now() - start_time))

# Exiting the program
window.Close()  # be sure and close the window before trying to exit the program
print('Completed shutdown')
