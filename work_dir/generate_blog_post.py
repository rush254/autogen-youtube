# filename: generate_blog_post.py
import re

# Read the transcript file
with open("9eb5adf1-f2c5-4014-902d-497678648e3c.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

# Preprocess the transcript
transcript = re.sub(r'\n+', '\n', transcript)  # Remove consecutive newlines
transcript = re.sub(r'^\s+', '', transcript)  # Remove leading whitespace
transcript = re.sub(r'\s+$', '', transcript)  # Remove trailing whitespace

# Generate the blog post
blog_post = "Blog Post:\n\n" + transcript

# Print the blog post
print(blog_post)