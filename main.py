import hashlib

def calculate_md5(text):
    """Calculates the MD5 hash of the given text."""
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest()

def calculate_sha256(text):
    """Calculates the SHA-256 hash of the given text."""
    sha256_hash = hashlib.sha256()
    sha256_hash.update(text.encode('utf-8'))
    return sha256_hash.hexdigest()

def main():
    text = input("Enter the text to hash: ")

    md5_hash = calculate_md5(text)
    sha256_hash = calculate_sha256(text)

    print(f"MD5 Hash: {md5_hash}")
    print(f"SHA-256 Hash: {sha256_hash}")

if __name__ == "__main__":
    main()