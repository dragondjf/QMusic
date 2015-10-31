import QtQuick 2.3
import QtQuick.Controls 1.2

Menu {
    id: root
    property var currentPlaylistName

    MenuItem {
        text: MenuI18nWorker.playAll
        onTriggered: {
            MenuWorker.playFTAllSongs(currentPlaylistName);
        }
    }
}