#!/usr/bin/python
import neverwise as nw, os#, datetime


class SkyTg24(object):

  def __init__(self):

    li = nw.createListItem(nw.addonName, thumbnailImage = '{0}/icon.png'.format(os.path.dirname(os.path.abspath(__file__))), streamtype = 'video', infolabels = { 'title' : nw.addonName })
    # rtmp://cp49989.live.edgefcs.net:1935/live/streamRM1@2564 app=live playpath=streamRM1@2564 swfUrl=http://videoplatform.sky.it/player/swf/player_v2.swf pageURL=http://video.sky.it/news/diretta swfVfy=true live=true timeout=30 flashVer=LNX 11,2,202,297
    xbmc.Player().play('rtmp://cp49989.live.edgefcs.net:1935/live/streamRM1@2564 live=true', li)

# Entry point.
#startTime = datetime.datetime.now()
st24 = SkyTg24()
del st24
#xbmc.log('{0} azione {1}'.format(nw.addonName, str(datetime.datetime.now() - startTime)))
