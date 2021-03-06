# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:44:21 2020

@author: USER
"""

import PySimpleGUI as sg
import numpy as np
from pickle import load

# ADD TITLE COLOUR ,title_color='white'
sg.theme('DefaultNoMoreNagging')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Developed by Hoang Dac Nguyen, James Michael LaFave, Young Joo Lee, and Myoungsu Shin')],
            [sg.Text('Ulsan National Institute of Science and Technology (UNIST)')],
            [sg.Text('Ulsan, South Korea')],
            [sg.Text('Email: nguyenhoangkt712@unist.ac.kr')],
            #[sg.Text('Input parameters')],
              
            [sg.Frame(layout=[
            [sg.Text('S1s',size=(10, 1)),sg.InputText(key='-f1-'),sg.Text('g')],
            [sg.Text('S2s',size=(10, 1)), sg.InputText(key='-f2-'),sg.Text('g')],
            [sg.Text('S3s',size=(10, 1)), sg.InputText(key='-f3-'),sg.Text('g')],
            [sg.Text('S4s',size=(10, 1)), sg.InputText(key='-f4-'),sg.Text('g')],
            [sg.Text('S5s',size=(10, 1)), sg.InputText(key='-f5-'),sg.Text('g')],
            [sg.Text('T1',size=(10, 1)), sg.InputText(key='-f6-'),sg.Text('s')],
            [sg.Text('T2',size=(10, 1)), sg.InputText(key='-f7-'),sg.Text('s')],
            [sg.Text('T3',size=(10, 1)),sg.InputText(key='-f8-'),sg.Text('s')]],title='Input parameters')],
            [sg.Frame(layout=[   
            [sg.Text('Damage state',size=(10, 1)), sg.InputText(key='-OP-',size=(48, 1))]],title='Output')],
            [sg.Button('Predict'),sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('ENHANCED RAPID DAMAGE-STATE ASSESSMENT OF STEEL MOMENT FRAMES', layout)

filename = 'BestModel_RF.sav'
loaded_model = load(open(filename, 'rb'))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    #window['-OP-'].update('Please fill all the input parameters')
    if event == 'Predict':
        #window['-OP-'].update(values[0])
        #break
        if values['-f1-'] == '' or values['-f2-'] == '' or values['-f3-'] == '' or values['-f4-'] == '' or values['-f5-'] == '' or values['-f6-'] == '' or values['-f7-'] == '' or values['-f8-'] == '':

            window['-OP-'].update('Please fill all the input parameters')

        else:

            x_test=np.array([[float(values['-f1-']),float(values['-f2-']), float(values['-f3-']),float(values['-f4-']),float(values['-f5-']),values['-f6-'],values['-f7-'],values['-f8-']]])
            y_pred_disp = loaded_model.predict(x_test)
            if y_pred_disp == 1:
                window['-OP-'].update(("Green tag"))
            elif y_pred_disp == 2:
                window['-OP-'].update(("Yellow tag"))
            else:
                window['-OP-'].update(("Red tag"))   
                    
            

window.close()
