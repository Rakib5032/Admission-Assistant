import os

# ========= CONFIG =========
project_path = r"D:\My projects\test1"

# output file
output_file = os.path.join(project_path, "project_dump.txt")

# folders to ignore
ignore_dirs = {
    "venv",
    "env",
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
    "node_modules",
    "dist",
    "build",
    "site-packages",
    ".ipynb_checkpoints"
}

# only include these file types
allowed_extensions = {
    ".py",
    ".html",
    ".css",
    ".js",
    ".json",
    ".md",
    ".txt",
    ".yml",
    ".yaml"
}


# ========= FUNCTION =========
def should_ignore(path):
    parts = path.split(os.sep)

    for part in parts:
        if part in ignore_dirs:
            return True

    return False


# ========= WRITE OUTPUT =========
with open(output_file, "w", encoding="utf-8") as out:

    out.write("=" * 100 + "\n")
    out.write("PROJECT STRUCTURE\n")
    out.write("=" * 100 + "\n\n")

    # ---------- Folder Structure ----------
    for root, dirs, files in os.walk(project_path):

        # skip ignored folders
        if should_ignore(root):
            continue

        # remove ignored dirs from traversal
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        level = root.replace(project_path, "").count(os.sep)
        indent = "│   " * level

        folder_name = os.path.basename(root)

        if level == 0:
            out.write(f"📁 {folder_name}\n")
        else:
            out.write(f"{indent}📁 {folder_name}\n")

        sub_indent = "│   " * (level + 1)

        for file in files:

            ext = os.path.splitext(file)[1]

            # only show selected files
            if ext in allowed_extensions:
                out.write(f"{sub_indent}📄 {file}\n")

    # ---------- Source Code ----------
    out.write("\n\n")
    out.write("=" * 100 + "\n")
    out.write("SOURCE CODE\n")
    out.write("=" * 100 + "\n\n")

    for root, dirs, files in os.walk(project_path):

        if should_ignore(root):
            continue

        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for file in files:

            ext = os.path.splitext(file)[1]

            # skip unwanted file types
            if ext not in allowed_extensions:
                continue

            file_path = os.path.join(root, file)

            out.write("\n" + "=" * 100 + "\n")
            out.write(f"FILE: {file_path}\n")
            out.write("=" * 100 + "\n\n")

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                    # skip empty files
                    if content.strip():
                        out.write(content)
                    else:
                        out.write("[EMPTY FILE]")

            except Exception as e:
                out.write(f"ERROR READING FILE:\n{e}")

            out.write("\n\n")

print("\n✅ Done!")
print(f"📄 Output saved to:\n{output_file}")