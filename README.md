# Orange Dot 📺

> A modular, open-source Digital Signage player built in Python, designed to operate from a standalone (offline) mode up to complex, remotely managed networks.

![Status](https://img.shields.io/badge/Status-In_Development-yellow) 
![Python](https://img.shields.io/badge/Python-3.10%2B-blue) 
![License](https://img.shields.io/badge/License-GPL_v3-red)

## 🎯 Project Goal

The Digital Out-of-Home (DOOH) media market often presents high entry barriers due to expensive proprietary SaaS licensing models. **PySignage** aims to democratize access to this technology by offering a robust client that can be deployed on low-cost hardware (Raspberry Pi, Mini PCs, Linux/Windows).

## 🚀 Modular Architecture

The system is designed to be agnostic to the data source. It operates primarily in two modes, defined in `config/settings.yaml`:

1.  **Standalone Mode (Local):**
    * The system reads a local directory or a JSON file for the playlist.
    * Ideal for small, simple operations where updates are done via network share or direct access.
    * *No internet dependency required for playback.*

2.  **Cloud Mode (Remote) [Future]:**
    * The system connects to a central REST API/WebSocket server.
    * It downloads and caches media files locally.
    * It sends "Heartbeats" and Proof-of-Play Logs back to the server.

### The Key to Modularity

The separation of concerns is managed through the `PlaylistManager` interface:

```python
# The Player (src/player) doesn't know *where* the media comes from; 
# it only interacts with the Manager interface.

# Implementation A: Local Mode
manager = LocalManager(media_folder='media_cache') 

# Implementation B: Remote Mode (Future)
# manager = RemoteManager(api_url='[https://mycms.com/api/](https://mycms.com/api/)')

media = manager.get_next_item()
player.play(media)
```

## 🛠️ Technologies Used
  - Language: Python 3.10+
  - Graphical Interface: PyQt6 (for robust layout management and full-screen handling)
  -  Video Engine: LibVLC (via python-vlc)
  - Configuration: YAML / JSON

## 📂 Repository Structure
py-signage-player/

│

├── config/                  # Configuration files

│   ├── settings.yaml        # General configs (mode: LOCAL/REMOTE, resolution, etc.)

│   └── default_playlist.json# Playlist structure for local mode

│

├── media_cache/             # Folder for media files (Local content or Remote Cache)

│

├── src/

│   ├── main.py              # Application entry point

│   │

│   ├── player/              # Presentation Logic (GUI and Playback)

│   │   ├── window.py        # PyQt Window (Full screen, aspect ratio handling)

│   │   └── vlc_engine.py    # VLC wrapper and control logic

│   │

│   ├── managers/            # THE MODULAR CORE (Playlist Logic)

│   │   ├── base.py          # Abstract Base Class (The interface/contract)

│   │   ├── local_manager.py # Implementation for Standalone Mode (reads disk)

│   │   └── remote_manager.py# Future implementation (talks to API)

│   │

│   └── utils/               # Helper modules (logging, file downloads, system checks)

│

├── requirements.txt         # Python dependencies (PyQt6, python-vl└── README.md
└── LICENSE                  # (GPL v3 recommended)

...
