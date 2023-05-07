# import numpy as np
import math

# TODO add numpy support later

h = eval(input("What is your step size: "))


def y_prime(x_n, y_n):  # Note: change this return value based on the given problem!!
    return 2 + 5 * x_n + 2 * y_n


def euler_y_n(x_n, y_n):
    return y_n + h * y_prime(x_n, y_n)


def impr_euler_y_n(x_f, x_0, y_0):
    """Give the 'x_f' value that we want for (x_f, y_n)"""
    y_n = y_0
    i = x_0
    print(f"(x_0, y_0): ({x_0}, {y_0})")
    while i < x_f:
        i += h
        x_n = i
        y_pri_imp = euler_y_n(x_n, y_n)
        avg = (y_prime(x_n, y_n) + y_prime(x_n + h, y_pri_imp)) / 2
        y_n = y_n + h * avg
        print(f"(x_{i}, y_{i}): ({x_n}, {y_n})")


def main():
    x_0 = eval(input("What is your x_0? "))
    y_0 = eval(input("What is your y_0? "))
    x_f = eval(input("What is the final x-value? "))

    impr_euler_y_n(x_f, x_0, y_0)


main()
