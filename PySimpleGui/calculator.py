import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Franklin 14', button_element_size= (4,2))


    layout =[
        [sg.Push(),sg.Text('output', font='Franklin 30', pad=(10,20))],
        [sg.Button('Clear', expand_x=True), sg.Button('Enter', expand_x=True)],
        [sg.Button(7),sg.Button(8),sg.Button(9),sg.Button('*')],
        [sg.Button(4),sg.Button(5),sg.Button(6),sg.Button('/')],
        [sg.Button(3),sg.Button(2),sg.Button(1),sg.Button('-')],
        [sg.Button(0, expand_x = True),sg.Button('.'),sg.Button('+')],
        ]
    return sg.Window('Calculator', layout)

theme_menu = ['menu',['LightGrey1','dark','Darkgray8','random']]
window = create_window('dark')

while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()