import PySimpleGUI as sg

"""
Issues(*)/ToDo(-):

"""


sg.theme('DarkRed')

def main():
    Foundation_Column = [
                        [sg.Text("Main Page", font=("Helvetica", 25), justification="center", pad=(10,10), key="-MAIN-")],
                        [sg.Button('View1', size=(10,1), pad=(0,0), key="-VIEW1-")],
                        [sg.Button('View2', size=(10,1), pad=(0,0), key="-VIEW2-")],
                        [sg.Button('View3', size=(10,1), pad=(0,0), key="-VIEW3-")],
                        [sg.Button('Exit', size=(10,1), pad=(0,0), key="-EXIT-")],
            
                        ]
    
    Data_Column =   [   
                    [sg.Text("Data", font=("Helvetica", 25),justification="center", pad=(10,10),)],
                    [sg.Text("Data PlaceHolder\n 1 \n 2 \n 3", font=("Helvetica", 25),justification="center", pad=(10,10),)],
                    ]
    
    Chat_Column =   [   
                    [sg.Text('Output', size=(40, 1))],
                    [sg.Output(size=(75, 15), font=('Helvetica 10'))],
                    [sg.Text('Input', size=(40, 1))],
                    [sg.Multiline(size=(75, 2), enter_submits=False, key='-QUERY-', do_not_clear=False)],
                    [sg.Button('SEND', bind_return_key=True),]
                    ]
    
    layout = [
        [sg.Column(Foundation_Column, background_color="black", pad=(0,0), key="-FOUNDATION-"),
         sg.VSeperator(),
         sg.Column(Data_Column, background_color="black", pad=(0,0), key="-DATA-"),
         sg.VSeperator(),
         sg.Column(Chat_Column, background_color="black", pad=(0,0), key="-CHAT-")],
        [sg.Text("", key="-OUTPUT-")]
    ]
    
    window = sg.Window('Main', layout, resizable=True)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event == '-VIEW1-':
            view1()
        elif event == '-VIEW2-':
            view2()
        elif event == '-VIEW3-':
            view3()
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True)
        if event == 'Exit':
            break
    window.close()
        
def view1():
    
    Chat_Column =   [   
                    [sg.Text('Output', size=(40, 1))],
                    [sg.Output(size=(75, 15), font=('Helvetica 10'))],
                    [sg.Text('Input', size=(40, 1))],
                    [sg.Multiline(size=(75, 2), enter_submits=False, key='-QUERY-', do_not_clear=False)],
                    [sg.Button('SEND', bind_return_key=True),]
                    ]
    
    Data_Column =   [   
                    [sg.Text("Data", font=("Helvetica", 25),justification="center", pad=(10,10),)],
                    [sg.Text("Data PlaceHolder\n 1 \n 2 \n 3", font=("Helvetica", 25),justification="center", pad=(10,10),)],
                    ]
    
    Main_Column =   [
                    [sg.Text("View 1", font=("Helvetica", 25), justification="center", pad=(10,10), key="-VIEW1-")],
                    [sg.Button('Exit', size=(10,1), pad=(0,0), key="-MAIN-")],
                    ]    
    layout = [
            [sg.Column(Main_Column, background_color="black", pad=(0,0), key="-MAIN-"),
             sg.VSeparator(),
             sg.Column(Data_Column, background_color="black", pad=(0,0), key="-DATA-"),
             sg.VSeparator(),
             sg.Column(Chat_Column, background_color="black", pad=(0,0), key="-CHAT-"),]
            ] 
    
    window = sg.Window('View 1', layout, resizable=True)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True)
    window.close()
    
def view2():
    
    Chat_Column =   [   
                    [sg.Text('Output', size=(40, 1))],
                    [sg.Output(size=(75, 15), font=('Helvetica 10'))],
                    [sg.Text('Input', size=(40, 1))],
                    [sg.Multiline(size=(75, 2), enter_submits=False, key='-QUERY-', do_not_clear=False)],
                    [sg.Button('SEND', bind_return_key=True),]
                    ]
    
    Data_Column =   [   
                    [sg.Text("Data", font=("Helvetica", 25),justification="center", pad=(10,10),)],
                    [sg.Text("Data PlaceHolder\n 1 \n 2 \n 3", font=("Helvetica", 25),justification="center", pad=(10,10),)],
                    ]
    
    Main_Column =   [
                    [sg.Text("View 2", font=("Helvetica", 25), justification="center", pad=(10,10), key="-VIEW2-")],
                    [sg.Button('Exit', size=(10,1), pad=(0,0), key="-MAIN-")],
                    ]    
    layout = [
            [sg.Column(Main_Column, background_color="black", pad=(0,0), key="-MAIN-"),
             sg.VSeparator(),
             sg.Column(Data_Column, background_color="black", pad=(0,0), key="-DATA-"),
             sg.VSeparator(),
             sg.Column(Chat_Column, background_color="black", pad=(0,0), key="-CHAT-"),]
            ] 
    
    window = sg.Window('View 2', layout, resizable=True)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True)
    window.close()

def view3():
    
    Chat_Column =   [   
                    [sg.Text('Output', size=(40, 1))],
                    [sg.Output(size=(75, 15), font=('Helvetica 10'))],
                    [sg.Text('Input', size=(40, 1))],
                    [sg.Multiline(size=(75, 2), enter_submits=False, key='-QUERY-', do_not_clear=False)],
                    [sg.Button('SEND', bind_return_key=True),]
                    ]
    
    Data_Column =   [   
                    [sg.Text("Data", font=("Helvetica", 25),justification="center", pad=(10,10),)],
                    [sg.Text("Data PlaceHolder\n 1 \n 2 \n 3", font=("Helvetica", 25),justification="center", pad=(10,10),)],
                    ]
    
    Main_Column =   [
                    [sg.Text("View 3", font=("Helvetica", 25), justification="center", pad=(10,10), key="-VIEW3-")],
                    [sg.Button('Exit', size=(10,1), pad=(0,0), key="-MAIN-")],
                    ]    
    layout = [
            [sg.Column(Main_Column, background_color="black", pad=(0,0), key="-MAIN-"),
             sg.VSeparator(),
             sg.Column(Data_Column, background_color="black", pad=(0,0), key="-DATA-"),
             sg.VSeparator(),
             sg.Column(Chat_Column, background_color="black", pad=(0,0), key="-CHAT-"),]
            ] 
    
    window = sg.Window('View 3', layout, resizable=True)
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True)
    window.close()
    
    
if __name__ == "__main__":
    main()