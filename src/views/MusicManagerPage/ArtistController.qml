import QtQuick 2.3

Item {
    property var artistView
    property var artistMenu

    Connections {
        target: artistView
        onPlay: {
            MusicManageWorker.playArtist(name);
        }

        onClicked:{
            MusicManageWorker.detailArtist(name, index);
        }

        onRightClicked:{
            artistMenu.keyName = name;
            artistMenu.playlistNames = PlaylistWorker.playlistNames;
            artistMenu.popup();
        }
    }
}