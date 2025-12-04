from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class MediaItem:
    file_path: str
    media_type: str
    duration: int = 10

class PlaylistManager(ABC):
    @abstractmethod
    def refresh_playlist(self):
        pass

    @abstractmethod
    def get_next_media(self) -> Optional[MediaItem]:
        pass
