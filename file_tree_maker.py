import os 

"""Generates a text-based file tree of a directory."""
def generate_file_tree(startpath, indent = "    "): 
    tree = ""
    for root, dirs, files in os.walk(startpath): 
        level = root.replace(startpath, "").count(os.sep)

        is_last_directory = not any(os.path.join(root, d) for d in dirs)

        prefix = ""
        if level > 0: 
            ancestors = root.split(os.sep)[1:level]
            for i, ancestor in enumerate(ancestors): 
                prefix += "│   " if i < len(ancestors) - 1 \
                or not is_last_directory \
                else "    "

        folder_name = os.path.basename(root) if root != startpath \
        else os.path.basename(startpath)
        tree += f"{prefix}├── {folder_name}/\n"

        for i, f in enumerate(files): 
            sub_prefix = prefix + ("│   " if i < len(files) - 1 else "└── ")
            tree += f"{sub_prefix}{f}\n"
            
    return tree


    #     folder_name = os.path.basename(root) \
    #     if root != startpath else os.path.basename(startpath)

    #     if level == 0:
    #         tree += f"{folder_name}/\n"
    #     else: 
    #         tree += f"{prefix}├── {folder_name}/\n"

    #     subprefix = "│   " * (level + 1)
    #     for i, f in enumerate(files): 
    #         if i == len(files) - 1: 
    #             tree += f"{subprefix}└── {f}\n"
    #         else: 
    #             tree += f"{subprefix}├── {f}\n"

    #     if dirs:
    #         for d in dirs[:-1]:
    #             tree += f"{subprefix}├── {d}/\n"
    #         if dirs[:-1]:
    #             tree += f"{subprefix}└── {dirs[-1]}/\n"

    # return tree


"""Writes the file tree to a text file."""
def write_tree_to_file(tree, filepath): 
    with open(filepath, "w", encoding="utf-8") as file: 
        file.write(tree)


if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_directory, "file_tree.txt")

    tree = generate_file_tree(script_directory)
    write_tree_to_file(tree, output_file)

    print(f"File tree has been updated in: {output_file}")