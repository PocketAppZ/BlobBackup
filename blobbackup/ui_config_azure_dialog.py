# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config_azure_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConfigAzureDialog(object):
    def setupUi(self, ConfigAzureDialog):
        if not ConfigAzureDialog.objectName():
            ConfigAzureDialog.setObjectName(u"ConfigAzureDialog")
        ConfigAzureDialog.resize(400, 291)
        self.verticalLayout = QVBoxLayout(ConfigAzureDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(ConfigAzureDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.label)

        self.name_line_edit = QLineEdit(self.widget)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.horizontalLayout.addWidget(self.name_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.password_line_edit = QLineEdit(self.widget)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.password_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.confirm_password_line_edit = QLineEdit(self.widget)
        self.confirm_password_line_edit.setObjectName(u"confirm_password_line_edit")
        self.confirm_password_line_edit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.confirm_password_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.label_4)

        self.connection_line_edit = QLineEdit(self.widget)
        self.connection_line_edit.setObjectName(u"connection_line_edit")
        self.connection_line_edit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.connection_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_6.addWidget(self.label_6)

        self.container_line_edit = QLineEdit(self.widget)
        self.container_line_edit.setObjectName(u"container_line_edit")

        self.horizontalLayout_6.addWidget(self.container_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_7.addWidget(self.label_7)

        self.prefix_line_edit = QLineEdit(self.widget)
        self.prefix_line_edit.setObjectName(u"prefix_line_edit")

        self.horizontalLayout_7.addWidget(self.prefix_line_edit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignTop)

        self.buttonBox = QDialogButtonBox(ConfigAzureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ConfigAzureDialog)
        self.buttonBox.accepted.connect(ConfigAzureDialog.accept)
        self.buttonBox.rejected.connect(ConfigAzureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigAzureDialog)
    # setupUi

    def retranslateUi(self, ConfigAzureDialog):
        ConfigAzureDialog.setWindowTitle(QCoreApplication.translate("ConfigAzureDialog", u"Configure Microsoft Azure", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("ConfigAzureDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Backup Name:</span></p><p>Something descriptive to help you remember what this backup contains (eg: My Pictures).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("ConfigAzureDialog", u"Backup Name:", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("ConfigAzureDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Password:</span></p><p>Your data will be encrypted with this. Make sure to write it down. You will LOSE YOUR DATA if you lose this password.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("ConfigAzureDialog", u"Password:", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("ConfigAzureDialog", u"<html><head/><body><p>Re-type your password.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("ConfigAzureDialog", u"Confirm:", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("ConfigAzureDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Connection:</span></p><p>The connection string for your container. This can be found in the Azure web portal.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("ConfigAzureDialog", u"Connection:", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("ConfigAzureDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Container:</span></p><p>The name of your storage container on Azure. It must already exist. BlobBackup will not create containers for you.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("ConfigAzureDialog", u"Container:", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("ConfigAzureDialog", u"<html><head/><body><p><span style=\" font-weight:600;\">Prefix:</span></p><p>The path that will be added before every object that BlobBackup uploads.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("ConfigAzureDialog", u"Prefix:", None))
        self.label_5.setText(QCoreApplication.translate("ConfigAzureDialog", u"Note: hover mouse over label text for help.", None))
    # retranslateUi

