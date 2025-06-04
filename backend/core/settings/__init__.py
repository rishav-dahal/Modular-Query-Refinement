import os

env = os.environ.get("ENV") 
print(f"Current environment: {env}")
if env == "prod":
    from .prod import *
else:
    from .dev import *
