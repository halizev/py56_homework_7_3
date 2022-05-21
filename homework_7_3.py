import os


def files_merge_txt():
    files_list = []
    index_list = []

    for file in os.listdir('txt_files/'):
        files_list.append(file)

    for file_name in files_list:
        full_path = os.path.join('txt_files/', file_name)
        with open(full_path, encoding='utf8') as f:
            file_content = f.read()
            file_dict = dict()
            file_dict['name'] = file_name
            file_dict['lines_amount'] = len(file_content.split('\n'))
            file_dict['content'] = file_content
            index_list.append(file_dict)

    def sort_lines_amount(sorting_list):
        return sorting_list['lines_amount']

    sorted_list = sorted(index_list, key=sort_lines_amount)

    with open('merged_files.txt', mode="w", encoding='utf8') as f:
        for file in sorted_list:
            f.write(f"{file['name']}\n")
            f.write(f"{file['lines_amount']}\n")
            f.write(f"{file['content']}\n")


files_merge_txt()
