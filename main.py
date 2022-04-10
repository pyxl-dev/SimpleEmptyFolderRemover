from pathlib import Path
import PySimpleGUI as sg


# Remove empty folders
def remove_empty_folders(path: Path):
    for folder in path.rglob("*"):
        if folder.is_dir():
            try:
                folder.rmdir()
            except OSError:
                print(f"{folder} is not empty")


def main():
    layout = [
        [sg.Text("Enter folder path:")],
        [sg.InputText(), sg.FolderBrowse(key="-BROWSE-")],
        [sg.Button("Remove empty folders"), sg.Button("Exit")]
    ]
    window = sg.Window("Remove empty folders", layout)
    while True:
        event, values = window.read()
        if event in [sg.WIN_CLOSED, "Exit"]:
            break
        elif event == "Remove empty folders":
            path = Path(values["-BROWSE-"])
            remove_empty_folders(path)
    window.close()


if __name__ == "__main__":
    main()
