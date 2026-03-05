import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_descending_basic():
    # input: 5 3 8 -> descending: 8 5 3
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'\b8\b.*\b5\b.*\b3\b'], lines)


@pytest.mark.T2
def test_descending_ordered():
    # input: 10 1 5 -> descending: 10 5 1
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'\b10\b.*\b5\b.*\b1\b'], lines)


@pytest.mark.T3
def test_descending_negative():
    # input: -2 7 4 -> descending: 7 4 -2
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'\b7\b.*\b4\b.*-2'], lines)


@pytest.mark.T4
def test_descending_equal():
    # input: 3 3 3 -> descending: 3 3 3
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'\b3\b.*\b3\b.*\b3\b'], lines)
