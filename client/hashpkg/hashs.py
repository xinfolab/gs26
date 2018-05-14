import hashlib

class hash_calc:
    def __init__(self):
        self.hash_md5 = hashlib.md5()
        self.hash_sha1 = hashlib.sha1()
        self.hash_sha256 = hashlib.sha256()

    def get_md5_hash(self, path):
        with open(path, 'rb') as afile:
            buf = afile.read()
            self.hash_md5.update(buf)
        return self.hash_md5.hexdigest()

    def get_sha1_hash(self, path):
        with open(path, 'rb') as afile:
            buf = afile.read()
            self.hash_sha1.update(buf)
        return self.hash_sha1.hexdigest()

    def get_sha256_hash(self, path):
        with open(path, 'rb') as afile:
            buf = afile.read()
            self.hash_sha256.update(buf)
        return self.hash_sha256.hexdigest()

