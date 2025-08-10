# Encoding:
# How we save text as bits in computers



# Universal Code (Unicode): Every character is mapped to a unique integer.
# You can convert characters to integers and back using ord() and chr().

print(ord("A"))   # Output: 65 — 'A' to Unicode code point
print(chr(65))    # Output: 'A' — Unicode code point to character



# UTF-8 Encoding:
# Converts universal code (Unicode) to bytes (bits)
my_string = "سلام"                             # Some text 
my_string_encoded = my_string.encode("utf-8") # Encode to bytes
result = my_string_encoded.decode("utf-8")    # Decode bytes back to string

print(my_string_encoded)  # Output: b'\xd8\xb3\xd9\x84\xd8\xa7\xd9\x85'
print(result)             # Output: سلام