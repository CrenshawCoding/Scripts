from zipfile import ZipFile
import os

files = ['C:\\Users\\leand\\OneDrive\\KeePass\\Passwörter.kdbx']
backup_dir_gdrive = 'C:\\Users\\leand\\Google Drive\\Backup'

for file in files:
    file_dir = os.path.dirname(file)
    base_name = os.path.basename(file)
    zip_name = os.path.splitext(base_name)[0] + '.zip'
    with ZipFile(backup_dir_gdrive + '\\' + zip_name, 'w') as zip_file:
        zip_file.write(file, base_name)
