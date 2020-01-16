from string_calc import add
import re
import pytest

def test_empty_string():
    assert(add("")) == 0

def test_one_element():   
    assert(add("1")) == 1
    
def test_two_elements():
    assert(add("1,1")) == 2

# handle multiple integers
def test_more_than_two_elements():
    assert(add("1,2,3,4")) == 10

# handle new lines between integers
def test_delimeter_exception():
    with pytest.raises(Exception):
        assert (add("1\n2,3")) == 6

# handle different delimeters
def test_first_case_delimeter_exception():
    with pytest.raises(Exception):
        assert(add("//;\1;2")) == 3

def test_second_case_delimeter_exception():
    with pytest.raises(Exception):
        assert(add("//4\n142")) == 3

# handle negative numbers
#def test_negative_num():
    #if not re.match("1,2,-3,-4"):
        #raise Exception("negatives not allowed")

def test_negative_num_exception():
    with pytest.raises(Exception) as negative:
        assert(negative.add("-1,-2,3,4")) == "ERROR: negatives not allowed -1,-2"


