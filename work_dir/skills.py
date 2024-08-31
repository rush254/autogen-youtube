

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

        

##### Begin of generate_and_save_markdown #####

from typing import List, Dict, Optional
from pathlib import Path

def generate_and_save_markdown(
    sections: List[Dict[str, Optional[str]]], 
    output_file: str = "report.md", 
    report_title: str = "Markdown Report"
) -> None:
    """
    Function to generate a Markdown report file.

    :param sections: A list of sections where each section is represented by a dictionary containing:
                     - title: The title of the section.
                     - level: The heading level (e.g., "title", "h1", "h2").
                     - content: The content or body text of the section.
                     - image: (Optional) The URL or local path to the image.
    :param output_file: The name of the output Markdown file. (default is "report.md")
    :param report_title: The title of the report. (default is "Markdown Report")
    :return: None
    """

    # Create or overwrite the markdown file
    with open(output_file, "w") as md_file:
        # Write the report title as the main heading
        md_file.write(f"# {report_title}\n\n")

        # Process each section
        for section in sections:
            title = section.get("title", "")
            level = section.get("level", "h1")
            content = section.get("content", "")
            image = section.get("image", "")

            # Determine the heading level
            if level == "title":
                md_file.write(f"# {title}\n\n")
            elif level == "h1":
                md_file.write(f"## {title}\n\n")
            elif level == "h2":
                md_file.write(f"### {title}\n\n")
            else:
                md_file.write(f"#### {title}\n\n")

            # Add the content
            if content:
                md_file.write(f"{content}\n\n")

            # Add the image if provided
            if image:
                md_file.write(f"![{title}]({image})\n\n")

        print(f"Markdown report saved as {output_file}")

# # Example usage
# sections = [
#     {
#         "title": "Introduction - Early Life",
#         "level": "h1",
#         "image": "https://picsum.photos/536/354",
#         "content": ("Marie Curie was born on 7 November 1867 in Warsaw, Poland. "
#                     "She was the youngest of five children. Both of her parents were teachers. "
#                     "Her father was a math and physics instructor, and her mother was the head of a private school. "
#                     "Marie's curiosity and brilliance were evident from an early 


#### End of generate_and_save_markdown ####

        