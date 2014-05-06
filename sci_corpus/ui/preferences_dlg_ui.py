# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferences_dlg.ui'
#
# Created: Thu May  1 20:18:58 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_Preferences(object):

    def setupUi(self, Preferences):
        Preferences.setObjectName("Preferences")
        Preferences.setWindowModality(QtCore.Qt.WindowModal)
        Preferences.resize(500, 380)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            Preferences.sizePolicy().hasHeightForWidth())
        Preferences.setSizePolicy(sizePolicy)
        Preferences.setMinimumSize(QtCore.QSize(500, 380))
        Preferences.setMaximumSize(QtCore.QSize(500, 380))
        self.gridLayout_2 = QtGui.QGridLayout(Preferences)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBoxWorkspace = QtGui.QGroupBox(Preferences)
        self.groupBoxWorkspace.setObjectName("groupBoxWorkspace")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBoxWorkspace)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtGui.QLabel(self.groupBoxWorkspace)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditWorkspace = QtGui.QLineEdit(self.groupBoxWorkspace)
        self.lineEditWorkspace.setObjectName("lineEditWorkspace")
        self.gridLayout_4.addWidget(self.lineEditWorkspace, 0, 1, 1, 1)
        self.checkBoxCreateDir = QtGui.QCheckBox(self.groupBoxWorkspace)
        self.checkBoxCreateDir.setObjectName("checkBoxCreateDir")
        self.gridLayout_4.addWidget(self.checkBoxCreateDir, 1, 1, 1, 1)
        self.checkBoxOpenLast = QtGui.QCheckBox(self.groupBoxWorkspace)
        self.checkBoxOpenLast.setObjectName("checkBoxOpenLast")
        self.gridLayout_4.addWidget(self.checkBoxOpenLast, 2, 1, 1, 1)
        self.pushButtonWorkspace = QtGui.QPushButton(self.groupBoxWorkspace)
        self.pushButtonWorkspace.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pushButtonWorkspace.setObjectName("pushButtonWorkspace")
        self.gridLayout_4.addWidget(self.pushButtonWorkspace, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBoxWorkspace, 2, 0, 1, 1)
        self.groupBoxAppearance = QtGui.QGroupBox(Preferences)
        self.groupBoxAppearance.setObjectName("groupBoxAppearance")
        self.gridLayout = QtGui.QGridLayout(self.groupBoxAppearance)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtGui.QLabel(self.groupBoxAppearance)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBoxAppearance)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBoxTheme = QtGui.QComboBox(self.groupBoxAppearance)
        self.comboBoxTheme.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBoxTheme.setSizeAdjustPolicy(
            QtGui.QComboBox.AdjustToContents)
        self.comboBoxTheme.setObjectName("comboBoxTheme")
        self.comboBoxTheme.addItem("")
        self.comboBoxTheme.addItem("")
        self.gridLayout.addWidget(self.comboBoxTheme, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(
            40,
            20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBoxAppearance, 0, 0, 1, 3)
        self.groupBoxSentenceStrip = QtGui.QGroupBox(Preferences)
        self.groupBoxSentenceStrip.setObjectName("groupBoxSentenceStrip")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBoxSentenceStrip)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBoxReplace = QtGui.QComboBox(self.groupBoxSentenceStrip)
        self.comboBoxReplace.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBoxReplace.setInsertPolicy(QtGui.QComboBox.NoInsert)
        self.comboBoxReplace.setSizeAdjustPolicy(
            QtGui.QComboBox.AdjustToContents)
        self.comboBoxReplace.setObjectName("comboBoxReplace")
        self.comboBoxReplace.addItem("")
        self.comboBoxReplace.addItem("")
        self.gridLayout_3.addWidget(self.comboBoxReplace, 2, 1, 1, 1)
        self.labelMarker = QtGui.QLabel(self.groupBoxSentenceStrip)
        self.labelMarker.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelMarker.setObjectName("labelMarker")
        self.gridLayout_3.addWidget(self.labelMarker, 0, 0, 1, 1)
        self.comboBoxMarker = QtGui.QComboBox(self.groupBoxSentenceStrip)
        self.comboBoxMarker.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBoxMarker.setObjectName("comboBoxMarker")
        self.comboBoxMarker.addItem("")
        self.comboBoxMarker.addItem("")
        self.comboBoxMarker.addItem("")
        self.gridLayout_3.addWidget(self.comboBoxMarker, 0, 1, 1, 1)
        self.labelReplace = QtGui.QLabel(self.groupBoxSentenceStrip)
        self.labelReplace.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelReplace.setObjectName("labelReplace")
        self.gridLayout_3.addWidget(self.labelReplace, 2, 0, 1, 1)
        self.lineEditReplaceBy = QtGui.QLineEdit(self.groupBoxSentenceStrip)
        self.lineEditReplaceBy.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEditReplaceBy.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEditReplaceBy.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditReplaceBy.setObjectName("lineEditReplaceBy")
        self.gridLayout_3.addWidget(self.lineEditReplaceBy, 1, 1, 1, 1)
        self.labelReplaceBy = QtGui.QLabel(self.groupBoxSentenceStrip)
        self.labelReplaceBy.setMinimumSize(QtCore.QSize(100, 0))
        self.labelReplaceBy.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.labelReplaceBy.setObjectName("labelReplaceBy")
        self.gridLayout_3.addWidget(self.labelReplaceBy, 1, 0, 1, 1)
        self.labelImportant = QtGui.QLabel(self.groupBoxSentenceStrip)
        self.labelImportant.setObjectName("labelImportant")
        self.gridLayout_3.addWidget(self.labelImportant, 0, 2, 3, 1)
        self.gridLayout_2.addWidget(self.groupBoxSentenceStrip, 1, 0, 1, 3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtGui.QSpacerItem(
            40,
            20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonCancel = QtGui.QPushButton(Preferences)
        self.pushButtonCancel.setMaximumSize(QtCore.QSize(85, 16777215))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.pushButtonOk = QtGui.QPushButton(Preferences)
        self.pushButtonOk.setMaximumSize(QtCore.QSize(85, 16777215))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 3)

        self.retranslateUi(Preferences)
        QtCore.QMetaObject.connectSlotsByName(Preferences)

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(
            QtGui.QApplication.translate(
                "Preferences",
                "Preferences",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.groupBoxWorkspace.setTitle(
            QtGui.QApplication.translate(
                "Preferences",
                "Workspace",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate(
                "Preferences",
                "Directory:",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.checkBoxCreateDir.setText(
            QtGui.QApplication.translate(
                "Preferences",
                "Create \"Sci Corpus\" directory",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.checkBoxOpenLast.setText(
            QtGui.QApplication.translate(
                "Preferences",
                "Open last opened DB when starts",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonWorkspace.setText(
            QtGui.QApplication.translate(
                "Preferences",
                "...",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.groupBoxAppearance.setTitle(
            QtGui.QApplication.translate(
                "Preferences",
                "Appearance",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(
            QtGui.QApplication.translate(
                "Preferences",
                "It needs restart application",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate(
                "Preferences",
                "Theme: ",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTheme.setItemText(
            0,
            QtGui.QApplication.translate(
                "Preferences",
                "White",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.comboBoxTheme.setItemText(
            1,
            QtGui.QApplication.translate(
                "Preferences",
                "Black",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.groupBoxSentenceStrip.setTitle(
            QtGui.QApplication.translate(
                "Preferences",
                "Sentence Strip Dealer",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.comboBoxReplace.setItemText(
            0,
            QtGui.QApplication.translate(
                "Preferences",
                "Inside markers",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.comboBoxReplace.setItemText(
            1,
            QtGui.QApplication.translate(
                "Preferences",
                "Outside markers",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelMarker.setText(
            QtGui.QApplication.translate(
                "Preferences",
                "Marker:",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.comboBoxMarker.setItemText(
            0,
            QtGui.QApplication.translate(
                "Preferences",
                "{{}}",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.comboBoxMarker.setItemText(
            1,
            QtGui.QApplication.translate(
                "Preferences",
                "{}",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.comboBoxMarker.setItemText(
            2,
            QtGui.QApplication.translate(
                "Preferences",
                "[ ]",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelReplace.setText(
            QtGui.QApplication.translate(
                "Preferences",
                "Replace: ",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.lineEditReplaceBy.setText(
            QtGui.QApplication.translate(
                "Preferences",
                "...",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelReplaceBy.setText(
            QtGui.QApplication.translate(
                "Preferences",
                "Replace By:",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.labelImportant.setText(
            QtGui.QApplication.translate(
                "Preferences",
                "<html><head/><body><p>Important: this function not <br>change your DB, it just adjust <br>the sentence to you visualize.</p></body></html>",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonCancel.setText(
            QtGui.QApplication.translate(
                "Preferences",
                "Cancel",
                None,
                QtGui.QApplication.UnicodeUTF8))
        self.pushButtonOk.setText(
            QtGui.QApplication.translate(
                "Preferences",
                "Ok",
                None,
                QtGui.QApplication.UnicodeUTF8))
