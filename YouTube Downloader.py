#!/usr/bin/env python
# coding: utf-8

# In[3]:


""""
      # YouTube Downloader
 -Download Any Video From YouTube Using This Code 
 
 -Just Install pytube module 
 
 -Paste the link of video which you want to download
      


""""

from pytube import YouTube
link=input("Enter The Link:")
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download()


# In[ ]:




