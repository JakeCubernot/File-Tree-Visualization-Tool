# File Tree Visualization Tool

This Python tool generates a visual representation of the file structure in a directory and outputs it to a `.txt` file. It automatically updates the file tree using GitHub Actions, which runs the `.py` script and commits the updated file tree to the repository whenever changes are made to the repo.

## Features

- Outputs the file tree as an indented visual structure to a file_tree.txt file.
- Supports any directory to provide a clear overview of its contents.
- Fully automated with GitHub Actions to keep the file tree up-to-date.
- Lightweight and easy to use.

## Requirements

- Python 3.x or higher.

## Installation

1. Clone the repository or download the script file.

   ```bash
   git clone https://github.com/your-username/File-Tree-Visualization-Tool.git

2. Navigate to the project directory.

   ```bash
   cd File-Tree-Visualization-Tool

3. Set up GitHub Actions for automation:

- Ensure the `.github/workflows/update_file_tree.yml` file is present in the repository. This file defines the automation process for running the Python script and committing updates to the `file_tree.txt`.
-  If it doesn't exist, create a `update_file_tree.yml` file in the `.github/workflows/` directory with the following content:

   ```yaml
   name: Update File Tree
   
   on:
     push:
       branches:
         - main
   
   jobs:
     update-file-tree:
       runs-on: ubuntu-latest
   
       steps:
         - name: Checkout code
           uses: actions/checkout@v3
   
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.x'
   
         - name: Install dependencies
           run: |
             python -m pip install --upgrade pip
             pip install -r requirements.txt
   
         - name: Run file tree generator
           run: python file_tree_maker.py
   
         - name: Commit and push changes
           run: |
             git config --global user.name 'github-actions'
             git config --global user.email 'github-actions@github.com'
             git add file_tree.txt
             git commit -m "Update file_tree.txt"
             git push https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/${{ github.repository }}.git

4. Push your changes to the repository to enable GitHub Actions:

   ```bash
   git add .
   git commit -m "Set up File Tree Visualization Tool"
   git push origin main

5. Verify the workflow:

- Go to the "Actions" tab in your GitHub repository to see the workflow running.
- After the first successful run, you should see the `file_tree.txt` file updated in your repository.

## Usage
1. Run the script manually to generate the file tree (if needed):

   ```bash
   python file_tree_maker.py
By default, the tool will generate a file_tree.txt file in the current directory.

2. For automatic updates, make changes to the repository, and the GitHub Actions workflow will automatically update the `file_tree.txt` file.

## Example Output

The generated file_tree.txt file provides a hierarchical view of your directory structure. Example:
   
      Project/
      ├── file_tree_maker.py
      ├── README.md
      ├── requirements.txt
      └── src/
          ├── module1.py
          └── module2.py

# License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
