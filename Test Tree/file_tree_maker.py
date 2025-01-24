import os

def print_tree(startpath, prefix="", is_last=False):
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
            print(f"{prefix}{symbol} {entry}/")
            print_tree(entry_path, prefix + next_prefix, is_last=(i == len(entries) - 1))
        else:
            print(f"{prefix}{symbol} {entry}")

def generate_file_tree():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print(f"{os.path.basename(script_dir)}/")
    print_tree(script_dir)

if __name__ == "__main__":
    generate_file_tree()
