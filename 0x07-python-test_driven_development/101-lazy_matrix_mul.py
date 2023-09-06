#!/usr/bin/python3
""" This is the Matrix multiplication function using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplying  the matrices using numpy

    Args:
        m_a: the list of list
        m_b: the list of list
    Returns:
        The new matrix
    """
    return (np.matmul(m_a, m_b))
