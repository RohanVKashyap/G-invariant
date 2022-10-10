import tensorflow as tf


def poly_Z5(x):
    def inv1(a, b):
        return a * b ** 2

    a, b, c, d, e = tf.unstack(x, axis=1)
    q1 = inv1(a, b) + inv1(b, c) + inv1(c, d) + inv1(d, e) + inv1(e, a)
    return q1


def poly_Z10(x):
    def inv1(a, b):
        return a * b ** 2

    a, b, c, d, e, f , g , h, i, j = tf.unstack(x, axis=1)
    q1 = inv1(a, b) + inv1(b, c) + inv1(c, d) + inv1(d, e) + inv1(e, f) + inv1(f, g) + inv1(g, h) \
         + inv1(h, i) + inv1(i, j) + inv1(j, a)
    return q1


def poly_Z5_Z10(x):
    def inv1(a, b):
        return a * b ** 2

    a, b, c, d, e, f , g , h, i, j  = tf.unstack(x, axis=1)
    q1 = inv1(a, b) + inv1(b, c) + inv1(c, d) + inv1(d, e) + inv1(e, a)
    return q1


def poly_Z16(x):
    def inv1(a, b):
        return a * b ** 2

    a, b, c, d, e, f , g , h, i, j, k, l, m, n, o, p = tf.unstack(x, axis=1)
    q1 = inv1(a, b) + inv1(b, c) + inv1(c, d) + inv1(d, e) + inv1(e, f) + inv1(f, g) + inv1(g, h) \
         + inv1(h, i) + inv1(i, j) + inv1(j, k) + inv1(k, l)+ inv1(l, m)+ inv1(m, n) + inv1(n, o) \
         + inv1(o, p) + inv1(p, a)
    return q1


def poly_Z8_Z16(x):
    def inv1(a, b):
        return a * b ** 2

    a, b, c, d, e, f , g , h, i, j, k, l, m, n, o, p = tf.unstack(x, axis=1)
    q1 = inv1(a, b) + inv1(b, c) + inv1(c, d) + inv1(d, e) + inv1(e, f) \
         + inv1(f, g) + inv1(g, h) + inv1(h, a)
    return q1

def poly_Z4_Z16(x):
    def inv1(a, b):
        return a * b ** 2

    a, b, c, d, e, f , g , h, i, j, k, l, m, n, o, p = tf.unstack(x, axis=1)
    q1 = inv1(a, b) + inv1(b, c) + inv1(c, d) + inv1(d, a)
    return q1

def poly_Z2_Z16(x):
    def inv1(a, b):
        return a * b ** 2

    a, b, c, d, e, f , g , h, i, j, k, l, m, n, o, p = tf.unstack(x, axis=1)
    q1 = inv1(a, b) + inv1(b, a)
    return q1


def poly_D8(x):
    def inv1(a, b):
        return a * b ** 2

    a, b, c, d, e = tf.unstack(x, axis=1)
    q1 = inv1(a, b) + inv1(b, c) + inv1(c, d) + inv1(d, a) + \
         inv1(b, a) + inv1(c, b) + inv1(d, c) + inv1(a, d)
    return q1 + e


def poly_A4(x):
    a, b, c, d, e = tf.unstack(x, axis=1)
    q1 = a * b + c * d
    q2 = a * c + b * d
    q3 = a * d + b * c
    q4 = a * b * c + a * b * d + a * c * d + b * c * d

    return q1 + q2 + q3 + q4 + e


def poly_S4(x):
    a, b, c, d, e = tf.unstack(x, axis=1)
    q1 = a * b * c * d
    return q1 + e


def poly_S3xS2(x):
    a, b, c, d, e = tf.unstack(x, axis=1)
    q1 = a*b*c + d + e
    return q1

def poly_S3(x):
    a, b, c, d, e = tf.unstack(x, axis=1)
    q1 = a * b * c + 2 * d + e
    return q1

def poly_Z3(x):
    def inv1(a, b):
        return a * b ** 2

    a, b, c, d, e = tf.unstack(x, axis=1)
    q1 = inv1(a, b) + inv1(b, c) + inv1(c, a) + 2 * d + e
    return q1
