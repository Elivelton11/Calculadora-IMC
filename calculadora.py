import PySimpleGUI as sg

sg.theme('reddit')

layout = [
[sg.VPush()],
[sg.Text('Peso', justification='center', size=(20,1))],
[sg.Input(key='peso', size=(10,1), justification='center')],
[sg.Text('Altura', justification='center', size=(20,1))],
[sg.Input(key='altura', size=(10,1), justification='center')],
[sg.Button('Calcular')],
[sg.Text('', key='resultado', size=(25,1), justification='center')],
[sg.Text('', key='referencia', size=(25,1), justification='center')],
[sg.VPush()]

]

layout_centered = [[sg.Column(layout, element_justification='center', vertical_alignment='center')]]
janela = sg.Window('Calculadora IMC', layout=layout_centered, size=(260,250))


while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break 
    elif event =='Calcular':
        try: 
            peso = float(values['peso'])
            altura = float(values['altura'])
            resultado = peso / (altura * altura)
            if resultado <17:
                janela['referencia'].update(f'Situação atual: Está muito abaixo do peso')
            elif 17 <= resultado <18.5:
                    janela['referencia'].update(f'Situação: Está abaixo do peso')
            elif 18.5 <= resultado <24.9:
                    janela['referencia'].update(f'Situação: Peso normal')
            elif 25 <= resultado <29.9:
                    janela['referencia'].update(f'Situação: Acima do peso')
            elif 30 <= resultado <34.9:
                    janela['referencia'].update(f'Situação: Obesidade I')
            elif 35 <= resultado <39.9:
                    janela['referencia'].update(f'Situação: Obesidade II(severa)')
            elif resultado >40:
                    janela['referencia'].update(f'Situação: Obesidade III (mórbida)')
            janela['resultado'].update(f'O seu indice de IMC é de: {resultado:.2f}')
        except ValueError: 
            janela['resultado'].update('Por favor, insira valores numéricos válidos.')

janela.close