import QtQuick 2.3

Item {
    id: mainWindowController
    property bool isSearchBoxVisible: false
    property var mainWindow
    property var stackViews
    property var bgImage
    property var titleBar
    property var leftSideBar
    // property var webEngineViewPage
    property var playBottomBar
    property var dSimpleWindow
    property var searchPage
    property var searchInputBox
    property var searchInput: searchInputBox.searchInput

    property bool isDownload: {
        var url = MediaPlayer.url;
        var artist = MediaPlayer.artist;
        var title = MediaPlayer.title;
        if(url.indexOf('http') != -1){
            if (DownloadSongWorker.isOnlineSongExisted(artist, title)){
                return false;
            }else{
                return true;
            }
        }else{
            return false;
        }
        return false
    }

    function initConnect(){
        WindowManageWorker.switchPageByID.connect(leftSideBar.swicthViewByID);
        SignalManager.lrcSetting.connect(switchToSettingPage);
        SignalManager.addtoFavorite.connect(favoriteOn);
        SignalManager.removeFromFavorite.connect(favoriteOff);

        SignalManager.globalSearched.connect(showSearchPage)
        SignalManager.jumpToLocalDetailArtist.connect(showLocalDetailArtistPage)
    }

    function resetSkin() {
        playBottomBar.color = "#282F3F"
        bgImage.source = ''
    }


    function setSkinByImage(url) {
        if (url){
            bgImage.source = url
        }else{
            resetSkin();
        }
    }

    function favoriteOn(songUrl) {
        if (songUrl == MediaPlayer.url){
            playBottomBar.musicStarButton.isFavorite = true;
        }
    }

    function favoriteOff(songUrl) {
        if (songUrl == MediaPlayer.url){
            playBottomBar.musicStarButton.isFavorite = false;
        }
    }

    function getModelByPlaylistName(name){
        if (name){
            var model = eval('Playlist_' + Qt.md5(name));
            if (model){
                return model
            }else{
                return EmptyModel
            }
        }else{
            return EmptyModel
        }
    }

    function showSearchPage(keyword){
        var index =  mainWindow.views.indexOf('SearchPage');
        stackViews.setCurrentIndex(index);
    }

    function showLocalDetailArtistPage(name){
        var index =  mainWindow.views.indexOf('MusicManagerPage');
        stackViews.setCurrentIndex(index);
    }

    function switchToSettingPage(){
        var index =  mainWindow.views.indexOf('SettingPage');
        stackViews.setCurrentIndex(index);
    }


    Binding {
        target: playBottomBar.musicStarButton
        property: 'isFavorite'
        value: PlaylistWorker.isFavorite(MediaPlayer.url)
    }

    Binding {
        target: playBottomBar.musicDownloadButton
        property: 'visible'
        value: mainWindowController.isDownload
    }

    Binding {
        target: searchInputBox
        property: 'visible'
        value: isSearchBoxVisible
    }


    Binding {
        target: searchInput
        property: 'text'
        value: SearchWorker.keyword
    }

    Connections {
        target: searchInputBox
        onClosed:{
            isSearchBoxVisible = false;
        } 
    }


    Connections {
        target: searchInput
        onAccepted: {
            if (searchInput.text){
                SignalManager.globalSearched(searchInput.text);
                isSearchBoxVisible = true;
            }
        }

        onTextChanged:{
            searchTimer.restart();
        }
    }

    Timer {
        id: searchTimer
        interval: 100
        running: false
        onTriggered: {
            if (searchInput.text){
                SignalManager.globalSearched(searchInput.text);
                isSearchBoxVisible = true;
            }
        }
    }

    Connections {
        target: bgImage
        onProgressChanged:{
            if (progress == 1){
                playBottomBar.color = "transparent"
            }
        }
    }

    Connections {
        target: leftSideBar
        onSwicthViewByID: {
            var index =  mainWindow.views.indexOf(viewID);
            stackViews.setCurrentIndex(index);
        }

        onSearchButtonClicked:{
            isSearchBoxVisible = true;
        }
    }

    Connections {
        target: playBottomBar.musicStarButton
        onClicked:{
            var url = MediaPlayer.url;
            if (!playBottomBar.musicStarButton.isFavorite){
                SignalManager.addtoFavorite(url);
            }else{
                SignalManager.removeFromFavorite(url);
            }
        }
    }

    Connections {
        target: playBottomBar.musicDownloadButton
        onClicked:{
            var songId = MediaPlayer.songId;
            SignalManager.addtoDownloadlist(songId);
        }
    }

    Component.onCompleted: {
        initConnect();
    }
}
