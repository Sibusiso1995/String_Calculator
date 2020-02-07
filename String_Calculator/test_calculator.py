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
    assert (add("1\n2,3")) == 6

# handle different delimeters
def test_first_case_delimeter_exception():
    assert(add("//;\n1;2")) == 3

def test_negative_num_exception():
    with pytest.raises(Exception) as negative:
        assert(negative.add("-1,-2,3,4")) == "ERROR: negatives not allowed -1,-2"

def test_greater_than_1000():
    assert(add("//;\n1000,1;2")) == 3

def test_delimeters_of_any_length():
    assert (add("//***\n1***2***3")) == 6

def test_different_delimeters():
    assert(add("//[:D][%]\n1:D2%3")) == 6

def test_different_delimeters():  
    assert(add("//[***][%%%]\n1***2%%%3")) == 6

def test_different_delimeters():    
   assert(add("//[(-_-')][%]\n1(-_-')2%3")) == 6






