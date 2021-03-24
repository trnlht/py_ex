import unittest


def compress_string(s):
    i = 0
    res = ""
    while i < len(s):
        cnt = 1

        while (i != len(s) - 1) and s[i] == s[i+1]:
            cnt += 1
            i += 1

        res += s[i] + str(cnt)

        i += 1

    return res if len(res) < len(s) else s

