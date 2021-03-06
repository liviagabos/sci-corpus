#! python
# -*- coding: utf-8 -*-

"""
.. module:: preferences_dlg
   :platform: Unix, Windows
   :synopsis: Graphical interface preferences setup.

.. moduleauthor:: Daniel Pizetta <daniel.pizetta@usp.br>

Date: 01/05/2014 #@TODO: how to put this?

This script provides a graphical interface for preferences setup.

"""

from PySide.QtGui import QDialog, QFileDialog
import os
import platform

from sci_corpus.ui import preferences_dlg_ui


class PreferencesDialog(QDialog):

    """Preferences dialog."""

    def __init__(self, preferences, parent=None):
        """Contructor."""
        super(PreferencesDialog, self).__init__(parent)
        self.ui = preferences_dlg_ui.Ui_Preferences()
        self.ui.setupUi(self)
        self.preferences = preferences

        try:
            # Signals
            self.ui.pushButtonOk.clicked.connect(self.accept)
            self.ui.pushButtonCancel.clicked.connect(self.reject)
            self.ui.pushButtonWorkspace.clicked.connect(self.searchWorkspace)

            index = self.ui.comboBoxTheme.findText(self.preferences['theme'])
            self.ui.comboBoxTheme.setCurrentIndex(index)

            index = self.ui.comboBoxMarker.findText(self.preferences['marker'])
            self.ui.comboBoxMarker.setCurrentIndex(index)

            index = self.ui.comboBoxMode.findText(self.preferences['mode'])
            self.ui.comboBoxMode.setCurrentIndex(index)

            index = self.ui.comboBoxWhere.findText(self.preferences['where'])
            self.ui.comboBoxWhere.setCurrentIndex(index)

            self.ui.lineEditReplaceBy.setText(str(self.preferences['replace_by']))

        except Exception:
            pass
        finally:
            os_sys = platform.system()
            if os_sys == 'Windows':
                self.workspace = self.preferences['win_workspace']
            if os_sys == 'Linux':
                self.workspace = self.preferences['lin_workspace']
            if os_sys == 'Mac':
                self.workspace = self.preferences['mac_workspace']

            if self.workspace == '':
                self.workspace = os.path.abspath(os.path.expanduser('~'))

            self.ui.lineEditWorkspace.setText(str(self.workspace))
            self.ui.checkBoxOpenLast.setChecked(self.preferences['open_last'])
            # self.ui.checkBoxCreateDir.setChecked(True)
            self.ui.checkBoxCreateDir.clicked.connect(self.createDir)

    def createDir(self):
        """Create a directory for workspace."""
        create = self.ui.checkBoxCreateDir.isChecked()
        path = self.ui.lineEditWorkspace.text()
        if create:
            path = os.path.join(os.path.abspath(path), "Sci Corpus")
        else:
            path = os.path.splitext(os.path.dirname(path))[0]
        self.ui.lineEditWorkspace.setText(path)

    def searchWorkspace(self):
        """Seach a workspace."""
        path = QFileDialog.getExistingDirectory(
            self,
            self.tr('Choose a workspace for your Sci Corpus'),
            self.tr(self.workspace))
        if path != '':
            self.createDir()
            self.workspace = os.path.abspath(path)
            self.ui.lineEditWorkspace.setText(os.path.abspath(path))

    def accept(self):
        """Accept event."""
        self.preferences['theme'] = self.ui.comboBoxTheme.currentText()
        self.preferences['marker'] = str(self.ui.comboBoxMarker.currentText())
        self.preferences['where'] = str(self.ui.comboBoxWhere.currentText())
        self.preferences['mode'] = str(self.ui.comboBoxMode.currentText())
        self.preferences['replace_by'] = str(self.ui.lineEditReplaceBy.text())
        self.workspace = str(self.ui.lineEditWorkspace.text())

        os_sys = platform.system()
        if os_sys == 'Windows':
            self.preferences['win_workspace'] = self.workspace
        if os_sys == 'Linux':
            self.preferences['lin_workspace'] = self.workspace
        if os_sys == 'Mac':
            self.preferences['mac_workspace'] = self.workspace

        self.preferences['open_last'] = self.ui.checkBoxOpenLast.isChecked()

        if not os.path.exists(self.workspace):
            os.makedirs(self.workspace)

        QDialog.accept(self)

    def reject(self):
        """Reject event."""
        QDialog.reject(self)
