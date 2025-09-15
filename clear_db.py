#!/usr/bin/env python3
import os
from pymongo import MongoClient

# Get MongoDB URL from environment or prompt
DATABASE_URL = os.environ.get('DATABASE_URL')
if not DATABASE_URL:
    DATABASE_URL = input("Enter DATABASE_URL: ").strip()
    if not DATABASE_URL:
        print("DATABASE_URL is required")
        exit(1)

# Connect and clear the core config
client = MongoClient(DATABASE_URL)
db = client["Loader"]
config = db["config"]

# Delete the core config to force using hardcoded values
result = config.delete_one({'key': 'core'})
print(f"Deleted {result.deleted_count} core config entry")

client.close()
print("Database cleared. UBLoader will now use hardcoded repository settings.")