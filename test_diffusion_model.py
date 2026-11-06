import numpy as np
import pytest

from diffusionModel import calculate_stable_time_step

def test_time_test_with_zero_spacing():
    assert calculate_stable_time_step(0.0, 1) == pytest.approx(0.0)