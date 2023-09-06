import PySimpleGUI as sg

# Define the layout for the GUI
layout = [
    [sg.Text("Select Risk:")],
    [sg.Combo(['Low', 'Medium', 'High'], key='-RISK-', size=(15, 1))],
    [sg.Text("Select Risk Criteria:")],
    [sg.Combo(['Criteria 1', 'Criteria 2', 'Criteria 3'], key='-CRITERIA-', size=(15, 1))],
    [sg.Button("Submit")]
]

# Create the window
window = sg.Window("Risk Assessment App", layout, resizable=True)

# Cargar las listas para la selección
def cargar_listas():
    return 


# Evento central
def main():
    while True:
        event, values = window.read()

        cargar_listas()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Submit":
            selected_risk = values['-RISK-']
            selected_criteria = values['-CRITERIA-']
            sg.popup(f"Selected Risk: {selected_risk}\nSelected Criteria: {selected_criteria}")

    window.close()

# ejecutar el main
main()