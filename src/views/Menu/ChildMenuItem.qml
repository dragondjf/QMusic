import QtQuick 2.3
import QtQuick.Controls 1.2

MenuItem{
    property var keyName
    property var playlistName
    property var keyType
    onTriggered: {
        print(keyType)
        if (keyType == "Song"){
            MenuWorker.addSongToPlaylist(keyName, playlistName);
        }else if (keyType == "Artist" || keyType=="Album" || keyType == "Folder"){
            MenuWorker.addSongsToPlaylist(keyName, playlistName, keyType);
        }
    }
}