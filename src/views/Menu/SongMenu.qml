import QtQuick 2.3
import QtQuick.Controls 1.2

Menu {
    id: root
    property var keyName
    property var keyType: "Song"
    property var playlistNames
    property var menuItems: []
    property var modelType // ['AllSongs', 'DetailSubSongs']

    MenuItem {
        text: MenuI18nWorker.play
        onTriggered: {
            SignalManager.playMusicByLocalUrl(keyName);
        }
    }

    MenuSeparator { }

    Menu {
        id: playlistMenu
        title: MenuI18nWorker.addToSinglePlaylist
    }

    MenuItem {
        text: MenuI18nWorker.addToMutiPlaylist
        onTriggered: {
            SignalManager.newMultiPlaylistDialogShowed(keyName, 'Song')
        }
    }

    MenuItem {
        text: MenuI18nWorker.newPlaylist
        onTriggered: {
            SignalManager.newPlaylistDialogShowed();
        }
    }

    MenuSeparator {}

    Menu {
        title: MenuI18nWorker.order
        MenuItem {
            text: MenuI18nWorker.orderBySongName
            onTriggered: {
                MenuWorker.orderByKey(modelType, 'title')
            }
        }
        MenuItem {
            text: MenuI18nWorker.orderByArtist
            onTriggered: {
                MenuWorker.orderByKey(modelType, 'artist')
            }
        }
        MenuItem {
            text: MenuI18nWorker.orderByAlbum
            onTriggered: {
                MenuWorker.orderByKey(modelType, 'album')
            }
        }
        MenuItem {
            text: MenuI18nWorker.orderByDuration
            onTriggered: {
                MenuWorker.orderByKey(modelType, 'duration')
            }
        }
        MenuItem {
            text: MenuI18nWorker.orderByPlayCount
            onTriggered: {
                MenuWorker.orderByKey(modelType, 'playCount')
            }
        }
        MenuItem {
            text: MenuI18nWorker.orderByAddTime
            onTriggered: {
                MenuWorker.orderByKey(modelType, 'created_date')
            }
        }
        MenuItem {
            text: MenuI18nWorker.orderByFileSize
            onTriggered: {
                MenuWorker.orderByKey(modelType, 'size')
            }
        }
    }

    MenuSeparator { }

    MenuItem {
        text: MenuI18nWorker.removeFromDatabase
        onTriggered: {
            if (keyType == "Artist"){
                MenuWorker.removeFromDatabaseByArtistName(keyName);
            }else if (keyType == "Album"){
                MenuWorker.removeFromDatabaseByAlbumName(keyName);
            }else if (keyType == "Folder"){
                MenuWorker.removeFromDatabaseByFolderName(keyName);
            }else if (keyType == "Song"){
                MenuWorker.removeFromDatabaseByUrl(keyName);
            }
        }
    }

    MenuItem {
        text: MenuI18nWorker.removeFromDriver
        onTriggered: {
            if (keyType == "Artist"){
                MenuWorker.removeFromDriverByArtistName(keyName);
            }else if (keyType == "Album"){
                MenuWorker.removeFromDriverByAlbumName(keyName);
            }else if (keyType == "Folder"){
                MenuWorker.removeFromDriverByFolderName(keyName);
            }else if (keyType == "Song"){
                MenuWorker.removeFromDriveByUrl(keyName);
            }
        }
    }

    MenuSeparator { }

    MenuItem {
        text: MenuI18nWorker.openFolder
        onTriggered: {
            MenuWorker.openSongFolder(keyName)
        }
    }

    MenuItem {
        text: MenuI18nWorker.information
        onTriggered: {
            SignalManager.informationShow(keyName)
        }
    }

    onPlaylistNamesChanged:{
        for(var i = 0 ; i< menuItems.length; i++){
            playlistMenu.removeItem(menuItems[i]);
        }
        menuItems.splice(0, menuItems.length);
        var names = [MenuI18nWorker.temporary, MenuI18nWorker.favorite]
        for (var i = 0 ; i< PlaylistWorker.playlistNames.length; i++){
            names.push(PlaylistWorker.playlistNames[i].name);
        }
        for (var i = 0 ; i< names.length; i++){
            var component = Qt.createComponent("./ChildMenuItem.qml");
            var playlistName;
            if (i == 0){
                playlistName = "temporary";
            }else if (i == 1){
                playlistName = "favorite";
            }else{
                playlistName = names[i];
            }
            var item = component.createObject(playlistMenu, {"keyName": keyName, "playlistName": playlistName, "keyType":keyType, "text": names[i]});
            if (item == null) {
                console.log("Error creating artist chile MenuItem object");
            }else{
                playlistMenu.insertItem(i, item);
                menuItems.push(item);
            }
        }
    }
}