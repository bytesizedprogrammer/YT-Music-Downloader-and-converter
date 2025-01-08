# YouTube to MP3 Downloader

Description

This project uses yt-dlp and ffmpeg to process a list of YouTube URLs, downloading the videos and converting them into MP3 files. Future updates may include an automated web scraping feature to fetch URLs from a YouTube playlist provided by the user, eliminating the need to manually input URLs.

Features

Downloads YouTube videos from a list of URLs.

Converts downloaded videos into MP3 files.

Automatically handles duplicate links by processing each URL only once.

Requirements

Python 3.x

Installed Python packages (yt-dlp, etc.)

ffmpeg installed and added to your system PATH

Installation

Clone the repository or download the project files.

Install the required Python packages:

pip install yt-dlp

Ensure ffmpeg is installed. Follow installation instructions for your operating system:

Windows: Download from FFmpeg official site and add it to your PATH.

Linux/MacOS: Install via package manager (e.g., sudo apt install ffmpeg for Ubuntu).

Usage

Open the urls.txt file and paste your YouTube URLs, one per line.

Press Enter after each URL to add a new line.

Run the downloadYTSongs.py script to download the videos:

python downloadYTSongs.py

Run the convertFilesToMP3.py script to convert the videos to MP3:

python convertFilesToMP3.py

Your converted MP3 files will be located in the mp3FilesHere directory.

Notes

Duplicate URLs in the urls.txt file will only be processed once.

Ensure all URLs in the file are valid YouTube links.

Legal Warning

This tool is intended for use only with content you have the right to download, such as:

Your own works uploaded to YouTube.

Content for which you have explicit permission to download audio.

I do not condone or support the illegal downloading of copyrighted YouTube content. Use this tool responsibly.
