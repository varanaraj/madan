import youtubetofacebook
import os
facebookApi = os.environ.get('FB_YOUTUBE_ACCESS', None)
def Run():
    channel = youtubetofacebook.youtubetofb("https://www.youtube.com/c/madangowri",
                                            facebookApi, "SirichchaPochchu")

    if(channel.haveNewVideo()):
        channel.downloadVideo()
        channel.uploadVideo()