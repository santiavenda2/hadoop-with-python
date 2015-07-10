#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""
import sys

print_format = "{0}{1}{2}"


def main(separator='\t'):
    cantidad_total = 0
    suma_total = 0
    for line in sys.stdin:
        suma, cantidad = line.rstrip().split(separator, 1)
        cantidad_total += int(cantidad)
        suma_total += float(suma)

    print print_format.format(suma_total, separator, cantidad_total)


if __name__ == "__main__":
    main()
