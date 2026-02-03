# 1.

# א. זיכרון נדיף (RAM) מאבד את תוכנו עם ניתוק החשמל, בעוד זיכרון לא נדיף שומר על המידע גם ללא זרם חשמלי.
# ב. דוגמאות: כונן קשיח (HDD), כונן SSD, דיסק און קי (Flash Drive), כרטיס SD.
# ג. מתודת close משחררת את המשאבים שהוקצו לקובץ במערכת ההפעלה ומבטיחה שכל המידע שנכתב בזיכרון הזמני אכן נשמר פיזית בדיסק.
# ד. הבדלים:
# 'r': קריאה בלבד (שגיאה אם הקובץ לא קיים).
# 'w': כתיבה (דורס את תוכן הקובץ הקיים או יוצר חדש).
# 'a': הוספה (Append) - כותב לסוף הקובץ מבלי למחוק את תוכנו.

# 2.
with open("example.txt", "w") as f:
    f.write("Hello, World!")

# 3.
def read_50_chars(filename):
    with open(filename, "r") as f:
        return f.read(50)

# 4.
def safe_write(filename, text):
    try:
        with open(filename, "w") as f:
            f.write(text)
        return True
    except Exception:
        return False

# קריאות לפונקציה
print(safe_write("success.txt", "It works!"))
print(safe_write("invalid_folder/fail.txt", "Error!"))

# 5.
def find_lines_starting_with(filename, prefix):
    results = []
    with open(filename, "r") as f:
        for line in f:
            if line.startswith(prefix):
                results.append(line.strip())
    return results

# 6.
def are_files_identical(file1, file2):
    try:
        with open(file1, "rb") as f1, open(file2, "rb") as f2:
            return f1.read() == f2.read()
    except FileNotFoundError:
        return False

