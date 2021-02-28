#Devloped By C15C01337 (Bishal Aryal)
#Follow me on Twitter username @C15C01337

print("Devloped By C15C01337 (Bishal Aryal)")
print("Follow me on Twitter username @C15C01337")

user_input = input("Enter url of video you want to download:")

import pafy #pip install pafy && youtube-dl


video =pafy.new(user_input)

#getting streams
streams = video.streams

for i in streams:
    print(i)


    #now its time to get best resolution
    best = video.getbest()

    print(best.resolution, best.extension)

    #Let's download the video

    best.download()
    print("Video from youtube downloaded succesfully.")
