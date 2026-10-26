import pytest

from app import calculate_total


def test_no_code():
    assert calculate_total(50) == 50


def test_vday_code():
    assert calculate_total(50, "VDAY20") == 40


def test_unknown_code():
    assert calculate_total(50, "FAKE") == 50


def test_negative_subtotal():
    with pytest.raises(ValueError):
        calculate_total(-5)
