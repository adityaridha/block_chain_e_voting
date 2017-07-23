import ecdsa
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

''' sign and verify '''
sk = SigningKey.from_pem(open("certificate\private_1.pem").read())
message = open("certificate\message.txt","rb").read()
sig = sk.sign(message)
open("certificate\signature.txt","wb").write(sig)

vk = VerifyingKey.from_pem(open("certificate\public_1.pem").read())
message = open("certificate\message.txt","rb").read()
sig = open("certificate\signature.txt","rb").read()
try:
    vk.verify(sig, message)
    print ("good signature")
except BadSignatureError:
    print ("BAD SIGNATURE")
