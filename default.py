#!/usr/bin/python
import os
from neverwise import Util

li = Util.createListItem('Sky Tg24', os.path.dirname(os.path.abspath(__file__)) + '/icon.png', '', 'video', { 'title' : 'Sky Tg24', 'Genre' : 'Notizie' })
# rtmp://cp49989.live.edgefcs.net:1935/live/streamRM1@2564 app=live playpath=streamRM1@2564 swfUrl=http://videoplatform.sky.it/player/swf/player_v2.swf pageURL=http://video.sky.it/news/diretta swfVfy=true live=true timeout=30 flashVer=LNX 11,2,202,297
xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play('rtmp://cp49989.live.edgefcs.net:1935/live/streamRM1@2564 live=true', li)
