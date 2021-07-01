'''
calculatorGUI.py
'''
import PySimpleGUI as sg

# 공통 속성
bw : dict = {'size':(6,2), 'font':('D2Coding', 24), 'button_color':("white","#7a7a7b")}
bt : dict = {'size':(6,2), 'font':('D2Coding', 24), 'button_color':("white","#39393a")}
bo : dict = {'size':(6,2), 'font':('D2Coding', 24), 'button_color':("white","#ECA527")}
b0 : dict = {'size':(17,2), 'font':('D2Coding', 24), 'button_color':("white","#7a7a7b")}

# layout 구성
layout: list = [
    # [sg.Text('CalculatorGUI', size=(50,1), justification='right', background_color="black",
    #     text_color='white', font=('D2Coding', 14, 'bold'))],
    [sg.Text('0', size=(16,1), justification='right', background_color='#242425', text_color='white',
        font=('D2Coding',60), relief='flat', key="_DISPLAY_")],
    [sg.Button('AC', **bt), sg.Button('+/-', **bt), sg.Button('%', **bt), sg.Button('/', **bo)],
    [sg.Button('7', **bw), sg.Button('8', **bw), sg.Button('9', **bw), sg.Button('*', **bo)],
    [sg.Button('4', **bw), sg.Button('5', **bw), sg.Button('6', **bw), sg.Button('-', **bo)],
    [sg.Button('1', **bw), sg.Button('2', **bw), sg.Button('3', **bw), sg.Button('+', **bo)],
    [sg.Button('0', **b0), sg.Button('.', **bw), sg.Button('=', **bo, bind_return_key=True)],
]

window: object = sg.Window(title='CalculatorGUI',layout=layout, element_justification='right', margins=(1,1), background_color="#242425", return_keyboard_events=True)


# 계산기 함수
var : dict = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}

# 소수
def format_number() -> float:
    return float(''.join(var['front']) + '.' + ''.join(var['back']))


def update_display(display_value: str):
    try:
        window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
    except:
        window['_DISPLAY_'].update(value=display_value)


# 이벤트 체크
def number_click(event: str):
    global var
    if var['decimal']:
        var['back'].append(event)
    else:
        var['front'].append(event)
    update_display(format_number())


def clear_click():
    # AC
    global var
    var['front'].clear()
    var['back'].clear()
    var['decimal'] = False


def operator_click(event: str):
    # +, -, /, *
    global var
    var['operator'] = event
    try:
        var['x_val'] = format_number()
    except:
        var['x_val'] = var['result']
    clear_click()




def calculate_click():
    global var
    var['y_val'] = format_number()
    try:
        var['result'] = eval(str(var['x_val']) + var['operator'] + str(var['y_val']))
        update_display(var['result'])
        clear_click()
    except:
        update_display("ERROR! DIV/0")
        clear_click()


# main loop
while True:
    event, values = window.read()
    print(event)
    if event is None:
        break
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        number_click(event)
    if event in ['Escape:27', 'AC']:
        clear_click()
        update_display(0.0)
        var['result'] = 0.0
    if event in ['+', '-', '*', '/']:
        operator_click(event)
    if event == '=':
        calculate_click()
    if event == '.':
        var['decimal'] = True
    if event == '%':
        update_display(var['result'] / 100.0)
    if event == '+/-':
        update_display(var['result'] * -1)




