import PySimpleGUI as sg
from scraper import *

#choose theme
sg.theme('DarkAmber')

Layout1 = [[sg.Text("Would you like to scan this page?")],
           [sg.Button('Yes'), sg.Button('No')]]

Layout2 = [[sg.Text("Would you like to edit your cover letter for this job posting?")],
           [sg.Button('Yes'), sg.Button('No')]]

# layout3 = [[sg.Text('Paste your link here: '), sg.InputText()],
#            [sg.Text(size=(40,1), key = 'OUTPUT')],
#            [sg.Button('Upload'), sg.Button('Cancel')]]
layout4 = [[sg.Text("Your Cover Letter has successfully changed!")],
           [sg.Button('Awesome!')]]
window1 = sg.Window('cv scanner', Layout1)
window2 = sg.Window('cv scanner', Layout2)
# window3 = sg.Window('cv scanner link', layout3)
window4 = sg.Window('Done!', layout4)

while True:
    event, _ = window1.read()

    if event == sg.WIN_CLOSED or event == 'No':
        break
    else:
        window1.close()
       
        event, _ = window2.read()
        if event == sg.WIN_CLOSED:
            break
        else:
            #grab current url and run it through the web scraper
            window2.close()
            event, values = window4.read()
            if event == sg.WIN_CLOSED or event == 'Awesome':
                break
            # else:
            #     title = find_title(values[0])
            #     print(title)
            #     window3['OUTPUT'].update("the job title is: " + title)
