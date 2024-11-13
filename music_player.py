import sys
import time
import vlc
import yt_dlp 
# from pytube import YouTube

class MusicPlayer:
    def __init__(self, song_file):
        self.song_file = song_file
        self.songs = self.load_songs()
        self.current_song_index = 0
        self.previous_song_index = -1
        self.is_playing = False
        self.player = None

    # Load songs from the specified file.
    def load_songs(self):
        songs = []
        try:
            with open(self.song_file, 'r') as file:
                for line in file:
                    base_url = line.strip()
                    if base_url:
                        title = "Unknown title"
                        try:
                            ydl_opts = {'quiet': True}
                            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                                info_dict = ydl.extract_info(base_url, download=False)
                                title = info_dict.get('title', title)
                        except Exception as e:
                            print(f"Error accessing title of {base_url}: {e}")
                        songs.append((base_url, title))
        except Exception as e:
            print(f"Error loading songs: {e}")
            sys.exit(1)
        return songs

    # Get the stream URL from YouTube.
    def get_stream_url(self, url):
        try:
            base_url = url.split('&')[0]
            ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(base_url, download=False)
                stream_url = info_dict['url']
                return stream_url
           
            yt = YouTube(base_url)
            stream = yt.streams.filter(only_audio=True).first()
            if not stream:
                print("No audio stream available.")
                return None
            return stream.url
            
        except Exception as e:
            print(f"Error getting stream URL from {url}: {e}")
            return None

    # Play the current song. - works well. plays song in specified index.
    def play(self, index=None):
        # Stop current song playing
        if self.is_playing and self.player is not None:
            self.player.stop()
            self.is_playing = False

        if index is not None:
            self.current_song_index = index
        
        if self.current_song_index < len(self.songs):
            song_url, song_title = self.songs[self.current_song_index]
            stream_url = self.get_stream_url(song_url)
            if not stream_url:
                print("Failed to get stream URL.")
                return
            
            self.player = vlc.MediaPlayer(stream_url)
            self.player.play()
            self.is_playing = True
            print(f'Playing: {song_title} (Status: Playing)')

            self.previous_song_index = self.current_song_index

            # Wait for the song to finish playing
            while self.player.is_playing():
                time.sleep(1)

            self.is_playing = False
            # self.current_song_index += 1  # Move to the next song

    # Pause the current song.
    def pause(self):
        if self.is_playing and self.player is not None:
            self.player.pause()
            self.is_playing = False
            print('Paused Music')
        else:
            print("No song is currently playing to pause.")

    # Resume the current song.
    def resume(self):
        if self.is_playing and self.player is not None:
            self.player.play()
            self.is_playing = True
            print('Resumed Music')

    # Stop current song
    def stop(self):
        self.player.stop()
        if self.is_playing and self.player is not None:
            # self.player.stop()
            self.is_playing = False
            print('Stopped Music')

    # Skip to the next song.
    def skip(self):
        self.stop()            
        '''
        if self.is_playing and self.player is not None:
            self.player.stop()
            self.is_playing = False
        '''

        self.current_song_index += 1
        if self.current_song_index < len(self.songs):
            self.play()
        else:
            print("No more songs in the playlist. Update playlist innit")

    # Go back to the previous song
    def previous(self):
        if self.current_song_index > 0:
            self.stop()
            self.previous_song_index = self.current_song_index
            self.current_song_index -=1
            self.play(self.current_song_index)
        else:
            print("No previous song available. Update playlist innit")

        '''
        if self.previous_song_index >= 0:
            self.current_song_index = self.previous_song_index
            self.play(self.current_song_index)
        else:
            print("No previous song available. Update playlist innit")
        '''        

    # Display the current song's metadata.
    def display_metadata(self):
        if self.current_song_index < len(self.songs):
            song_url, song_title = self.songs[self.current_song_index]
            status = "Playing" if self.is_playing else "Paused" if self.player and not self.is_playing else "Stopped"
            print(f"Current song: {song_title} (Index: {self.current_song_index}, Status: {status})")
        else:
            print("No song is currently playing.")

    # List songs in the playlist (songs.txt) - works weel. lists songs in an array format
    def list_songs(self):
        print("Songs in the playlist: ")
        for index, (base_url, title) in enumerate(self.songs):
            print(f"{index}: {title}")

    # Display all help commands
    def help(self):
        help_text = """
            Available commands:

            play + <index> : Play song at a specific index
            next: Go to next song
            previous: Go to previous song
            pause: Pause current song
            resume: Resume current song
            stop: Stop playing current song
            
            show status: Show details on current song playing
            list songs: Display all songs in your playlist 'songs.txt'

            help: Show available commands 
            exit: Exit music player

            Aliases for the commands:
            r - resume current song
            p - pause current song
            pr - previous song
            
            ss - show status/song metadata
            ls - list songs

            h - help (show all commands)
            q - exit music player
        """
        print(help_text)


    # Run the whole Music Player Application
    def run(self):
        self.help()  # Display help text at the start
        while True:
            command = input(f" \nEnter command (play <index>, pause, resume, next, previous, show status, list songs, exit): \n").strip().lower() 

            if command.startswith('play'):
                try:
                    index = int(command.split()[1])  # Get the index from the command
                    self.play(index)
                except (IndexError, ValueError):
                    print("Please provide a valid index.")
            elif command == 'pause' or command == 'p':
                self.pause()
            elif command == 'resume' or command == 'r':
                self.resume()
            elif command == 'next' or command == 'skip':
                self.skip()
            elif command == 'previous' or command == 'pr':
                self.previous()
            elif command == 'stop':
                self.stop()
            elif command == 'show status' or command =='ss':
                self.display_metadata()
            elif command == 'list songs' or command == 'ls':
                self.list_songs()
            elif command == 'help' or command == 'h':
                self.help()
            elif command == 'exit' or command == 'q':
                self.stop()
                break
            else:
                print("Unknown command")

if __name__ == "__main__":
    player = MusicPlayer('songs.txt')
    player.run()
