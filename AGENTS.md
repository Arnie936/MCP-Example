# Repository guidance

## Code Review Rules

- Functions that accept a percentage must reject values outside the range from 0 to 100.
- Apply percentage discounts to the full subtotal, not as a fixed currency amount.
- Changes under `examples/` must include tests for the boundary values 0 and 100.
- Focus on correctness and observable behavior. Ignore formatting-only issues.
