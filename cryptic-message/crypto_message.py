def enigma_light():
#create keys
    keys = 'abcdefghijklmnopqrstuvwxyz'
#autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
    print(keys)
    print(values)
#create two dictionaries
    encrypt_dict = dict(zip(keys, values))
    decrypt_dict = dict(zip(values, keys))

#or we can write two dictionaries in other way
    #encrypt_dict = dict(zip(keys, values))
    #decrypt_dict = {value:key for key, value in encrypt_dict.items()}
#user input 'the message' and mode
    msg = input("Enter the secret message: ")
    mode = input("Crypto mode: encode (e) or decrypt as default: ")
# run encode or decode
    if mode == 'e':
        new_msg = ''.join([encrypt_dict[letter] for letter in msg])
    else:
        new_msg = ''.join([decrypt_dict[letter] for letter in msg])

    return new_msg

print(enigma_light())