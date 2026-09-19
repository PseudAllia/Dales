import pytest
from RLE import run_length_encoding

@pytest.mark.parametrize("text, omit", [("A", False)])
def test_single_no_omit(text, omit):
    assert run_length_encoding(text, omit) == "A1"

@pytest.mark.parametrize("text, omit", [("A", True)])
def test_single_omit(text, omit):
    assert run_length_encoding(text, omit) == "A"

@pytest.mark.parametrize("text", ["AAARRRRGGGGGHH"])
def test_multiple_repetition_no_omit(text):
    assert run_length_encoding(text) == "A3R4G5H2"

@pytest.mark.parametrize("text, omit", [("AAARRRRGGGGGHH", True)])
def test_multiple_repetition_omit(text, omit):
    assert run_length_encoding(text, omit) == "A3R4G5H2"

@pytest.mark.parametrize("text", ["CUTLASSES"])
def test_single_repetition_no_omit(text):
    assert run_length_encoding(text) == "C1U1T1L1A1S2E1S1"

@pytest.mark.parametrize("text, omit", [("CUTLASSES", True)])
def test_single_repetition_omit(text, omit):
    assert run_length_encoding(text, omit) == "CUTLAS2ES"