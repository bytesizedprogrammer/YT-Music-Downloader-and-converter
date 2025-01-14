from pytube import Playlist

def get_playlist_urls(playlist_url):
    try:
        # Create a Playlist object
        playlist = Playlist(playlist_url)
        
        # Fetch all video URLs
        urls = [video_url for video_url in playlist.video_urls]
        
        print("URLs in the playlist:")
        for url in urls:
            print(url)
        
        return urls
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    get_playlist_urls(playlist_url)
