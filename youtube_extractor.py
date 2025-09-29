import re
import subprocess
import json

def extract_video_id(url):
    # Extract the video ID from the YouTube URL
    pattern = r"(?:v=)([^&#]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")

def fetch_video_info(video_id):
    # Construct the API URL
    api_url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&part=snippet,statistics,recordingDetails&key=AIzaSyBmQcXmAHD2h5ZurlNKHvHRwMVHbBQqbvc"

    # Use curl to fetch the JSON output
    curl_command = f"curl -s '{api_url}'"
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        raise RuntimeError("Failed to fetch data from YouTube API")

    # Parse and pretty-print the JSON output
    data = json.loads(result.stdout)
    print(json.dumps(data, indent=2))

def main():
    # Prompt the user for a YouTube URL
    youtube_url = input("Enter a YouTube URL (e.g., https://www.youtube.com/watch?v=nBJRaflBDBg): ").strip()

    try:
        video_id = extract_video_id(youtube_url)
        print(f"\nExtracted Video ID: {video_id}\n")
        fetch_video_info(video_id)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
