import QtQuick 2.3

Item {
    property var folderView
    property var folderListModel
    property var folderMenu

    Connections {
        target: folderView
        onPlay: {
            MusicManageWorker.playFolder(folderListModel.get(index).name);
        }

        onClicked:{
            MusicManageWorker.detailFolder(name, index);
        }

        onRightClicked:{
            var name = folderListModel.get(index).name;
            folderMenu.keyName = name;
            folderMenu.playlistNames = PlaylistWorker.playlistNames;
            folderMenu.popup();
        }
    }

    Component.onCompleted: {

    }
}