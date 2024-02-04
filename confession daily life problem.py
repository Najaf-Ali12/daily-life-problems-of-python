#REAL LIFE PROBLEM NO 4
#here's a Python programming problem scenario based on the confession theme, 
#designed to subtly highlight potential time-wasting aspects and encourage 
#more productive digital activities:
#Scenario:
#The Digital Dilemma: Balancing Online Engagement and Productivity
#You're a student developer working on a time management app aimed at helping university students 
#strike a balance between their academic goals and online social activities. Your task is to
# create a function called analyze_confession_engagement(confession_data)
# that analyzes data from a fictional confessions page to provide insights into 
#student behavior and time usage.
#Function Inputs:
# confession_data: A list of dictionaries, where each dictionary represents a confession post
# with the following keys:
#o timestamp: The date and time the post was made (e.g., "2024-01-28 14:30").
#o likes: The number of likes the post received.
#o comments: The number of comments on the post.
#o length: The length of the post in characters.
#Function Outputs:
#average_time_spent: The average amount of time spent per confession post, estimated based on length 
#and assuming an average reading speed.
# most_engaged_hours: A list of the top 3 hours of the day with the highest overall engagement 
#(likes and comments).
# popular_topics: A list of the most common confession topics, identified using keyword analysis.
#Additional Requirements:
# Implement clear and concise code using appropriate Python data structures and functions 
#(e.g., lists, dictionaries, conditional statements, loops, string manipulation).
# Use datetime functions to extract and analyze time-related information.
# Incorporate basic text analysis techniques to extract keywords and identify popular topics.
#Discussion Prompts:
# What insights can you derive from the confession data?
# How might this data be used to help students understand their online behavior 
#and make more informed choices about time management?
# What alternative online activities could be promoted to enhance productivity and personal development?
#Goals:
# Engage students with a relatable topic while fostering critical thinking about time
# management and digital habits.
# Demonstrate practical applications of Python programming for data analysis and insights.
# Encourage discussions about responsible online engagement and prioritizing academic goals.
from collections import Counter
from datetime import datetime

def analyze_confession_engagement(confession_data):
    # Calculate average time spent per confession post
    total_length = sum(confession['length'] for confession in confession_data)
    average_time_spent = total_length / len(confession_data)
    # Extract hour from timestamp and calculate engagement for each hour
    engagement_by_hour = Counter()
    for confession in confession_data:
        timestamp = datetime.strptime(confession['timestamp'], '%Y-%m-%d %H:%M')
        hour = timestamp.hour
        engagement_by_hour[hour] += confession['likes'] + confession['comments']
    
    # Find top 3 engaged hours
    most_engaged_hours = [hour for hour, _ in engagement_by_hour.most_common(3)]
    
    # Extract keywords from confession posts and identify popular topics
    topics = []
    for confession in confession_data:
        topics.extend(confession['content'].split())
    popular_topics = [topic for topic, _ in Counter(topics).most_common(3)]
    
    return average_time_spent, most_engaged_hours, popular_topics

# Example usage:
like1=int(input("enter the likes of post1:"))
like2=int(input("enter the likes of post2:"))
like3=int(input("enter the likes of post3:"))
comment1=int(input("enter the number of comments of post1:"))
comment2=int(input("enter the number of comments of post2:"))
comment3=int(input("enter the number of comments of post3:"))
char1=int(input("enter the number of characters used in post1:"))
char2=int(input("enter the number of characters used in post2:"))
char3=int(input("enter the number of characters used in post3:"))
confession_data = [
    {'timestamp': '2024-1-1 1:20', 'likes': like1, 'comments': comment1, 'length': char1, 'content': 'Confession post 1 content'},
    {'timestamp': "2024-2-2 6:30", 'likes': like2, 'comments': comment2, 'length': char2, 'content': 'Confession post 2 content'},
    {'timestamp': "2024-2-4 9:36", 'likes': like3, 'comments': comment3, 'length': char3, 'content': 'Confession post 3 content'},
    # Add more confession posts as needed
]

average_time_spent, most_engaged_hours, popular_topics = analyze_confession_engagement(confession_data)
print("Average time spent per confession post:", average_time_spent)
print("Top 3 engaged hours of the day:", most_engaged_hours)
print("Most common confession topics:", popular_topics)






