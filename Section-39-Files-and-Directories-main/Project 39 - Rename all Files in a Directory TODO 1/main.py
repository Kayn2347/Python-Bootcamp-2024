import pathlib


def rename_file(file_name, new_name, file_type):
    current_path = pathlib.Path.cwd()
    seq_num = 0
    for path in current_path.iterdir():
        if path.is_file() and path.suffix == file_type:
            if path.stem == file_name:
                update_name = new_name + file_type
                path.rename(update_name)
                print(f"File name successfully change from {file_name + file_type} to {update_name}")
                return
            elif file_name == "All":
                update_name = new_name + str(seq_num) + file_type
                path.rename(update_name)
                seq_num += 1
                print(f"File name successfully change from {path.name} to {update_name}")
    if file_name != "All":
        print(f"The file {file_name} does not exist!")


rename_file('All', 'test', '.txt')





