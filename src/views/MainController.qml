import QtQuick 2.3

Item {

    property var rootWindow
    property var mainWindow
    property var simpleWindowLoader
    property var miniWindow
    property var temporaryLoader
    property var constants

    function initConnect() {
        WindowManageWorker.mainWindowShowed.connect(showMainWindow);
        WindowManageWorker.simpleWindowShowed.connect(showSimpleWindow);
        WindowManageWorker.miniWindowShowed.connect(showMiniWindow);
        Qt.globalPos = WindowManageWorker.cursorPos;
        MenuWorker.simpleTrigger.connect(showSimpleWindow);
        MenuWorker.fullTrigger.connect(showMainWindow)
        MenuWorker.miniTrigger.connect(showMiniWindow);
        MenuWorker.settingTrigger.connect(loadSettingPage);
        MenuWorker.exitTrigger.connect(closeAll)

        SignalManager.informationDialogShowed.connect(showInformationWindow);
        // UnLockWindow.qPositionChanged.connect(updateLrcWindowPosition)
    }

    function showMainWindow() {
        MainWindow.show();
        rootWindow.width = constants.mainWindowWidth;
        rootWindow.height = constants.mainWindowHeight;
        mainWindow.visible = true;
        simpleWindowLoader.source = ''
        simpleWindowLoader.focus = false;

        miniWindow.visible = false;

        WindowManageWorker.windowMode = 'Full'
        WindowManageWorker.lastWindowMode = 'Full'
    }

    function showSimpleWindow() {
        MainWindow.show();
        rootWindow.width = constants.simpleWindowWidth;
        rootWindow.height = constants.simpleWindowHeight;
        mainWindow.visible = false;
        simpleWindowLoader.source = './SimpleWindow/SimpleWindow.qml';
        simpleWindowLoader.focus = true;

        miniWindow.visible = false;
        WindowManageWorker.windowMode = 'Simple'
        WindowManageWorker.lastWindowMode = 'Simple'
    }

    function showMiniWindow() {
        miniWindow.visible = true;
        MainWindow.hide();

        WindowManageWorker.windowMode = 'Mini'
    }

    function showInformationWindow(songObj) {
        print(songObj)
        var component = Qt.createComponent("./dialogs/InformationDialog.qml");  
        var item = component.createObject(rootWindow, {"songObj":songObj});
        if (item == null) {
            console.log("Error creating InformationDialog object");
        }else{
            item.visible = true;
            item.moveCenter();
            item.y = MainWindow.y;
        }
}

    function closeAll() {
        Qt.quit();
    }

    function destoryTermporyWindow(){
        temporaryLoader.source = ''
        mainWindow.focus = true;
    }

    function loadSettingPage(){
        WindowManageWorker.switchPageByID('SettingPage')
    }

    // function updateLrcWindowPosition(pos){
    //     lrcWindow.x = pos.x + (UnLockWindow.qSize.width - lrcWindow.width) / 2;
    //     lrcWindow.y = pos.y - lrcWindow.height;
    // }

	Connections {
        target: mainWindow.titleBar

        onSimpleWindowShowed: {
            showSimpleWindow();
        }

        onShowMinimized: {
            MainWindow.showMinimized()
        }

        onClosed: {
            closeAll();
        }
    }

    Connections {
        target: mainWindow.playBottomBar.playlistButton
        onClicked:{
            if (temporaryLoader.source == ''){
                temporaryLoader.source = './TemporaryWindow/TemporaryWindow.qml'
                temporaryLoader.focus = true;
                mainWindow.focus = false;
            }else{
                destoryTermporyWindow();
            }
        } 
    }

    Connections {
        target: mainWindow.playBottomBar.lrcButton
        onClicked:{
            SignalManager.lrcToggleShow();
        }
    }

    Connections {
        target: temporaryLoader
        onLoaded:{
            var temporyWindow = temporaryLoader.item;
            if (temporyWindow){
                var closeButton = temporyWindow.closeButton;
                closeButton.clicked.connect(destoryTermporyWindow);
            }
        }
    }

    Connections {
        target: miniWindow

        onExpandNoraml : {
            WindowManageWorker.showNormal();
        }

        onClosed:{
            closeAll();
        }
    }

    Component.onCompleted: {
        initConnect();
    }
}
