"""
Returns module.

This module provides basic functions to calculate simple returns
and logarithmic returns for financial assets.
"""

import math

def simple_return(initial_price: float, final_price: float) -> float:
    """
    Calculate the simple return between two prices of an asset.

    Formula:
        R = (P1 - P0) / P0

    Args:
        initial_price: Initial asset price.
        final_price: Final asset price.

    Returns:
        Simple return as a decimal.

    Example:
        simple_return(100, 110) returns 0.10
    """
    if initial_price <= 0:
        raise ValueError("Initial price must be greater than zero.")

    return (final_price - initial_price) / initial_price


def log_return(initial_price: float, final_price: float) -> float:
    """
    Calculate the logarithmic return between two prices of an asset.

    Formula:
        r = ln(P1 / P0)

    Args:
        initial_price: Initial asset price.
        final_price: Final asset price.

    Returns:
        Logarithmic return as a decimal.

    Example:
        log_return(100, 110) returns approximately 0.0953
    """
    if initial_price <= 0:
        raise ValueError("Initial price must be greater than zero.")

    if final_price <= 0:
        raise ValueError("Final price must be greater than zero.")

    return math.log(final_price / initial_price)

def simple_returns(prices):
    if len(prices) < 2:
        raise ValueError("At least two prices are required.")

    if any(price <= 0 for price in prices):
        raise ValueError("All prices must be greater than zero.")

    return [
        simple_return(prices[i], prices[i + 1])
        for i in range(len(prices) - 1)
    ]

# Calculate logarithmic returns for a list of prices
def log_returns(prices):
    if len(prices) < 2:
        raise ValueError("At least two prices are required.")

    if any(price <= 0 for price in prices):
        raise ValueError("All prices must be greater than zero.")

    return [
        log_return(prices[i], prices[i + 1])
        for i in range(len(prices) - 1)
    ]

# 

def mean_return(returns: list[float]) -> float:
    """
    Calculate the arithmetic mean of a list of returns.

    Formula:
        mean = sum(returns) / n

    Args:
        returns: List of returns.

    Returns:
        Mean return as a decimal.

    Example:
        mean_return([0.05, -0.028571, 0.078431]) returns approximately 0.0333
    """
    if len(returns) == 0:
        raise ValueError("At least one return is required.")

    return sum(returns) / len(returns)

def volatility(returns: list[float], sample: bool = True) -> float:
    """
    Calculate the volatility, or standard deviation, of a list of returns.

    Args:
        returns: List of returns.
        sample: If True, calculate sample standard deviation.
            If False, calculate population standard deviation.

    Returns:
        Volatility as a decimal.

    Formula:
        variance = sum((r - mean)²) / (n - 1) if sample=True
        variance = sum((r - mean)²) / n if sample=False
        volatility = sqrt(variance)

    Example:
        volatility([0.05, -0.028571, 0.078431]) returns approximately 0.0554
    """
    if len(returns) == 0:
        raise ValueError("At least one return is required.")

    if sample and len(returns) < 2:
        raise ValueError("At least two returns are required when sample=True.")

    mean = mean_return(returns)

    denominator = len(returns) - 1 if sample else len(returns)

    variance = sum(
        (r - mean) ** 2
        for r in returns
    ) / denominator

    return math.sqrt(variance)

def cagr(initial_value: float, final_value: float, years: float) -> float:
    """
    Calculate the Compound Annual Growth Rate (CAGR).

    Formula:
        CAGR = (Vf / Vi) ** (1 / n) - 1

    Args:
        initial_value: Initial investment or asset value.
        final_value: Final investment or asset value.
        years: Investment horizon in years.

    Returns:
        Annualized return as a decimal.

    Example:
        cagr(100, 121, 2) returns 0.10
    """
    if initial_value <= 0:
        raise ValueError("Initial value must be greater than zero.")

    if final_value <= 0:
        raise ValueError("Final value must be greater than zero.")

    if years <= 0:
        raise ValueError("The time horizon must be greater than zero.")

    return (final_value / initial_value) ** (1 / years) - 1


def compound_annualized_return(
    returns: list[float],
    periods_per_year: int = 252
) -> float:
    """
    Calculate the compound annualized return from a list of periodic simple returns.

    Formula:
        annualized_return = Π(1 + r_i) ** (periods_per_year / n) - 1

    Args:
        returns: List of periodic simple returns.
        periods_per_year: Number of periods in one year.
            Use 252 for daily trading data, 52 for weekly data,
            12 for monthly data, and 4 for quarterly data.

    Returns:
        Compound annualized return as a decimal.
    """
    if len(returns) == 0:
        raise ValueError("At least one return is required.")

    if periods_per_year <= 0:
        raise ValueError("Periods per year must be greater than zero.")

    if any(r < -1 for r in returns):
        raise ValueError("Returns cannot be less than -100%.")

    total_wealth_factor = 1.0

    for r in returns:
        total_wealth_factor *= 1 + r

    years = len(returns) / periods_per_year

    return total_wealth_factor ** (1 / years) - 1


def annualized_volatility(
    returns: list[float],
    periods_per_year: int = 252,
    sample: bool = True
) -> float:
    """
    Annualize the volatility of periodic returns.

    Formula:
        annualized_volatility = periodic_volatility * sqrt(periods_per_year)

    Args:
        returns: List of periodic returns.
        periods_per_year: Number of periods in one year.
        sample: If True, use sample volatility.

    Returns:
        Annualized volatility as a decimal.
    """
    if periods_per_year <= 0:
        raise ValueError("Periods per year must be greater than zero.")

    periodic_volatility = volatility(returns, sample=sample)

    return periodic_volatility * math.sqrt(periods_per_year)

########################### Main execution block ############################

if __name__ == "__main__":
    p0 = 100
    p1 = 110

    sr = simple_return(p0, p1)
    lr = log_return(p0, p1)

    print("Returns Module")
    print(f"Initial price: {p0}")
    print(f"Final price: {p1}")
    print(f"Simple return: {sr:.4f}")
    print(f"Log return: {lr:.4f}")

    prices = [100, 105, 102, 110]

    simple_returns_result = simple_returns(prices)
    log_returns_result = log_returns(prices)

    mean_simple_return_result = mean_return(simple_returns_result)
    mean_log_return_result = mean_return(log_returns_result)

    print("\nList of Prices:", prices)
    print("Simple Returns:", [f"{r:.4f}" for r in simple_returns_result])
    print("Log Returns:", [f"{r:.4f}" for r in log_returns_result])
    print("Mean Simple Return:", f"{mean_simple_return_result:.4f}")
    print("Mean Log Return:", f"{mean_log_return_result:.4f}")

    volatility_result = volatility(log_returns_result)
    print("Volatility:", f"{volatility_result:.4f}")

cagr_result = cagr(100, 121, 2)
compound_annual_return = compound_annualized_return(simple_returns_result, periods_per_year=252)
annual_vol = annualized_volatility(simple_returns_result, periods_per_year=252)

print("CAGR:", f"{cagr_result:.4f}")
print("Compound Annualized Return:", f"{compound_annual_return:.4f}")
print("Annualized Volatility:", f"{annual_vol:.4f}")
