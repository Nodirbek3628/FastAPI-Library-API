import config

for key in ["DB_HOST", "DB_PORT", "DB_USER", "DB_PASSWORD", "DB_NAME"]:
    val = getattr(config, key)
    print(key, repr(val))