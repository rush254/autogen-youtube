

##### Begin of generate_youtube_transcript #####

from typing import List
import uuid
import requests
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi

def generate_and_save_transcript(video_url: str) -> str:
    """
    Function to generate and save a transcript from a YouTube video URL. 
    The transcript is retrieved using the YouTube Transcript API and saved to a text file.

    :param video_url: The URL of the YouTube video.
    :return: The filename of the saved transcript.
    """
    
    # Extract the video ID from the URL
    video_id = video_url.split("v=")[-1]

    # Fetch the transcript using the YouTubeTranscriptApi
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        print(f"An error occurred while retrieving the transcript: {e}")
        return ""

    # Convert the transcript from list of dictionaries to plain text
    transcript_text = "\n".join([item['text'] for item in transcript])

    # Generate a random UUID as the file name
    file_name = str(uuid.uuid4()) + ".txt"
    file_path = Path(file_name)

    # Save the transcript to a file
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(transcript_text)
            print(f"Transcript saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving the transcript: {e}")
        return ""

    # Return the filename of the saved transcript
    return str(file_path)

# Example usage of the function:
# generate_and_save_transcript("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


#### End of generate_youtube_transcript ####

        