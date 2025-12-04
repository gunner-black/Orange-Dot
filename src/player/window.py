import sys
import platform
from PyQt6.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer
import vlc

class DigitalSignagePlayer(QMainWindow):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        
        self.setup_ui()
        
        self.events = self.mediaplayer.event_manager()
        self.events.event_attach(vlc.EventType.MediaPlayerEndReached, self.on_end_reached)

    def setup_ui(self):
        self.setWindowTitle("PySignage Player")
        self.setStyleSheet("background-color: black;")
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.video_frame = QFrame()
        self.video_frame.setFrameShape(QFrame.Shape.NoFrame)
        
        # layout
        layout = QVBoxLayout(self.central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.video_frame)

    def get_handle(self):
        return int(self.video_frame.winId())

    def play_next(self):
        media_item = self.manager.get_next_media()
        
        if not media_item:
            print("Nenhuma mídia encontrada.")
            return

        print(f"Tocando: {media_item.file_path}")
      
        media = self.instance.media_new(media_item.file_path)
        self.mediaplayer.set_media(media)
        if platform.system() == "Windows":
            self.mediaplayer.set_hwnd(self.get_handle())
        elif platform.system() == "Linux":
            self.mediaplayer.set_xwindow(self.get_handle())
        else: # MacOS
            self.mediaplayer.set_nsobject(self.get_handle())

        self.mediaplayer.play()

        if media_item.media_type == 'image':
            QTimer.singleShot(media_item.duration * 1000, self.play_next)

    def on_end_reached(self, event):
        self.play_next()
