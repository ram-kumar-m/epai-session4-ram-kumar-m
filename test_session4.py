import session4
import pytest
import random
import os
import inspect
import re
import math
import cmath
from decimal import Decimal

states = [0, 1, -1]
choice = random.choice(states)
q = session4.Qualean(choice)

README_CONTENT_CHECK_FOR = [
    '__and__',  '__or__', '__repr__', '__str__', '__add__', '__eq__', '__float__',
    '__ge__', '__gt__', '__invertsign__', '__le__', '__lt__', '__mul__', '__sqrt__',
    '__bool__'
]

CHECK_FOR_THINGS_NOT_ALLOWED = []


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_repr():
    assert q.__repr__(
    ) == f'Qualean(({q.val}, {q.uni_val}) -> {format(q.qual,".10f")})', f'Check for repr, found repr {q.__repr__()}'


def test_str():
    assert q.__str__(
    ) == f'This is an object of type Qualean with internal val {format(q.qual,".10f")}', f'Check for str, found repr {q.__repr__()}'


def test_add_two_qualeans():
    states = [0, 1, -1]
    choice = random.choice(states)
    p = session4.Qualean(choice)
    assert (p+q).qual == (p.qual + q.qual), f'Checks if we can add two qualeans'


def test_cant_add_num_with_qualeans():
    with pytest.raises(TypeError):
        q+10


def test_qualean_class_exists_for_states():
    assert type(session4.Qualean(0)) == type(session4.Qualean(1)) == type(
        session4.Qualean(-1)) == session4.Qualean, f'Checks if input value in (0,1,-1)'


def test_for_invalid_inputs():
    with pytest.raises(ValueError):
        session4.Qualean(random.randint(10, 10000)
                         ), f'Ensures ValueError for invalid inputs'


def test_for_derieved_datatype():
    assert (q+session4.Qualean(-1)
            ).val == 'Derieved', f'Makes sure sum of qualeans has a field called "Derieved"'


def test_scalar_multiplication_by_100():
    p = session4.Qualean(0)
    for _ in range(100):
        p += q
    assert p == q*100, f'Checks if q + q + q ... 100 times = 100 * q'


def test_for_eq():
    p = session4.Qualean(0)
    q = session4.Qualean(0)
    assert p == q, f'Checks equality of qualeans'


def test_for_decimal_sqrt():
    if q.qual > 0:
        assert q.__sqrt__() == Decimal.sqrt(
            q.qual), f'returns number of type Decimal if q >0'
    else:
        assert q.__sqrt__() == cmath.sqrt(q.qual), f'returns number of type Complex if q >0'


def test_central_limit_theorum():
    q = session4.Qualean(0)
    for _ in range(1000000):
        q += session4.Qualean(random.choice([0, 1, -1]))
    assert math.isclose(
        q.qual, 0, abs_tol=1000) == True, f'sum of 1 million different qs is very close to zero (using isclose)'


def test_qualean_multiplication():
    p = session4.Qualean(random.choice([0, 1, -1]))

    assert (p*q).qual == p.qual * \
        q.qual, f' Checks if qualean multiplicaton works'


def test_gt():
    p = session4.Qualean(qual=Decimal('0.1234567890'))
    q = session4.Qualean(qual=Decimal('0.1234567899'))

    assert q > p, f'Checks if greater than operator works'


def test_ge():
    p = session4.Qualean(qual=Decimal('0.1234567890'))
    q = session4.Qualean(qual=Decimal('0.1234567899'))

    assert q >= p, f'Checks if greater than or equal to operator works'


def test_le():
    p = session4.Qualean(qual=Decimal('0.1234567890'))
    q = session4.Qualean(qual=Decimal('0.1234567899'))

    assert p <= q, f'Checks if less than operator works'


def test_lt():
    p = session4.Qualean(qual=Decimal('0.1234567890'))
    q = session4.Qualean(qual=Decimal('0.1234567899'))

    assert p < q, f'Checks if less than or equal to operator works'


def test_bool():
    if q.qual != 0:
        assert q.__bool__() == True, 'True for values other than zero'
    else:
        assert q.__bool__() == False, 'False for values of zero'


def test_invertsign():
    assert q.__invertsign__().qual == q.qual*-1, 'Multiplies value by 1'


def test_float_constructor():
    assert q.__float__() == float(q.qual) and isinstance(q.__float__(),
                                                         float), 'Checks if float constructor returns back float object of same value'


def test_and():
    p = session4.Qualean(1)
    q = session4.Qualean(0)
    assert p.__and__(q) == False , 'Testting AND operation between qualeans'


def test_or():
    p = session4.Qualean(1)
    q = session4.Qualean(0)
    assert p.__or__(q) == True, 'Testting OR operation between qualeans'


'''
    '__and__',  '__or__', '__repr__', '__str__', '__add__', '__eq__', '__float__',
     '__ge__', '__gt__', '__invertsign__', '__le__', '__lt__', '__mul__', '__sqrt__',
      '__bool__'
'''
