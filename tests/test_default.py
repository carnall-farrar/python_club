"""test the default function in src"""

from src import f_default
import pytest


def test_f_default():
    """simple test of functionality"""
    assert f_default(100) == 1.0, 'You failed to divide by 100'



