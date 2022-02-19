# Uses python3
def edit_distance(s, t):
    str1 = s
    str2 = t
    m = len(str1)
    n = len(str2)
    # Create a table to store results of subproblems
    # dp = [[[0]*(n + 1)]*(m + 1)]
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    # print(dp)

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                insert = dp[i][j - 1],  # Insert
                remove = dp[i - 1][j],  # Remove
                replace = dp[i - 1][j - 1]  # Replace
                # print("insert: ", insert, "\n", "remove: ", remove, "\n", "replace: ", replace, "\n")
                dp[i][j] = 1 + min(insert[0], remove[0], replace)

    return dp[m][n]


def edit_distance_slow(s, t):
    # write your code here

    str1 = s
    str2 = t
    m = len(str1)
    n = len(str2)
    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m == 0:
        return n

    # If second string is empty, the only option is to
    # remove all characters of first string
    if n == 0:
        return m

    if str1[m - 1] == str2[n - 1]:
        return edit_distance_slow(str1[: m - 1], str2[:n - 1])

    insert = edit_distance_slow(str1[:m], str2[:n - 1]),  # Insert
    remove = edit_distance_slow(str1[:m - 1], str2[:n]),  # Remove
    replace = edit_distance_slow(str1[:m - 1], str2[:n - 1])  # Replace
    #
    print("insert: ", insert, "\n", "remove: ", remove, "\n", "replace: ", replace, "\n")
    return 1 + min(insert[0], remove[0], replace)


# Driver code

if __name__ == "__main__":
    print(edit_distance(input(), input()))

# str1 = "sunday"
# str2 = "saturday"
# m = len(str1)
# n = len(str2)
# print(editDistDP(str1, str2))
