#!/usr/bin/env python3
import shutil
import os

cache_path = ".rcache"
if os.path.exists(cache_path):
    shutil.rmtree(cache_path)
    print("Cache cleared")
else:
    print("No cache found")