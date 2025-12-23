import math

import pytest

from app.calculator import (MortgageInput, monthly_payment, overpayment,
                            total_payment)


def test_monthly_payment_zero_rate():
    m = MortgageInput(principal=1200000, annual_rate=0.0, years=10)
    mp = monthly_payment(m)
    assert mp == pytest.approx(10000.0)


def test_monthly_payment_positive_rate():
    m = MortgageInput(principal=1000000, annual_rate=10.0, years=20)
    mp = monthly_payment(m)
    assert mp == pytest.approx(9650, rel=0.01)


def test_total_and_overpayment_consistency():
    m = MortgageInput(principal=500000, annual_rate=8.0, years=15)
    tp = total_payment(m)
    op = overpayment(m)
    assert math.isclose(tp - m.principal, op, rel_tol=1e-6)


def test_invalid_input_raises():
    with pytest.raises(ValueError):
        _ = monthly_payment(
            MortgageInput(
                principal=0,
                annual_rate=10,
                years=10))
