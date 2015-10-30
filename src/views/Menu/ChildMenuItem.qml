import QtQuick 2.3
import QtQuick.Controls 1.2

MenuItem{
    property var keyName
    property var playlistName
    property var keyType
    onTriggered: {
        MenuWorker.addSongsToPlaylist(keyName, playlistName, keyType)
    }
}