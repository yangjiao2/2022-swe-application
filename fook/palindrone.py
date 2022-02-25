# Description
# Find all substrings that are palindromes in a given string

# Question Statement

# "aabbaab" should return "a" "a" "a" "a" "b" "b" "b" "aa" "aa" "bb" "aabbaa" "baab" "abba".


def solve(S):
    ans = set()
    N = len(S)
    for center in xrange(2 * N - 1):
        left = center / 2
        right = left + center % 2
        while 0 <= left and right < len(S) and S[left] == S[right]:
            ans.add(S[left : right + 1])
            left -= 1
            right += 1
    return ans


# Time complexity: O(n^2)
# Space complexity: O(1)


def expand(s, start, end):
    output = []
    while s[start] == s[end] and start >= 0 and end < len(s):
        output.append(s[start : end + 1])
        start -= 1
        end += 1

    return output


def allPalindromes(s):  # "aabbaab"
    output = []  # a aa, a, b, bb abba aabbaa, b, a, aa baab, a, b
    for i in range(len(s)):
        # i is center
        output.extend(expand(s, i, i))
        if i < len(s) - 1:
            output.extend(expand(s, i, i + 1))
    return output
