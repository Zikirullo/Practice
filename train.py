
'''
O-TASK (PYTHON)

Shunday function yozing, u har xil valuelardan iborat array qabul qilsin va List ichidagi sonlar yigindisini hisoblab chiqqan javobni qaytarsin.
MASALAN: calculate_summary([10, "10", {son: 10}, true, 35]) return 45
'''
print("Solution")


def calculate_summary(arr):
    total = 0

    for x in arr:
        if type(x) == int or type(x) == float:
            total = total + x

    return total


result = calculate_summary([100, "10", {"son": 10}, True, 35])
print(result)

'''
M-TASK (PYTHON)

Shunday function yozing, u string qabul qilsin va string palindrom yani togri oqilganda ham, orqasidan oqilganda ham bir hil oqiladigan soz ekanligini aniqlab boolean qiymat qaytarsin.
MASALAN: palindrom_check("dad") return True;  palindrom_check("son") return False;
'''
# print("Solution")


'''
K-TASK (PYTHON)

Shunday function yozing, u string qabul qilsin va string ichidagi eng uzun sozni qaytarsin.
MASALAN: find_longest("I come from Uzbekistan") return "Uzbekistan"
'''
# print('=== Solution ===')


# def palindrom_check(word):
#     reversed_word = word[::-1]

#     return word == reversed_word


# print(palindrom_check("dad"))
# print(palindrom_check("son"))

# def find_longest(s):
#     words = s.split()
#     longest = ""
#     for word in words:
#         if len(word) > len(longest):
#             longest = word
#     return longest


# print(find_longest("I come from Uzbekistan"))

# I-TASK (PYTHON)

# Shunday function tuzing, unga string argument pass bolsin. Function ushbu agrumentdagi digitlarni yangi stringda return qilsin
# MASALAN: get_digits("m14i1t") return qiladi "141"

# Masalaning yechimi
# print("=== Solution ===")

# def get_digits(digit):
#     return ''.join(filter(str.isdigit, digit))

# print(get_digits("m14i321t"))

# '''
# G-TASK (PYTHON)

# Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
# MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.
# '''
# Masalaning yechimi
# print("=== Solution ===")

# def task(arr):
#     return arr.index(max(arr))

# print(task([5, 3, 2, 4, 2, 4, 4, 23]))
