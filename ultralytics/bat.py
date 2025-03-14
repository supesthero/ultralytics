import os
import argparse

def create_md_for_py_files(target_dir):
    """
    遍历目录并为每个 .py 文件创建同名 .md 文件
    """
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".py"):
                py_path = os.path.join(root, file)
                md_file = file.replace(".py", ".md")
                md_path = os.path.join(root, md_file)
                
                # 如果 .md 文件不存在则创建
                if not os.path.exists(md_path):
                    try:
                        with open(md_path, 'w', encoding='utf-8') as f:
                            f.write(f"# {file}\n\nThis file documents the purpose of `{file}`.")
                        print(f"Created: {md_path}")
                    except Exception as e:
                        print(f"Error creating {md_path}: {str(e)}")
                else:
                    print(f"Skipped: {md_path} (already exists)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create .md files for all .py files in a directory")
    parser.add_argument("--dir", type=str, default=".", help="Target directory (default: current)")
    args = parser.parse_args()
    
    print(f"Scanning directory: {os.path.abspath(args.dir)}")
    create_md_for_py_files(args.dir)
