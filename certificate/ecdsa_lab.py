import hashlib, binascii
from ecdsa import BadSignatureError
from ecdsa import SigningKey, VerifyingKey

# # SECP256k1 is the Bitcoin elliptic curve
# sk = SigningKey.generate(curve=ecdsa.SECP256k1)
# pem_format = sk.to_pem()
# print(pem_format)
#
# sig = sk.sign(b"message")
# print(sig)
#
# vk = sk.get_verifying_key()
# public_pem = vk.to_pem()
# print(public_pem)
# print(vk)
# print(sk)
# print(vk.verify(sig, b"message")) # True
#
# pem_key = b'-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIMO7jCZLgwSqeVIAJjy9jhAFpMrNE8ZSprm4zJ5jMU4BoAcGBSuBBAAK\noUQDQgAEqVU957Pkic1y3R2lmCgtgDJIzv1fnwaIOf7cASsTeGkvYuAk0UWunCPK\nnm54cp6DfPtKFiI9J28rdxjXYS705g==\n-----END EC PRIVATE KEY-----\n'
# sk = SigningKey.from_pem(pem_key)
# sig = sk.sign(b"message")
#
# print(sig)
# vk = sk.get_verifying_key()
# print(vk.to_pem())

''' generate pair key to doc '''
# sk = SigningKey.generate(curve=ecdsa.SECP256k1)
# vk = sk.get_verifying_key()
# open("private_4.pem","wb").write(sk.to_pem())
# open("public_4.pem","wb").write(vk.to_pem())

val =  "wow"
hash_data = hashlib.sha256(bytes(val, 'utf-8'))
print(hash_data)
hash_hex = hash_data.hexdigest()
hash_bytes = bytes(hash_hex, 'utf-8')
print(hash_bytes)
print(type(hash_bytes))

''' sign and verify '''
sk = SigningKey.from_pem(open("certificate/private_1.pem").read())
sig = sk.sign(hash_bytes)
print(sig)
print(type(sig))
sig = binascii.hexlify(sig)
print(sig)
print(type(sig))
sig = binascii.unhexlify(sig)
print(sig)
print(type(sig))
# open("signature.txt","wb").write(sig)

vk = VerifyingKey.from_pem(open("certificate/public_1.pem").read())
try:
    vk.verify(sig, hash_bytes)
    print ("good signature")
except BadSignatureError:
    print ("BAD SIGNATURE")
