import QtQuick 2.3

Item {
    property var temporaryWindow
    property var playlistView
    property var songListModel
    property var clearButton
    property var closeButton
    property var temporyWindowMenu

    function init(){
        MediaPlayer.playlistChanged.connect(updateModel);
        MenuWorker.playMusicInTemporary.connect(playlistView.playMusicByUrl);
    }

    function playMusicByUrl(songUrl) {
        if (songUrl.indexOf('http') != -1){
            print(url)
        }else{
            MediaPlayer.playLocalMedia(songUrl);
        }
    }

    function clearCurrentPlaylist() {
        MediaPlayer.playlist.clearMedias()
    }

    function updateModel() {
        try {
            var pymodel = temporaryWindow.getModel();
            if (pymodel != null){
                songListModel.clear();
                songListModel.pymodel = pymodel;
                songListModel.initModel();
            }
        }catch(e) {

        }
    }

    Binding {
        target: playlistView
        property: 'currentIndex'
        value: {
            var playlist = MediaPlayer.playlist;
            if (playlist){
                return playlist.currentIndex;
            }else{
                return -1;
            }
        }
    }

    Connections {
        target: temporaryWindow
        onVisibleChanged: {
            if (visible){
                var pymodel = temporaryWindow.getModel()

                for(var i=0; i<pymodel.data.length; i++){
                    songListModel.set(i, pymodel.data[i])
                }
            }
        } 
    }

    Connections {
        target: playlistView
        onPlayMusicByUrl: playMusicByUrl(songUrl)
        onMenuShowed: {
            var playlist = MediaPlayer.playlist;
            if (playlist){
                var name = playlist.name
                temporyWindowMenu.url = songUrl;
                temporyWindowMenu.currentPlaylistName = name;
                temporyWindowMenu.popup();
            }


        }
        onModelChanged: playlistView.positionViewAtEnd()
    }

    Connections {
        target: clearButton
        onClicked: clearCurrentPlaylist() 
    }

    Component.onCompleted: {
        init();
    }
}
