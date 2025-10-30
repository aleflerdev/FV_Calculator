import pytest
from FutureValueCalculator import future_value


def test_zero_rate_monthly_deposits_sum_linearly():
    """When annual_rate == 0, principal should not grow and monthly deposits sum linearly.

    Example: principal=1000, monthly=100, years=2, compounds_per_year=12
    deposits = 100 * 12 * 2 = 2400, total = 1000 + 2400 = 3400
    """
    principal = 1000
    annual_rate = 0.0
    years = 2
    monthly_deposit = 100
    compounds_per_year = 12

    expected = 1000 + (monthly_deposit * compounds_per_year * years)
    result = future_value(principal, annual_rate, years, monthly_deposit, compounds_per_year)
    assert result == pytest.approx(expected, rel=1e-9)
