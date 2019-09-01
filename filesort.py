# Auto-sort and move files from downloads folder
import os
import shutil


def move_file(raw_path, target_path):
    shutil.move(os.path.join(raw_path, file), os.path.join(target_path, file))


def ensure_dir(directory):
    os.makedirs(directory, exist_ok=True)


def makedir_movetodir(raw_path, target_path):
    ensure_dir(target_path)
    move_file(raw_path, target_path)


class FileDetails:
    def __init__(self, name, extn):
        self.name = name
        self.extn = extn


source_path = 'C:/Users/' + os.getlogin() + '/Downloads'
source_files = os.listdir(source_path)

med = FileDetails("Media", ('.HEIC', '.mp4', '.jpg', '.JPG', '.MOV', '.jpeg', '.png'))
doc = FileDetails('Documents', ('.xlsx', '.docx', '.pdf', '.txt', '.xls'))
inst = FileDetails('Installers', ('.msi', '.exe'))
comp = FileDetails('Zipped', ('.zip', '.rar'))
ebk = FileDetails('Ebooks', ('.epub', '.mobi'))

created_dir = (med.name, doc.name, inst.name, comp.name, ebk.name)

for file in source_files:
    if file.endswith(med.extn):
        destination_path = source_path + '/' + med.name
        makedir_movetodir(source_path, destination_path)
    if file.endswith(doc.extn):
        destination_path = source_path + '/' + doc.name
        makedir_movetodir(source_path, destination_path)
    if file.endswith(inst.extn):
        destination_path = source_path + '/' + inst.name
        makedir_movetodir(source_path, destination_path)
    if file.endswith(comp.extn):
        destination_path = source_path + '/' + comp.name
        makedir_movetodir(source_path, destination_path)
    if file.endswith(ebk.extn):
        destination_path = source_path + '/' + ebk.name
        makedir_movetodir(source_path, destination_path)

source_files = os.listdir(source_path)

for item in created_dir:
    if item in source_files:
        source_files.remove(item)

for item in source_files:
    print(item)
