import os
from pathlib import Path
from .base import PlaylistManager, MediaItem

class LocalManager(PlaylistManager):
    def __init__(self, media_folder: str):
        self.media_folder = Path(media_folder)
        self.playlist: list[Path] = []
        self.current_index = 0
        
        if not self.media_folder.exists():
            os.makedirs(self.media_folder)
            
        self.refresh_playlist()

    def refresh_playlist(self):
        valid_extensions = {'.mp4', '.avi', '.mkv', '.jpg', '.png', '.jpeg'}
        
        all_files = list(self.media_folder.iterdir())
        self.playlist = [
            f for f in all_files 
            if f.suffix.lower() in valid_extensions
        ]
        print(f"Playlist carregada com {len(self.playlist)} itens.")

    def get_next_media(self) -> MediaItem:
        if not self.playlist:
            return None

        file_path = self.playlist[self.current_index]

        self.current_index = (self.current_index + 1) % len(self.playlist)
        
        m_type = 'video' if file_path.suffix.lower() in {'.mp4', '.avi', '.mkv'} else 'image'
        
        return MediaItem(
            file_path=str(file_path.absolute()),
            media_type=m_type,
            duration=5
        )
