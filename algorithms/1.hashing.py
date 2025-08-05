# Hash functions -> Take an input string/message and returns a fixed-size output
# Unique/same inputs produce unique/same outputs
# Since output has fixed length, different outputs might give same output -> Collision


def simple_hash_fx(input_string):
    summation = sum(
        ord(ch) for ch in input_string
    )  # Sum of the unicode values for every char
    return summation % 10  # Limit hash from 0 to 9


print(simple_hash_fx("Hello"))
print(simple_hash_fx("World"))
