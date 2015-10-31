import QtQuick 2.3
import DMusic 1.0
import QtQuick.Controls 1.3

Row {

    property alias keyText: keyLabel.text
    property alias valueText: valueLabel.text
    spacing: 20
    Label {
        id: keyLabel
        elide: Text.ElideRight
        horizontalAlignment: Text.AlignRight
        verticalAlignment: Text.AlignVCenter
        width: 80
        color: "#888888"
    }

    Label {
        id: valueLabel
        elide: Text.ElideRight
        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter
        width: 150
        color: "black"
    }

}
