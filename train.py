
'''
I-TASK (PYTHON)

Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
MASALAN: get_digits("m14i1t") return qiladi "141"
'''
# Masalaning yechimi
print("=== Solution ===")


def get_digits(digit):
    return ''.join(filter(str.isdigit, digit))


print(get_digits("m14i321t"))


'''
G-TASK (PYTHON)

Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
'''
# Masalaning yechimi
print("=== Solution ===")


def task(arr):
    return arr.index(max(arr))


print(task([5, 3, 2, 4, 2, 4, 4, 23]))
