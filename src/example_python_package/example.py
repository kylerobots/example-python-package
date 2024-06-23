"""Provides an example script for how to use the module."""

import argparse

from . import simple_math


def main() -> None:
    """Run the script."""
    parser = argparse.ArgumentParser(
        description="Demonstrate simple math operations.",
    )
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()
    print(f"{args.a} + {args.b} = {simple_math.add(a=args.a, b=args.b)}")
    print(f"{args.a} - {args.b} = {simple_math.subtract(a=args.a, b=args.b)}")
    print(f"{args.a} * {args.b} = {simple_math.multiply(a=args.a, b=args.b)}")
    print(f"{args.a} / {args.b} = {simple_math.divide(a=args.a, b=args.b)}")


if __name__ == "__main__":
    main()
