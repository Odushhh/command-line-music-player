# Command Line Music Player

## Description

Have you ever had such terrible RAM that you literally cannot stream any music on YouTube? Here's an alternative if you're streaming from a potato - a Spotify/YouTube-esque music player that you can operate right from your CLI (Powershell, Bash, Zsh, CMD, etc)

This is a simple (could be unnecessary) command-line application built using Python, where you can store a bunch of songs and their URLs from a YouTube playlist into a .txt file, and control the playback using CLI commands. 

'Hacker-oriented' project right here. It gives you the following ;
> Zero tolerance for search buttons, and

> Enormous hate for modern GUIs



P.S.: You'll need internet connection because the music is streamed from YouTube using `yt-dlp` and `python-vlc` 

With this overkill tool you can play, pause, skip, and manage songs. The libraries `python-vlc` and `yt-dlp` are used for audio playback & for downloading YouTube audio streams, respectively. You can play a specific song based on its index (think of the songs arranged in an array), without having to use YouTube's GUI and even skip ads!


## Features/Functionalities

- Command-line interface
- Play songs from a playlist of YouTube URLs.
- Pause and resume playback.
- Skip to the next song 
- Go back to the previous song.
- Display the metadata of the song playing.
- List all songs in the playlist.


## Requirements/Libraries

- Python 3.9 or higher
- VLC Media Player (if you don't have it already then they should confiscate your PC)
- `python-vlc` library
- `yt-dlp` library


## Installation

1. **Clone repository**:
   ```bash
   git clone https://github.com/yourusername/music_player.git
   cd music_player
   ```

2. **Install required Python libraries**:
   ```bash
   pip install python-vlc yt-dlp
   ```

3. **Install VLC Media Player**(**Optional**):
   - Download and install VLC from the [official VLC website](https://www.videolan.org/vlc/).
     **Ensure that VLC is added to your system's PATH** (this is usually done automatically during installation).


## Usage

1. **Create a `songs.txt` file** and put a bunch of YouTube URLs of the songs you want to play, one URL per line. For example:
   ```bash
   https://www.youtube.com/watch?v=bnc7hO8UGXU
   https://www.youtube.com/watch?v=Yhivl6fln3s
   ```

2. **Run the music player**:
   ```bash
   python music_player.py
   ```

3. **Commands to control playback**:

   - `play <index>`: Play the song at the specified index (e.g., `play 0`).
   - `pause`: Pause the currently playing song.
   - `resume`: Resume the currently paused song.
   - `next` or `skip`: Skip to the next song in the playlist.
   - `previous` or `pr`: Go back to the previous song.

   - `stop`: Stop the currently playing song.
   - `show status` or `ss`: Display the current song's metadata (title, index, status).
   - `list songs` or `ls`: List all songs in the playlist.

   - `help` or `h`: Show available commands.
   - `exit` or `q`: Exit the music player.


## Example Commands

- To play the first song (index = 0):
  ```bash
  play 0
  ```

- To pause the current song:
  ```bash
  pause
  ```

- To skip to the next song:
  ```bash
  next
  ```

- To go back to the previous song:
  ```bash
  previous
  ```

- To list all songs in the playlist:
  ```bash
  list songs
  ```


## Testing (**Optional**)

To ensure that all functionalities work correctly, you can run the provided test suite using `unittest`. 

1. **Run the tests**:
   ```bash
   python -m unittest test_music_player.py
   ```


## Legal Notice
This tool is provided for personal use only. Users are responsible for complying with YouTube's Terms of Service and all applicable copyright laws. The script facilitates playback of YouTube content through legal open-source tools (mpv and youtube-dl) but does not download, store, or redistribute any copyrighted content. Please respect content creators' rights and YouTube's terms of service when using this tool.


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


