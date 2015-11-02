#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, pyqtProperty, QPoint, QUrl
from PyQt5.QtGui import QCursor, QDesktopServices
from .utils import registerContext, openLocalUrl
from dwidgets import ModelMetaclass
from log import logger
from .playlistworker import PlaylistWorker
from .signalmanager import signalManager


class MenuI18nWorker(QObject):

    __metaclass__ = ModelMetaclass

    __Fields__ = (('addMusic', 'QString', u'添加歌曲'),
                  ('simpleMode', 'QString', u'简洁模式'),
                  ('fullMode', 'QString', u'完整模式'),
                  ('file', 'QString', u'文件'),
                  ('folder', 'QString', u'文件夹'),
                  ('miniMode', 'QString', u'迷你模式'),
                  ('checkUpdate', 'QString', u'查看新特性'),
                  ('setting', 'QString', u'设置'),
                  ('exit', 'QString', u'退出'),
                  ('play', 'QString', u'播放'),
                  ('pause', 'QString', u'暂停'),
                  ('download', 'QString', u'下载'),
                  ('temporary', 'QString', u'试听歌单'),
                  ('favorite', 'QString', u'我的收藏'),
                  ('addToSinglePlaylist', 'QString', u'添加到歌单'),
                  ('addToMutiPlaylist', 'QString', u'添加到多个歌单'),
                  ('newPlaylist', 'QString', u'新建歌单'),
                  ('removeFromDatabase', 'QString', u'从歌库中移除'),
                  ('removeFromDriver', 'QString', u'从硬盘中移除'),
                  ('removeFromPlaylist', 'QString', u'从列表中移除'),
                  ('changeCover', 'QString', u'更换封面'),
                  ('order', 'QString', u'排序'),
                  ('orderBySongName', 'QString', u'按歌曲名'),
                  ('orderByArtist', 'QString', u'按歌手'),
                  ('orderByAlbum', 'QString', u'按专辑'),
                  ('orderByDuration', 'QString', u'曲长'),
                  ('orderByPlayCount', 'QString', u'按播放次数'),
                  ('orderByAddTime', 'QString', u'按添加时间'),
                  ('orderByFileSize', 'QString', u'按文件大小'),
                  ('openFolder', 'QString', u'打开目录'),
                  ('information', 'QString', u'信息'),
                  ('playAll', 'QString', u'播放全部'),
                  ('rename', 'QString', u'重命名'),
                  ('downloadAll', 'QString', u'下载全部'),
                  ('exportPlaylist', 'QString', u'导出歌单'),
                  ('importPlaylist', 'QString', u'导入歌单'),
                  ('deletePlaylist', 'QString', u'删除歌单'),
                  ('startDownload', 'QString', u'开始下载'),
                  ('pauseDownload', 'QString', u'暂停下载'),
                  ('deleteDownload', 'QString', u'删除下载'),
                  ('preivousSong', 'QString', u'上一首'),
                  ('nextSong', 'QString', u'下一首'),
                  ('playbackMode', 'QString', u'播放模式'),
                  ('random', 'QString', u'随机播放'),
                  ('sequential', 'QString', u'顺序播放'),
                  ('currentItemInLoop', 'QString', u'单曲循环'),
                  ('windowMode', 'QString', u'窗口模式'),
                  ('showDesktopLrc', 'QString', u'打开桌面歌词'),
                  ('hideDesktopLrc', 'QString', u'关闭桌面歌词'),
                  ('lockDesktopLrc', 'QString', u'锁定桌面歌词'),
                  ('unlockDesktopLrc', 'QString', u'解锁桌面歌词'), )

    __contextName__ = "MenuI18nWorker"

    @registerContext
    def initialize(self, *agrs, **kwargs):
        pass


class MenuWorker(QObject):

    __contextName__ = 'MenuWorker'

    settingMenuShow = pyqtSignal('QString')
    artistMenuShow = pyqtSignal('QString')
    albumMenuShow = pyqtSignal('QString')
    songMenuShow = pyqtSignal('QString', 'QString')
    folderMenuShow = pyqtSignal('QString')
    playlistLocalSongMenuShow = pyqtSignal('QString', 'QString')
    playlistOnlineSongMenuShow = pyqtSignal('QString', 'QString', int)
    playlistNavigationMenuShow = pyqtSignal('QString', int)
    ftPlaylistNavigationMenuShow = pyqtSignal('QString')
    temporaryMenuShowed = pyqtSignal('QString', 'QString')
    downloadMenuShowed = pyqtSignal(int, bool)

    #setting Menu
    simpleTrigger = pyqtSignal()
    fullTrigger = pyqtSignal()
    miniTrigger = pyqtSignal()
    addSongFile = pyqtSignal()
    addSongFolder = pyqtSignal()
    updateTrigger = pyqtSignal()
    settingTrigger = pyqtSignal()
    exitTrigger = pyqtSignal()

    #Artist Menu
    playArtist = pyqtSignal('QString')
    removeFromDatabaseByArtistName = pyqtSignal('QString')
    removeFromDriverByArtistName = pyqtSignal('QString')

    #Album Menu
    playAlbum = pyqtSignal('QString')
    removeFromDatabaseByAlbumName = pyqtSignal('QString')
    removeFromDriverByAlbumName = pyqtSignal('QString')

    #Song Menu
    orderByKey = pyqtSignal('QString', 'QString')
    openSongFolder = pyqtSignal('QString')
    removeFromDatabaseByUrl = pyqtSignal('QString')
    removeFromDriveByUrl = pyqtSignal('QString')

    #Folder Menu
    playFolder = pyqtSignal('QString')
    removeFromDatabaseByFolderName = pyqtSignal('QString')
    removeFromDriverByFolderName = pyqtSignal('QString')

    #playlist menu:
    playMusicByUrl = pyqtSignal('QString')
    removeFromPlaylist = pyqtSignal('QString', 'QString')

    #playlist navigation menu
    playFTAllSongs = pyqtSignal('QString')
    playNavigationAllSongs = pyqtSignal('QString', int)
    deletePlaylist = pyqtSignal('QString')

    # temporary menu
    playMusicInTemporary = pyqtSignal('QString')

    #download menu
    switchDownloadedStatus = pyqtSignal(int, bool)
    playMusicByIdSignal = pyqtSignal(int)
    removeFromDownloadList = pyqtSignal(int)

    #search menu
    searchLocalSongShowed = pyqtSignal('QString')

    #systemTray:
    systemTrayMenuShowed = pyqtSignal()

    #public menu:
    addSongToPlaylist = pyqtSignal('QString', 'QString')
    addSongsToPlaylist = pyqtSignal('QString', 'QString', 'QString')

    @registerContext
    def __init__(self):
        super(MenuWorker, self).__init__()


menuWorker = MenuWorker()
menuI18nWorker = MenuI18nWorker()
