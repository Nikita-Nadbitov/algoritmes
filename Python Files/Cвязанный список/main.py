from linked_list import Linked_List

def polynomial(a, x, n):
    if a >= n:
        P = Linked_List()
        for i in range(n, -1, -1):
            node = a * x ** i
            P.add(node)
            a -= 1
        return P
    else:
        return ValueError("a>=n")

print(polynomial(12, 2, 10))