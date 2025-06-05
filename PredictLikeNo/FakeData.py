import json
import random
from datetime import datetime, timedelta
import faker

# Create a faker generator
fake = faker.Faker()

# Reactions and comment ranges
reaction_range = (50, 500)
comment_range = (5, 100)

# Generate 100 fake posts
posts = []
for i in range(100):
    post = {
        "post_id": fake.uuid4()[:8],
        "author": fake.name(),
        "timestamp": (datetime.now() - timedelta(days=random.randint(0, 60))).isoformat(),
        "content": fake.sentence(nb_words=12),
        "reactions": random.randint(*reaction_range),
        "comments": random.randint(*comment_range)
    }
    posts.append(post)

# Return as JSON
json_data = json.dumps(posts, indent=2)
json_data[:1000]  # Previewing only part of the data for readability

