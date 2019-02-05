
import itertools
# Ask user for input
# import sys
# inp_s = sys.argv[0]
inp_s = input("Please enter String: ")
s=inp_s
# Check to see if inp_sing is valid for Longest Repeated Subsequence
n = len(s)
if n == 0: # Null string Case
    print(" Invalid Input ")
elif n == 1: # Case for a single Character
    print(" Invalid Input ")
elif (n==2 and inp_s[0] != inp_s[1]): # case for two different characters
    print("Invalid Input")
else:
    # use itertools to find all possible combinations of characters in the string
    com=[list(itertools.combinations(s,x)) for x in range(1,len(s)+1)]
    ops=[]
    for s in sum(com,[]):
        st=''.join(s)
        ops.append(st)
        #print (ops)
        storage= {}
        number = [0]*len(s)
    for i in range (len(s)):
        number[i]=i+1
    # use itertools to find indices of all possible combinations of characters in the string
    com=[list(itertools.combinations(number,x)) for x in range(1,len(number)+1)]
    opn=[]
    for s in sum(com,[]):
        st=''.join(map(str,s))
        opn.append(st)
#print (opn) # searching for valid subsequences with different indices.
    for i in range(len(ops)):
        for g in range(i+1,len(ops)):
            if(ops[i]== ops[g]):
                fl=1
                u=opn[i]
                v=opn[g]
                for k in range(len(u)):
                    for l in range(len(v)):
                        if (u[k] == v[l]):
                            fl=0
                if (fl==1): # Creating storage as a dictionary to store valid subsequences
                    if(ops[i] in storage):
                        storage[ops[i]]+=1
                    else:
                        storage[ops[i]]=1
#print(storage)
    length =0
    rep=0

    # Finding subequence in storage which is longest and repeated most
    for h in storage:
        if (len(h)>length):
            if (storage[h]>=rep):
                length = len(h)
                rep=storage[h]
                output=h
    print("Output:",output) # Printing the lonest subsequence


