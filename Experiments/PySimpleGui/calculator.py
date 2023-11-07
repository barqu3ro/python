import PySimpleGUI as sg


def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Franklin 14', button_element_size=(4, 2))

    layout = [
        [sg.Push(), sg.Text(
            '',
            font='Franklin 30',
            pad=(10, 20),
            right_click_menu=theme_menu,
            key = "-TEXT-")],
        [sg.Button('Clear', expand_x=True), sg.Button('Enter', expand_x=True)],
        [sg.Button(7), sg.Button(8), sg.Button(9), sg.Button('*')],
        [sg.Button(4), sg.Button(5), sg.Button(6), sg.Button('/')],
        [sg.Button(3), sg.Button(2), sg.Button(1), sg.Button('-')],
        [sg.Button(0, expand_x=True), sg.Button('.'), sg.Button('+')]
    ]
    return sg.Window('Calculator', layout)


theme_menu = ['menu', ['LightGrey1', 'dark', 'Darkgray8', 'random']]
window = create_window('dark')
current_num = []
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in ['1','2','3','4','5','6','7','8','9','0','.']:
        current_num.append(event)
        num_string = ''.join(current_num)
        window['-TEXT-'].update(num_string)
 

    if event in ['-','+','/','*']:
        full_operation.append(''.join(current_num))
        current_num=[]
        full_operation.append(event)
        window['-TEXT-'].update(num_string)

    if event == 'Enter':
        full_operation.append(''.join(current_num))
        result =  eval(''.join(full_operation))
        window['-TEXT-'].update(result)
        full_operation = []

    if event ==  'Clear':
        full_operation = []
        current_num = []
        result = []
        window['-TEXT-'].update('')


window.close()