#BisectionRootFinder
def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        return "Root is not within the given interval"

    iter_count = 0
    while (b-a)/2 > tol and iter_count < max_iter:
        midpoint = (a+b)/2
        if func(midpoint) == 0:
            return midpoint
        elif func(midpoint) * func(a) < 0:
            b = midpoint
        else:
            a = midpoint

        iter_count += 1

    return (a+b)/2

def get_user_function():
    user_func = input("Enter the function in terms of 'x': ")
    return lambda x: eval(user_func)

def get_user_inputs():
    a = float(input("Enter the lower bound of the interval: "))
    b = float(input("Enter the upper bound of the interval: "))
    tol = 1e-6
    max_iter = 100
    return a, b, tol, max_iter

user_func = get_user_function()
a, b, tol, max_iter = get_user_inputs()

root = bisection_method(user_func, a, b, tol, max_iter)

print(f"The root is approximately {root:.6f}")
