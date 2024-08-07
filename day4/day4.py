import hashlib

secret_key = "yzbqklnj"
hashes = '00000'
number = 0

while True:

    number += 1
    string_number = str(number)
    new_key = secret_key+string_number
    m = (hashlib.md5(new_key.encode('utf-8')).hexdigest())
    if m.startswith(hashes):
        break

print(new_key)
print(m)
