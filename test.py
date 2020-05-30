def print_star(*coeff):
    coeffs = coeff
    print("coeff: *{!r}.".format(coeff))

l = []
print_star(l)
l = [1]
print_star(l)
l = [1, 2]
print_star(l)