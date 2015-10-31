import QtQuick 2.3
import DMusic 1.0
import "../Menu"

Rectangle {
    id: root

    SongListView {
        id: songListView
        datamodel: SongListModel
    }

    SongMenu {
        id: songMenu
        modelType: "AllSongs"
    }

    SongController {
        songsView: songListView.view
        songMenu: songMenu
    }
}