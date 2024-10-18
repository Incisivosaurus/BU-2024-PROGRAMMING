binary = "001100010000111001000001"

longest_chain = 0
current_chain_length = 0

for bit in binary:
    if bit == "0":
        current_chain_length += 1
    else:
        if current_chain_length > longest_chain:
            longest_chain = current_chain_length

        current_chain_length = 0

print(f"The length of the longest chain of zeros is: {longest_chain}.")
