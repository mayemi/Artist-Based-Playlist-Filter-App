import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Playlist Filter")
        self.setWindowIcon(QIcon("Artist-Based-Playlist-Filter-App/spotify.png"))
        self.setGeometry(420, 200, 400, 450)
        self.setMaximumWidth(600)
        self.setMinimumWidth(300)
        self.setMaximumHeight(700)
        self.setMinimumHeight(450)
        self.setStyleSheet("background: rgb(0, 66, 37); font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;")

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id="CLIENT ID HERE",
            client_secret="CLIENT SECRET HERE",
            redirect_uri="http://localhost:8888/callback",
            scope="playlist-modify-public playlist-read-private"
            ))
        
        grid = QGridLayout()

        label1 = QLabel("Playlist URL:")
        label1.setStyleSheet("color: azure; font-size: 16px; font-weight: 500;")
        label2 = QLabel("Artist Name:")
        label2.setStyleSheet("color: azure; font-size: 16px; font-weight: 500;")

        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setPlaceholderText("https://open.spotify.com/playlist/Op53oehixzjz5ZQJB?si=ec83e52ca34b9f")
        self.lineEdit1.setStyleSheet("background: azure; font-size: 14px; height: 20px; border: none;")
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setPlaceholderText("Iron Maiden")
        self.lineEdit2.setStyleSheet("background: azure; font-size: 14px; height: 20px; border: none;")

        pushButton = QPushButton("Create Playlist")
        pushButton.setCursor(Qt.PointingHandCursor)
        pushButton.setStyleSheet("""QPushButton{
                                 background: azure; 
                                 font-size: 13px; 
                                 font-weight: 500; 
                                 border: none; 
                                 padding: 4px 4px 4px 4px; 
                                 border-radius: 10px;}
                                 QPushButton:pressed{
                                 background-color: lightgray;
                                 }""")
        pushButton.clicked.connect(self.createPlaylist)

        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)
        self.textEdit.setStyleSheet("background: azure; border: none; font-size: 13px;")
        self.addLog("Application has been launched!")

        grid.setSpacing(25)
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 1, 0)
        grid.addWidget(self.lineEdit1, 0, 1)
        grid.addWidget(self.lineEdit2, 1, 1)
        grid.addWidget(pushButton, 2, 0, 1, 2)
        grid.addWidget(self.textEdit, 3, 0, 1, 2)

        self.setLayout(grid)

    def addLog(self, message):
        self.textEdit.append(message)

    def createPlaylist(self):
        playlist_link = self.lineEdit1.text()
        artist_name = self.lineEdit2.text()

        playlist_id = playlist_link.split("/")[-1].split("?")[0]

        results = self.sp.playlist_items(playlist_id, limit=100, offset=0)

        self.addLog(f"{artist_name}'s tracks in playlist: ")

        order = 0
        tracksToAdd = []

        while results:
            for item in results['items']:
                track = item['track']

                if track and 'artists' in track:
                    track_artists = track['artists']
                    for artist in track_artists:
                        if artist and artist.get('name') and artist['name'].lower() == artist_name.lower():
                            order += 1
                            self.addLog(f"{order}. {track['name']}")
                            tracksToAdd.append(track['id'])
                else:
                    self.addLog("Podcast detected. Skipping...")
            
            if results.get('next'):
                results = self.sp.next(results)
            else:
                results = None
        user_id = self.sp.me()['id']

        newPlaylistName = f"{artist_name}"
        new_playlist = self.sp.user_playlist_create(user=user_id, name=newPlaylistName, description=f"Only {artist_name}." ,public=True)
        new_playlist_id = new_playlist['id']

        self.sp.user_playlist_add_tracks(user_id, new_playlist_id, tracksToAdd)
        self.addLog(f"A new playlist has been created featuring songs by {artist_name}: {newPlaylistName}.")
        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
