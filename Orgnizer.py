import os
import sys

folder_dic = {
    'py': 'Python Scripts',
    'js': 'JavaScript Files',
    'jsx': 'React JSX Files',
    'ts': 'TypeScript Files',
    'tsx': 'TypeScript React Files',
    'java': 'Java Source Files',
    'class': 'Java Source Files',
    'cs': 'C# Source Files',
    'cpp': 'C++ Source Files',
    'cxx': 'C++ Source Files',
    'cc': 'C++ Source Files',
    'c': 'C Source Files',
    'h': 'C/C++ Header Files',
    'hpp': 'C++ Header Files',
    'go': 'Go Source Files',
    'rb': 'Ruby Scripts',
    'php': 'PHP Scripts',
    'swift': 'Swift Source Files',
    'sh': 'Shell Scripts',
    'bat': 'Batch Scripts',
    'ps1': 'PowerShell Scripts',
    'json': 'JSON Data Files',
    'yaml': 'YAML Config Files',
    'yml': 'YAML Config Files',
    'xml': 'XML Files',
    'toml': 'TOML Config Files',
    'ini': 'INI Config Files',
    'env': 'Environment Config Files',
    'txt': 'Text Files',
    'md': 'Markdown Files',
    'rst': 'reStructuredText Files',
    'log': 'Log Files',
    'pdf': 'PDF Documents',
    'doc': 'Word Documents',
    'docx': 'Word Documents',
    'xls': 'Excel Spreadsheets',
    'xlsx': 'Excel Spreadsheets',
    'ppt': 'PowerPoint Presentations',
    'pptx': 'PowerPoint Presentations',
    'ipynb': 'Jupyter Notebooks',
    'jar': 'Java Archives',
    'war': 'Web Application Archives',
    'egg': 'Python Eggs',
    'whl': 'Python Wheels',
    'nupkg': 'NuGet Packages',
    'vsix': 'Visual Studio Extensions',
    'exe': 'Executables',
    'dll': 'Dynamic Link Libraries',
    'so': 'Shared Object Libraries',
    'out': 'Compiled Binaries',
    'app': 'macOS Applications',
    'png': 'Images',
    'jpg': 'Images',
    'jpeg': 'Images',
    'gif': 'Animated Images',
    'webp': 'Animated Images',
    'svg': 'Vector Graphics',
    'psd': 'Photoshop Files',
    'ai': 'Illustrator Files',
    'zip': 'ZIP Archives',
    'tar': 'TAR Archives',
    'tgz': 'Compressed TAR Archives',
    'tar.gz': 'Compressed TAR Archives',
    'rar': 'RAR Archives',
    '7z': '7-Zip Archives',
    'sql': 'SQL Files',
    'db': 'Database Files',
    'sqlite': 'SQLite Databases',
    'sqlite3': 'SQLite Databases',
    'pem': 'Certificate Files',
    'crt': 'Certificate Files',
    'key': 'Key Files',
}

def organize(folder_path):
    os.chdir(folder_path)
    files = os.listdir()

    this_file = os.path.basename(sys.argv[0])

    for file in files:
        if os.path.isdir(file):
            continue
        if file == this_file:
            continue
        if '.' not in file:
            folder = "Other Files"
        else:
            _, ext = os.path.splitext(file)
            ext = ext.lstrip(".").lower()
            folder = folder_dic.get(ext, "Other Files")

        os.makedirs(folder, exist_ok=True)

        new_path = os.path.join(folder, file)
        try:
            os.rename(file, new_path)
            print(f"Moved: {file} to {folder}/")
        except Exception as e:
            print(f"Could not move {file}: {e}")

    print("Done organizing files")

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    organize(current_dir)
