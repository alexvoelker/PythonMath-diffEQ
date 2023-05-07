# import numpy as np
import math

# TODO add numpy support later

h = eval(input("What is your step size: "))


def y_prime(x_n, y_n):  # Note: change this return value based on the given problem!!
    return -4*x_n + y_n**2


def euler_y_n(x_n, y_n):
    return y_n + h * y_prime(x_n, y_n)


def all_euler_y_n(x_f, x_0, y_0):
    """Give the 'x_f' value that we want for (x_f, y_n)"""
    y_n = y_0
    i = x_0
    print(f"\n(x_0, y_0): ({x_0}, {y_0})\n")
    while i < x_f:
        x_n = i
        y_pri = y_prime(x_n, y_n)
        y_new = y_n + h * y_pri
        y_n = y_new
        print(f"(x_{i}, y_{i}): ({x_n}, {y_n})")
        i += h


def main():
    x_0 = eval(input("What is your x_0? "))
    y_0 = eval(input("What is your y_0? "))
    x_f = eval(input("What is the final x-value? "))

    all_euler_y_n(x_f, x_0, y_0)


main()# import numpy as np
import math

# TODO add numpy support later

h = eval(input("What is your step size: "))


def y_prime(x_n, y_n):  # Note: change this return value based on the given problem!!
    return -4*x_n + y_n**2


def euler_y_n(x_n, y_n):
    return y_n + h * y_prime(x_n, y_n)


def all_euler_y_n(x_f, x_0, y_0):
    """Give the 'x_f' value that we want for (x_f, y_n)"""
    y_n = y_0
    i = x_0
    print(f"\n(x_0, y_0): ({x_0}, {y_0})\n")
    while i < x_f:
        x_n = i
        y_pri = y_prime(x_n, y_n)
        y_new = y_n + h * y_pri
        y_n = y_new
        print(f"(x_{i}, y_{i}): ({x_n}, {y_n})")
        i += h


def main():
    x_0 = eval(input("What is your x_0? "))
    y_0 = eval(input("What is your y_0? "))
    x_f = eval(input("What is the final x-value? "))

    all_euler_y_n(x_f, x_0, y_0)


main()
