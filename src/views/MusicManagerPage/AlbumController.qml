import QtQuick 2.3

Item {
    property var albumView
    property var albumMenu

    Connections {
        target: albumView
        onPlay: {
            MusicManageWorker.playAlbum(name)
        }

        onClicked:{
            MusicManageWorker.detailAlbum(name, index)
        }

        onRightClicked:{
            albumMenu.keyName = name;
            albumMenu.playlistNames = PlaylistWorker.playlistNames;
            albumMenu.popup();
        }
    }
}