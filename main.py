import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme('DarkAmber')

label1 = sg.Text("Select archive")
input1 = sg.Input()
choose_button = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor", layout =[[label1, input1, choose_button],
                                         [label2,input2,choose_button2],
                                         [extract_button, output_label]])

while True:
    try:
        event, values = window.read()
        archivepath = values["archive"]
        dest_dir = values["folder"]
        extract_archive(archivepath, dest_dir)
        window["output"].update(value = f"Successfully extracted to {dest_dir}")
    except AttributeError:
        break


window.read()
window.close()
