import random

# Simulated user data
user_profiles = {
    'User1': {'interests': ['sports', 'technology']},
    'User2': {'interests': ['politics', 'travel']},
    'User3': {'interests': ['music', 'food']},
    # ... Add more user profiles
}

# Simulated content with relevance scores
content = [
    {'title': 'Breaking News in Tech', 'relevance_score': 0.9},
    {'title': 'Travel Tips for Your Next Vacation', 'relevance_score': 0.8},
    {'title': 'New Music Album Release', 'relevance_score': 0.7},
    # ... Add more content
]

def calculate_ctr(user_profile, content):
    user_interests = user_profile.get('interests', [])
    relevant_content = [c for c in content if any(interest in c['title'].lower() for interest in user_interests)]
    ctr = len(relevant_content) / len(content)
    return ctr

# Calculate CTR for a specific user
user = user_profiles['User1']
ctr = calculate_ctr(user, content)
print(f'Click-Through Rate (CTR) for User1: {ctr:.2f}')
