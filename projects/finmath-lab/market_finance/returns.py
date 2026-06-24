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