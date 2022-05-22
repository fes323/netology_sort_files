import os

def count_line(file):
    count_lines = sum(1 for line in open(file, 'r', encoding='utf-8'))
    return count_lines

def find_files_and_create_data(files_folder):
    data = {}
    file_list = []
    for files in os.listdir(files_folder):
        if files.endswith(".txt"):
            file_list.append(files)
    for file in file_list:
        file_path = os.path.join(files_folder, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            file_name = os.path.basename(file_path)
            properties = (count_line(file_path), f.read().strip())
            data[file_name] = properties
    return data

def main(data):
    sorted_list = sorted(data.items(), key=lambda item: item[1])
    sorted_dict = {k: v for k, v in sorted_list}
    with open('result.txt', 'w', encoding='utf-8') as f:
        for k, v in sorted_dict.items():
            f.write(k + '\n')
            f.write(str(v[0]) + '\n')
            f.write(v[1] + '\n')
    return

main(find_files_and_create_data('files'))