import os
from filters import Filter

def get_files_recursive(directory, file_filter):
    """
    Gets all files in a directory recursively
    Directory: folder to check files in, if file is another directory, call this function on that directory
    """
    banned = file_filter.exceptions
    correct_extensions = file_filter.extensions
    contents = os.listdir(directory)
    files = []

    for c in contents:
        if os.path.isfile(os.path.join(directory, c)) and os.path.splitext(c)[-1] in correct_extensions and os.path.splitext(c)[0] not in banned:
            files.append(os.path.join(directory, c))
        elif os.path.isdir(os.path.join(directory, c)) and c + "/" not in banned:
            files += get_files_recursive(os.path.join(directory, c), file_filter)
    return files

file_filter = Filter()


"""
Enter directory for searching
"""
while True:
    search_dir = input("Directory: ")
    if os.path.exists(search_dir):
        break
    print("Directory doesn't exist!")
print("\n")

"""
Enter extensions to add
"""
while True:
    ext = input("Enter extension (end): ")
    if ext == "end":
        break

    file_filter.extensions.append(ext)
print("\n")

"""
Enter files or directories that shouldn't be entered
"""
while True:
    exc = input("Enter exception (end): ")
    if exc == "end":
        break

    file_filter.exceptions.append(exc)
print("\n")

"""
Enter templates
"""
while True:
    template = input("Add template (template/no)?: ")
    if template.lower() == "no":
        break
    file_filter.apply_filter_template(template)

all_files = get_files_recursive(search_dir, file_filter)

line_count_details = []
for file in all_files:
    try:
        with open(file, "r") as f:
            line_count_details.append({"filename": file.split("\\")[-1], "count": len(f.readlines())})
    except Exception as e:
        print(e)

line_count_details.sort(key=lambda x: x["count"])

for d in line_count_details:
    print("%30s%30s" % (d["filename"], d["count"]))

print("%30s%30s" % ("Total", sum([detail["count"] for detail in line_count_details])))
