# Вариант решения 1:
# import os
# from test_data.scripts.reverse import reverse


# current_dir = os.path.dirname(os.path.abspath(__file__))  # путь к файлу теста

# before_txt = open(os.path.join(current_dir, "..", "data", "text_for_reverse.txt")).read()
# result = open(os.path.join(current_dir, "..", "data", "result.txt")).read()


# def test_reverse():
#     reverse_func = reverse(before_txt)
#     assert reverse_func == result


# Вариант решения 2:
from test_data.scripts.reverse import reverse
from pathlib import Path

def get_test_reverse(filename):
    return Path(__file__).parent.parent / "data" / filename


def read_file(filename):
    return get_test_reverse(filename).read_text()


def test_reverse():
    before_txt = read_file('text_for_reverse.txt')
    result = read_file('result.txt')
    reverse_func = reverse(before_txt)
    assert reverse_func == result