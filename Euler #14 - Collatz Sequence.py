'''The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
Using the rule above and starting with , we generate the following sequence:

It can be seen that this sequence (starting at  and finishing at ) contains  terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at .

Which starting number, under one million, produces the longest chain?
'''

def sequence_Collatz(upper):
    max_seq = 0
    longest = 0
    for i in range(upper, 0, -1):
        n = i
        seq = 1
        while n != 1:
            seq += 1
            if n % 2 == 0:
                n = n//2
            else:
                n = 3*n + 1
        if seq > max_seq:
            max_seq = seq
            longest = i
    return(max_seq, longest)

print(sequence_Collatz(1000000))
# Returns (525, 837799) -> Correct
            