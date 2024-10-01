import pathlib


# TODO - 1 Rename one file
def rename_file(file_name, new_name, file_type):
    current_path = pathlib.Path.cwd()
    seq_num = 0
    for item in current_path.iterdir():
        if item.is_file() and item.suffix == file_type:
            if item.stem == file_name:
                update_name = new_name + file_type
                item.rename(update_name)
                print(f"File name is successfully changed from {file_name+file_type} to {update_name}")
                return
            # TODO 2 Rename all files' names
            elif file_name == "All":
                update_name = new_name + str(seq_num) + file_type
                item.rename(update_name)
                seq_num += 1
                print(f"File name is successfully changed from {item.name} to {update_name}")
    if file_name != "All":
        print(f"The file {file_name+file_type} does not exist!")


rename_file('All', 'sample', '.txt')