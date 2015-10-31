import QtQuick 2.3
import QtQuick.Controls 1.2

Menu {
    id: root
    property var url
    property var currentPlaylistName

    MenuItem {
        text: MenuI18nWorker.play
        onTriggered: {
            MenuWorker.playMusicInTemporary(url);
        }
    }

    MenuItem {
        text: MenuI18nWorker.removeFromPlaylist
        onTriggered: {
            MenuWorker.removeFromPlaylist(currentPlaylistName, url);
        }
    }
}