import QtQuick 2.3

Item {

    property var songsView
    property var songMenu

    Binding {
        target: songsView
        property: 'currentIndex'
        value: {
            var model = songsView.model
            for(var i=0; i<songsView.count; i++){
                if (model.get(i).url == MediaPlayer.url){
                    return i;
                }
            }
            return -1;
        }
    }

    Connections {
        target: songsView

        onPlayMusicByUrl: {
            SignalManager.playMusicByLocalUrl(url);
        }

        onMenuShowed:{
            songMenu.keyName = url;
            songMenu.playlistNames = PlaylistWorker.playlistNames;
            songMenu.popup();
        }
    }

}