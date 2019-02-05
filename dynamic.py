# Ask user for input
# import sys
# inp_s = sys.argv[0]
inp_s = input("Please enter string: ")
# Check to see if inp_sing is valid for Longest Repeated Subsequence
nlen = len(inp_s)
if nlen == 0:  # Null string Case
    print(" Invalid Input ")
elif nlen == 1:  # Case for a single Character
    print(" Invalid Input ")
elif nlen == 2 and inp_s[0] != inp_s[1]:  # case for two different characters
    print("Invalid Input")
else:
    def lrs(inp_s):  # Defining LRS function (eliminates same character and same index elements.)

        dypt = [[0 for i in range(nlen + 1)] for j in range(nlen + 1)]

    # Table to perform Dynamic programming( from Longest common subsequence concept)
        for i in range(1, nlen + 1):
            for j in range(1, nlen + 1):
                if inp_s[i - 1] == inp_s[j - 1] and i != j and dypt[i-1][j-1] < (nlen/2)-1:  # match $ different indices
                    dypt[i][j] = 1 + dypt[i - 1][j - 1]
                else:
                    dypt[i][j] = max(dypt[i][j - 1], dypt[i - 1][j])  # No match
        # Initialize result
        results = ''
        # Traverse starting bottom right
        i = nlen
        j = nlen

        while i > 0 and j > 0:
                # cell same as diagonally adjust cell. Add cell char to result
            if dypt[i][j] == dypt[i - 1][j - 1] + 1:
                results += inp_s[i - 1]
                i -= 1
                j -= 1

            # shift to maximum result end.
            elif dypt[i][j] == dypt[i - 1][j]:
                i -= 1
            else:
                j -= 1
        results = ''.join(reversed(results))  # reverse due to bottom traverse
        return results
    print("Output:", lrs(inp_s))  # Call and print LRS function

