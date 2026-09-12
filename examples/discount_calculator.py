"""A small checkout calculation used for a pull request review demo."""


def calculate_total(
    unit_price: float,
    quantity: int,
    discount_percent: float = 0,
) -> float:
    """Return the order total after applying a percentage discount."""
    subtotal = unit_price * quantity
    return subtotal - discount_percent
