from enum import Enum

class AppMode(Enum):
    DEVELOPMENT = "dev"
    PRODUCTION = "prod"
    TESTING = "test"

current_mode = AppMode.PRODUCTION

if current_mode == AppMode.DEVELOPMENT:
    print("Running in development mode.")
else:
    print("Running in non-development mode.")