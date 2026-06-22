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