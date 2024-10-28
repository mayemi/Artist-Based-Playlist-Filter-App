# Artist-Based-Playlist-Filter-App
EN: A PyQt5 product, provides you to filter your Spotify playlists by artist. TR: PyQt5 ürünü, Spotify çalma listelerinizi sanatçı bazında filtrelemenizi sağlayan bir uygulama.

# TR:  
Python'un masaüstü geliştirme kütüphanesi olan PyQt5 ve Spotify API ile geliştirilmiş bu uygulama, kalabalık Spotify çalma listelerinizi sanatçı bazında bölebilmenizi sağlıyor. Ayıklanmasını istediğiniz çalma listesinin urlini ve sanatçının adını girip "Create Playlist" butonuna tıklamanız yeterli. Belirttiğiniz sanatçının şarkılarını seçip yeni bir playlist oluşturacaktır.  

Spotify ile bağlantıyı kurmak için gereken "Client ID" ve "Cliend Secret" bilgilerini koddan kaldırdım, sadece "exe" dosyasını kullanacaksanız uğraşmanıza gerek yok fakat kodu çalıştıracaksanız Spotify Developer Portal üzerinden bu bilgileri edinip kodda ilgili yere yazmalısınız.  

Gerekli modüller için terminale şu kodu yazın:  
-Windows: pip install spotipy PyQt5  
-Linux/MacOS: pip3 install spotipy PyQt5  

İyi dinlemeler!

# EN:  
This application developed with PyQt5, a desktop development library for Python, and the Spotify API allows you to split your crowded Spotify playlists by artist. Simply enter the URL of the playlist you want to extract and the artist's name, then click the "Create Playlist" button. It will select the songs of the specified artist and create a new playlist.  

I have removed the "Client ID" and "Client Secret" information required to connect to Spotify from the code. If you are only going to use the "exe" file, you don't need to worry about it, but if you want to run the code, you will need to obtain this information from the Spotify Developer Portal and write it in the relevant place in the code.  

For the required modules, run the following command in the terminal:  
-Windows: pip install spotipy PyQt5  
-Linux/MacOS: pip3 install spotipy PyQt5  

Happy listening!  

# NOTE: Some antivirus programs may give false-positive results for the exe file. The code is completely clean. If you want, you can scan the code using AI tools like ChatGPT. The reasons for it being flagged as a virus include the fact that it was converted into an exe file using PyInstaller and the permissions requested by the Spotipy module from the Spotify API. Please do your research and ensure that it’s clean before running the code.
