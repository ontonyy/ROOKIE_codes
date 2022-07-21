from pytube import YouTube

video_link = input("Enter the link: ")
yt = YouTube(video_link)

print("Title: ", yt.title)  # Number of views of video
print("Number of views: ", yt.views)  # Length of the video
print("Length of video: ", yt.length, "seconds")  # Description of video

ys = yt.streams.get_highest_resolution()

ys.download("videos/")

print("Download completed!!!")
