# src/core/shortener.py
import hashlib
import json
import os

class URLShortener:
    def __init__(self, storage_file="urls.json"):
        self.storage_file = storage_file
        if not os.path.exists(storage_file):
            with open(storage_file, "w") as f:
                json.dump({}, f)

    def shorten(self, original_url):
        short_hash = hashlib.md5(original_url.encode()).hexdigest()[:8]
        short_url = f"https://py.ly/{short_hash}"

        with open(self.storage_file, "r+") as f:
            data = json.load(f)
            data[short_url] = original_url
            f.seek(0)
            json.dump(data, f, indent=4)

        return short_url
