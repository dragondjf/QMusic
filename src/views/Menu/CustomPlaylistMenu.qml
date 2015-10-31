import QtQuick 2.3
import QtQuick.Controls 1.2


Menu {
    id: root
    property var currentPlaylistName
    property var playlistNavigationIndex

    MenuItem {
        text: MenuI18nWorker.playAll
        onTriggered: {
        	print(currentPlaylistName, playlistNavigationIndex)
            MenuWorker.playNavigationAllSongs(currentPlaylistName, playlistNavigationIndex);
        }
    }
    MenuSeparator { }

    MenuItem {
        text: MenuI18nWorker.rename
        onTriggered: {
            print("Not implemented")
        }
    }

    MenuSeparator { }

    MenuItem {
        text: MenuI18nWorker.exportPlaylist
        onTriggered: {
            print("Not implemented")
        }
    }

    MenuItem {
        text: MenuI18nWorker.importPlaylist
        onTriggered: {
            print("Not implemented")
        }
    }

    MenuSeparator { }

    MenuItem {
        text: MenuI18nWorker.deletePlaylist
        onTriggered: {
            MenuWorker.deletePlaylist(currentPlaylistName);
        }
    }

}