# 1.
def get_lines_starting_with(filename, prefix):
    matching_lines = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith(prefix):
                    matching_lines.append(line.strip())
    except FileNotFoundError:
        print("הקובץ לא נמצא.")
    return matching_lines


# 2.
def print_file_with_metadata(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                clean_line = line.rstrip('\n') # הסרת ירידת השורה לצורך חישוב אורך נקי
                line_length = len(clean_line)
                print(f"{line_length}**{clean_line}**")
    except FileNotFoundError:
        print("הקובץ לא נמצא.")


# 3.
def are_files_identical(file1_path, file2_path):
    try:
        with open(file1_path, 'rb') as f1, open(file2_path, 'rb') as f2:
            while True:
                line1 = f1.readline()
                line2 = f2.readline()

                # אם השורות שונות
                if line1 != line2:
                    return False

                # אם הגענו לסוף שני הקבצים בו זמנית
                if not line1: 
                    return True
    except FileNotFoundError:
        return False

