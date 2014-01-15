# Version 1.0.0 (02/12/2013)
# Sky Tg24
# Canale televisivo italiano all-news prodotto da Sky Italia.
# By NeverWise
# <mail>
# <url>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#######################################################################
import os, xbmc, tools

li = tools.createListItem('Sky Tg24', os.path.dirname(os.path.abspath(__file__)) + '/icon.png', '', 'video', { 'title' : 'Sky Tg24', 'Genre' : 'Notizie' })
# rtmp://cp49989.live.edgefcs.net:1935/live/streamRM1@2564 app=live playpath=streamRM1@2564 swfUrl=http://videoplatform.sky.it/player/swf/player_v2.swf pageURL=http://video.sky.it/news/diretta swfVfy=true live=true timeout=30 flashVer=LNX 11,2,202,297
xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).playStream('rtmp://cp49989.live.edgefcs.net:1935/live/streamRM1@2564 live=true', li)
