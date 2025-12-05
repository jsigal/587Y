class UserProfile:
    def __init__(self, username, email, preferences, activity_log):
        self.username = username
        self.email = email
        self.preferences = preferences  # Dictionary: {'theme': 'dark', 'notifications': True}
        self.activity_log = activity_log # List of dictionaries: [{'action': 'login', 'timestamp': '...'}, {'action': 'view_item', 'item_id': 123}]

# Example usage
user = UserProfile(
    "alice123",
    "alice@example.com",
    {'theme': 'light', 'language': 'en'},
    [{'event': 'registered', 'date': '2025-01-15'}, {'event': 'logged_in', 'date': '2025-12-01'}]
)
print(user.preferences['language'])
print(user.activity_log[0]['event'])