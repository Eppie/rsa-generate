from Crypto.PublicKey import RSA

KEYLENGTH = 2048

RSAkey = RSA.generate(KEYLENGTH)

print "Modulus: " + str(getattr(RSAkey.key, 'n'))
print "Public exponent: " + str(getattr(RSAkey.key, 'e'))
print "Private exponent: " + str(getattr(RSAkey.key, 'd'))
print "Key length: " + str(KEYLENGTH)

print RSAkey.publickey().exportKey()
print RSAkey.exportKey()
