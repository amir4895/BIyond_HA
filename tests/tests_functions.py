import random
import string


def generate_files(number_of_files=1, length=5):
    files_list = []
    for i in range(number_of_files):
        files_list.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=length)))
    return files_list
