import QtQuick 2.3
import QtQuick.Controls 1.2

Menu {

    Menu {
        title: MenuI18nWorker.addMusic

        MenuItem {
            text: MenuI18nWorker.file
            onTriggered: {
                MenuWorker.addSongFile();
            }
        }

        MenuItem {
            text: MenuI18nWorker.folder
            onTriggered: {
                MenuWorker.addSongFolder();
            }
        }
    }

    MenuSeparator { }

    MenuItem {
        text: WindowManageWorker.windowMode == "Full" ? MenuI18nWorker.simpleMode : MenuI18nWorker.fullMode
        onTriggered: {
            if (WindowManageWorker.windowMode == "Full"){
                MenuWorker.simpleTrigger();
            }else if (WindowManageWorker.windowMode == "Simple"){
                MenuWorker.fullTrigger();
            }
        }
    }

    MenuItem {
        text: MenuI18nWorker.miniMode
        onTriggered: {
            MenuWorker.miniTrigger();
        }
    }

    MenuSeparator {}

    MenuItem {
        text: MenuI18nWorker.checkUpdate
        onTriggered: {
            MenuWorker.updateTrigger();
        }
    }

    MenuItem {
        text: MenuI18nWorker.setting
        onTriggered: {
            MenuWorker.settingTrigger();
        }
    }

    MenuSeparator { }

    MenuItem {
        text: MenuI18nWorker.exit
        onTriggered: {
            MenuWorker.exitTrigger();
        }
    }

    
}