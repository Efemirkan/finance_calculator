from finance_calculator import numeric_exceptions, string_exception, repayment, compound_interest, simple_interest
import pytest 
from unittest.mock import patch

def test_numeric_exceptions():
    
    with patch('builtins.input', side_effect=['5']):
        assert numeric_exceptions("5") == 5

    with pytest.raises(ValueError):
        with patch('builtins.input', side_effect=['script']):
            numeric_exceptions("script")

def test_string_exception():
    
    with patch('builtins.input', side_effect=["simple"]):
        assert string_exception("simple", "compound") == "simple"
        
    with patch('builtins.input', side_effect=["compound"]):
        assert string_exception("simple", "compound") == "compound"

def test_simple_interest():

    with patch('builtins.input', side_effect=['10000', '5', '5']):
        assert simple_interest(10000, 5, 5) == 12500

def test_compound_interest():

    with patch('builtins.input', side_effect=['10000', '5', '5']):
        assert compound_interest(10000, 5, 5) == 12762.815625000003

def test_repayment():

    with patch('builtins.input', side_effect=['10000', '5', '5']):
        assert repayment(350000, 5, 10) == 3712.2930333676436
