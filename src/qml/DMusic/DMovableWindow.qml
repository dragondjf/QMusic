import QtQuick 2.3
import QtQuick.Window 2.2

Window {
    id: rootWindow

    flags: Qt.FramelessWindowHint | Qt.Dialog | Qt.WindowStaysOnTopHint

    MouseArea {
        property int dragStartX
        property int dragStartY
        property int windowLastX
        property int windowLastY

        anchors.fill: parent
        propagateComposedEvents: true

        onPressed: {
            var pos = WindowManageWorker.cursorPos
            
            windowLastX = rootWindow.x
            windowLastY = rootWindow.y
            dragStartX = pos.x
            dragStartY = pos.y
        }

        onPositionChanged: {
            if (pressed) {
                var pos = WindowManageWorker.cursorPos
                rootWindow.x = (windowLastX + pos.x - dragStartX)
                rootWindow.y = (windowLastY + pos.y - dragStartY)
                windowLastX = rootWindow.x
                windowLastY = rootWindow.y
                dragStartX = pos.x
                dragStartY = pos.y
            }
        }
    }

    function moveCenter() {
        var height = Screen.desktopAvailableHeight;
        var width = Screen.desktopAvailableWidth;
        rootWindow.x = (width - rootWindow.width) / 2
        rootWindow.y = (height - rootWindow.height) / 2
    }
}