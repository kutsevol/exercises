# coding: utf-8
# Task description

"""
A zero-indexed array A consisting of N integers is given. Rotation of the array
means that each element is shifted right by one index, and the last element of
the array is also moved to the first place.

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]. The
goal is to rotate array A K times; that is, each element of A will be shifted to
the right by K indexes.

Write a function:

def solution(A, K)

that, given a zero-indexed array A consisting of N integers and an integer K,
returns the array A rotated K times.

For example, given array A = [3, 8, 9, 7, 6] and K = 3, the function should
return [9, 7, 6, 3, 8].

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000...1,000].
In your solution, focus on correctness. The performance of your solution will
not be the focus of the assessment.
"""

# Code

def solution(A, K):
    return A[-K%len(A):] + A[:-K%len(A)] if A and K else A

# Verification

if __name__ == "__main__":
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
    assert solution([1, 2 ,3], 5) == [2, 3, 1]
    assert solution([], 4) == []
    assert solution([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert solution([2, 3], 2) == [2, 3]
    assert solution([5, -1000], 1) == [-1000, 5]
