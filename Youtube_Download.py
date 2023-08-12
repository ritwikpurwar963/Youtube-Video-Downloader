from pytube import YouTube

url = "https://www.youtube.com/watch?v=d9MyW72ELq0"
my_video = YouTube(url)

print("*********************Video Title************************")
print(my_video.title)

print("********************Tumbnail Image***********************")
print(my_video.thumbnail_url)

print("********************Download video*************************")
#get all the stream resolution for the
for stream in my_video.streams:
    print(stream)

#set stream resolution
my_video = my_video.streams.get_highest_resolution()

#Download video
try:
    my_video.download()
except:
    print("An error occured")