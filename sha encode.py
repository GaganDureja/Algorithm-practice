#Link: https://edabit.com/challenge/haaS4SBv42N3btcg5



from hashlib import sha256
def get_sha256_hash(txt):
    return sha256(txt.encode()).hexdigest()

    

print(get_sha256_hash("password123"))