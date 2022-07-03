import bitcoin

valid_private_key = False
while not valid_private_key:
    private_key = bitcoin.random_key()
    decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
    valid_private_key = 0 < decoded_private_key < bitcoin.N

print("Private Key (hex) is: " + private_key)
print("Private Key (decimal) is: " + str(decoded_private_key))

wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
print("Private Key (WIF) is: " + str(wif_encoded_private_key))

compressed_private_key = private_key + '01'
print("Private Key Compressed (hex) is: " + str(compressed_private_key))

wif_compressed_private_key = bitcoin.encode_privkey(
    bitcoin.decode_privkey(compressed_private_key, 'hex'), 'wif'
)
print("Private Key (WIF-Compressed) is: " + str(wif_compressed_private_key))

public_key = bitcoin.fast_multiply(bitcoin.G, decoded_private_key)
print("Public Key (x, y) coordinates is: " + str(public_key))

hex_encoded_public_key = bitcoin.encode_pubkey(public_key, 'hex')
print("Public Key (hex) is: " + str(hex_encoded_public_key))

(public_key_x, public_key_y) = public_key
if(public_key_y % 2) == 0:
    compressed_prefix = '02'
else:
    compressed_prefix = '03'
hex_compressed_public_key = compressed_prefix + \
    bitcoin.encode(public_key_x, 16)
print("Compressed Public Key (hex) is: " + str(hex_compressed_public_key))

print("Bitcoin Address (b58check) is: " +
      bitcoin.pubkey_to_address(public_key))

print("Compressed Bitcoin Address (b58check) is: " +
      bitcoin.pubkey_to_address(hex_compressed_public_key))
