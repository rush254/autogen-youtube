# filename: generate_transcript.py
from skills import generate_and_save_transcript

video_url = "https://www.youtube.com/watch?v=Rfws9ZMmkJk"
transcript_file = generate_and_save_transcript(video_url)
print(transcript_file)