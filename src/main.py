import sys
import os
from PyQt6.QtWidgets import QApplication
from managers.local_manager import LocalManager
from player.window import DigitalSignagePlayer

MEDIA_PATH = os.path.join(os.getcwd(), "media_cache")

def main():
    app = QApplication(sys.argv)
    manager = LocalManager(media_folder=MEDIA_PATH)
    player = DigitalSignagePlayer(manager)
    player.showFullScreen()
    from PyQt6.QtCore import QTimer
    QTimer.singleShot(1000, player.play_next)
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
