import os

def print_tree(startpath, prefix="", is_last=False, file=None):
    entries = os.listdir(startpath)
    for i, entry in enumerate(entries):
        entry_path = os.path.join(startpath, entry)
        
        if i == len(entries) - 1:
            next_prefix = "    "
            symbol = "└──"
        else:
            next_prefix = "│   "
            symbol = "├──"
        
        if os.path.isdir(entry_path):
            print(f"{prefix}{symbol} {entry}/", file=file)
            print_tree(entry_path, prefix + next_prefix, is_last=(i == len(entries) - 1), file=file)
        else:
            print(f"{prefix}{symbol} {entry}", file=file)

def generate_file_tree():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(script_dir, "file_tree.txt")
    
    with open(output_file, "w", encoding="utf-8") as file:
        print(f"{os.path.basename(script_dir)}/", file=file)  
        print_tree(script_dir, file=file)

    print(f"File tree has been written to {output_file}")

if __name__ == "__main__":
    generate_file_tree()
