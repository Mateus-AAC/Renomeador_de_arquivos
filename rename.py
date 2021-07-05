import re
import os
import shutil

print("//////////////////////////////////")
print("/                                /")
print("/          renomeador            /")
print("/                                /")
print("//////////////////////////////////")
main_folder = input(r'coloque o diretorio:')
os.system('cls')


def rename_file(file):
    file_name, file_extension = os.path.splitext(file)
    file_name_numbers = re.findall(r'\d+', file_name)

    if not file_name_numbers:
        return file

    file_name_numbers = file_name_numbers[0].zfill(4)

    return f'{file_name_numbers}{file_extension}'


def file_loop(root, dirs, files):
    for file in files:
        if not re.search(r'\.$', file):
            continue

        new_file_name = rename_file(file)
        old_file_full_path = os.path.join(root, file)
        new_file_full_path = os.path.join(root, new_file_name)

        print(f'Renomeado"{file}" para "{new_file_name}"')
        shutil.move(old_file_full_path, new_file_full_path)


def main_loop():
    for root, dirs, files in os.walk(main_folder):
        file_loop(root, dirs, files)


if __name__ == '__main__':
    main_loop()