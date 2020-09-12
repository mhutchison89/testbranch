import pytest
import requests
from add import Add
from add import Name
from add import isDivisible

def test_add():
    assert Add(2, 4) == 6

def test_name():
    assert Name('Mark','Hutchison') == 'Mark Hutchison'

def test_divider():
    assert isDivisible(3, 9) == 3

def test_api_sample():
    response = requests.get("http://api.zippopotam.us/us/80504")
    assert response.status_code == 200