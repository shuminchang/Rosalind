'''
Problem
http://rosalind.info/problems/perm/
'''
n = 6

if n == 2:
    for a in range(1, 3):
        for b in range(1, 3):
                if (a != b):
                    print(a, b)

if n == 3:
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                if (a != b) and (a != c) and \
                   (b != c):
                    print(a, b, c)

if n == 4:
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                for d in range(1, 5):
                                if (a != b) and (a != c) and (a != d) and \
                                   (b != c) and (b != d) and \
                                   (c != d):
                                       print(a, b, c, d)

if n == 5:
    for a in range(1, 6):
        for b in range(1, 6):
            for c in range(1, 6):
                for d in range(1, 6):
                    for e in range(1, 6):
                                if (a != b) and (a != c) and (a != d) and (a != e) and \
                                (b != c) and (b != d) and (b != e) and \
                                (c != d) and (c != e) and \
                                (d != e):
                                    print(a, b, c, d, e)

if n == 6:
    for a in range(1, 7):
        for b in range(1, 7):
            for c in range(1, 7):
                for d in range(1, 7):
                    for e in range(1, 7):
                        for f in range(1, 7):
                                if (a != b) and (a != c) and (a != d) and (a != e) and (a != f) and \
                                (b != c) and (b != d) and (b != e) and (b != f) and \
                                (c != d) and (c != e) and (c != f) and \
                                (d != e) and (d != f) and \
                                (e != f):
                                    print(a, b, c, d, e, f)

if n == 7:
    for a in range(1, 8):
        for b in range(1, 8):
            for c in range(1, 8):
                for d in range(1, 8):
                    for e in range(1, 8):
                        for f in range(1, 8):
                            for g in range(1, 8):
                                if (a != b) and (a != c) and (a != d) and (a != e) and (a != f) and (a != g) and \
                                (b != c) and (b != d) and (b != e) and (b != f) and (b != g) and \
                                (c != d) and (c != e) and (c != f) and (c != g) and \
                                (d != e) and (d != f) and (d != g) and \
                                (e != f) and (e != f) and \
                                (f != g):
                                    print(a, b, c, d, e, f, g)
