import ed25519

signing_key, verifying_key = ed25519.create_keypair()
ed25519_public_key = verifying_key.to_bytes().hex()
ed25519_private_key = signing_key.to_seed().hex()

print('ed25519 public key:', ed25519_public_key)
print('ed25519 private key:', ed25519_private_key)

# test
sk = ed25519.SigningKey(ed25519_private_key.encode('ascii'), encoding='hex')
sig = sk.sign(b"something here", encoding="base64")

vk = ed25519.VerifyingKey(ed25519_public_key, encoding='hex')
res = vk.verify(sig, b"something here", encoding='base64')
assert(res == None)
