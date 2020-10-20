import sys

from PyQt5.QtWidgets import QTabWidget, QMainWindow, QWidget, QApplication

from Rare.TabWidgets import Settings, GameListInstalled, BrowserTab, GameListUninstalled, UpdateList


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rare")
        self.setGeometry(0, 0, 800, 600)
        self.setCentralWidget(TabWidget(self))
        self.show()


class TabWidget(QTabWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)

        self.game_list = GameListInstalled(self)
        self.addTab(self.game_list, "Games")

        self.uninstalled_games = GameListUninstalled(self)
        self.addTab(self.uninstalled_games, "Install Games")

        self.update_tab = UpdateList(self)
        self.addTab(self.update_tab, "Updates")

        self.browser = BrowserTab(self)
        self.addTab(self.browser, "Store")

        self.settings = Settings(self)
        self.addTab(self.settings, "Settings")


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()