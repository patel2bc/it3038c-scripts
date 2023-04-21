import praw

# Enter API information, see README.md for more information 
reddit = praw.Reddit(client_id='THE ID BELOW WHERE IT SAYS PERSONAL USE SCRIPT',
                     client_secret='SECRET_KEY',
                     user_agent='Topics Review')

# User input for topic 
topic_name = input("Enter a single word topic -(For example: Tesla, School, Lincoln, RTX4090): ")

# Searches Reddit top 5 to get an average and reduce overwhelming results 
results = reddit.subreddit('all').search(topic_name, sort='top', limit=5)

# Define the positive and negative terms to look for in the comments
positive_terms = ['great', 'excellent', 'awesome', 'amazing', 'love', 'good', 'superb', 'exceptional', 'reliable']
negative_terms = ['bad', 'terrible', 'awful', 'hate', 'poor', 'garbage', 'trash', 'disappointed', 'unreliable', 'horrible']

# Variables to track positive and negative hotwords 
positive_count = 0
negative_count = 0

# Analyze the comments for each result
for result in results:
    print(f"\nComments for {result.title}:")
    for comment in result.comments:
        # Conditional statement to check for valid comments 
        if isinstance(comment, praw.models.Comment):
            # Check for positive or negative comments 
            if any(term in comment.body.lower() for term in positive_terms):
                print(f"Positive comment: {comment.body}")
                positive_count += 1
            elif any(term in comment.body.lower() for term in negative_terms):
                print(f"Negative comment: {comment.body}")
                negative_count += 1
        else:
            continue

# Calculate the percentage of positive and negative comments
total_count = positive_count + negative_count
if total_count > 0:
    positive_percent = (positive_count / total_count) * 100
    negative_percent = (negative_count / total_count) * 100
    print(f"\nTake this ratio with a grain of salt. Out of {total_count} comments, {positive_percent:.2f}% are positive and {negative_percent:.2f}% are negative.")
else:
    print("No comments found for this product.")
