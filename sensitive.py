#So, the idea is to:

#  Make an Instagram account
 #   Follow the best meme pages
  #  Write a script to login to our account, and then scrape and download all the videos these accounts posted in the last 24 hours. This can be done with Python and the Instagram API. I used 2 Python libraries called Instalooter and Instaloader to make this work.
# scrape_videos.py scrapes all the videos from pages we are following
def scrapeVideos(username = "",
                 password = "",
                 output_folder = "",
                 days = 1):
        
    print("Starting Scraping")

    L = instaloader.Instaloader()

    # Login or load session for loader
    L.login(username, password)  
    profile = instaloader.Profile.from_username(L.context, username)
    following = profile.get_followees()
    print(following)

    for profile in following:
        acc = profile.username
        looter = ProfileLooter(acc, videos_only=True, template="{id}-{username}-{width}-{height}")
        if not looter.logged_in():
            looter.login(username, password)
        print("Scraping From Account: " + acc)

        today = datetime.date.today()
        timeframe = (today, today - dateutil.relativedelta.relativedelta(days=days))
        numDowloaded = looter.download(output_folder, media_count=30, timeframe=timeframe)
        print("Downloaded " + str(numDowloaded) + " videos successfully")
        print("")

#This function will go through the list of accounts we are following, and then download all the videos they posted in the past 1 day to an output folder.
#3. Edit videos into a single compilation

#This part is pretty simple. We have all of our videos in a folder, and we want to edit them into a single compilation. This is not that bad, as we can just put each video one after another. To do this, we can use a Python library called moviepy.

# makeCompilation takes videos in a folder and creates a compilation with max length totalVidLength
def makeCompilation(path = "./",
                    introName = '',
                    outroName = '',
                    totalVidLength = 10*60,
                    maxClipLength = 20,
                    minClipLength = 5,
                    outputFile = "output.mp4"):

    allVideos = []
    seenLengths = defaultdict(list)
    totalLength = 0
    for fileName in os.listdir(path):
        if isfile(join(path, fileName)) and fileName.endswith(".mp4"):
            print(fileName)
            filePath = os.path.join(path, fileName)
            # Destination path  
            clip = VideoFileClip(filePath)
            clip = clip.resize(width=1920)
            clip = clip.resize(height=1080)
            duration = clip.duration
            print(duration)
            if duration <= maxClipLength and duration >= minClipLength:
                allVideos.append(clip)
                seenLengths[duration].append(fileName)
                totalLength += duration
    
    print("Total Length: " + str(totalLength))

    random.shuffle(allVideos)

    duration = 0
    # Add intro vid
    videos = []
    if introName != '':
        introVid = VideoFileClip("./" + introName)
        videos.append(introVid)
        duration += introVid.duration
    
    description = ""
    # Create videos
    for clip in allVideos:
        timeRange = generateTimeRange(duration, clip.duration)
        acc = extractAcc(clip.filename)
        description += timeRange + " : @" + acc + "\n"
        duration += clip.duration 
        videos.append(clip)
        print(duration)
        if duration >= totalVidLength:
            # Just make one video
            break
    
    # Add outro vid
    if outroName != '':
        outroVid = VideoFileClip("./" + outroName)
        videos.append(outroVid)

    finalClip = concatenate_videoclips(videos, method="compose")

    audio_path = "/tmp/temoaudiofile.m4a"

    #print(description)
    # Create compilation
    finalClip.write_videofile(outputFile, threads=8, temp_audiofile=audio_path, remove_temp=True, codec="libx264", audio_codec="aac")

    return description

#This function will look into the specified folder with videos, and combine them into a single video in random order. Now we have our meme compilation!
#4. Publish the video to Youtube

#We now have post it to Youtube automatically. To do this, we have to use the Youtube API. You will have to create a new Youtube Channel and complete the API Quick Start here carefully: https://developers.google.com/youtube/v3/getting-started

#Then, you can upload the video like this:

def uploadYtvid(VIDEO_FILE_NAME='',
                title='Intro Video!',
                description=':) ',
                tags=[],
                googleAPI=None):
    
    now = datetime.datetime.now()
    upload_date_time = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, int(now.second)).isoformat() + '.000Z'

    request_body = {
        'snippet': {
            'categoryId': 23,
            'title': title,
            'description': description,
            'tags': tags
        },
        'status': {
            'privacyStatus': 'public',
            'selfDeclaredMadeForKids': False, 
        },
        'notifySubscribers': False
    }

    mediaFile = MediaFileUpload(VIDEO_FILE_NAME, chunksize=-1, resumable=True)

    response_upload = googleAPI.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()

    """
    googleAPI.thumbnails().set(
        videoId=response_upload.get('id'),
        media_body=MediaFileUpload('thumbnail.png')
    ).execute()
    """

    print("Upload Successful!")

if __name__ == "__main__":
    uploadYtvid(VIDEO_FILE_NAME='./intro_vid.mp4')

#When you check on Youtube, the video should be posted on your channel!
#5. Cleanup

#If we run this every day and keep all of our videos on our computer, we will run out of storage eventually. So, we must delete the temporary files we created (which includes the compilation). We can do this with some Python:

# Step 4: Cleanup
    print("Removing temp files!")
    # Delete all files made:
    #   Folder videoDirectory
    shutil.rmtree(videoDirectory, ignore_errors=True)
    #   File outputFile
    try:
        os.remove(outputFile)
    except OSError as e:  ## if faile,d, report it back to the user ##
        print ("Error: %s - %s." % (e.filename, e.strerror))
    print("Removed temp files!")

#6. Putting it all together and repeating Steps 2–5

#Now, we have all the components we need. We can put it all into one function. This is main.py in the Github:

def routine():
    now = datetime.datetime.now()
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)
    title = "TRY NOT TO LAUGH (BEST Dank video memes) V1"
    videoDirectory = "./Memes_" + num_to_month[now.month].upper() + "_" + str(now.year) + "_V" + str(now.day) + "/"
    outputFile = "./" + num_to_month[now.month].upper() + "_" + str(now.year) + "_v" + str(now.day) + ".mp4"
    #metadataFile = "./metadata-" + num_to_month[now.month].upper() + "_" + str(now.year) + "_v" + str(now.day) + ".txt"
    description = ""
    print(outputFile)

    if not os.path.exists(videoDirectory):
        os.makedirs(videoDirectory)
    
    # Step 1: Scrape Videos
    print("Scraping Videos...")
    scrapeVideos(username = IG_USERNAME,
                 password = IG_PASSWORD,
                 output_folder = videoDirectory,
                 days=1)
    print("Scraped Videos!")
    
    description = "Enjoy the memes :) \n\n" \
    "like and subscribe for more \n\n" \

    # Step 2: Make Compilation
    print("Making Compilation...")
    makeCompilation(path = videoDirectory,
                    introName = INTRO_VID,
                    outroName = OUTRO_VID,
                    totalVidLength = TOTAL_VID_LENGTH,
                    maxClipLength = MAX_CLIP_LENGTH,
                    minClipLength = MIN_CLIP_LENGTH,
                    outputFile = outputFile)
    print("Made Compilation!")
    
    # Step 3: Upload to Youtube
    print("Uploading to Youtube...")
    uploadYtvid(VIDEO_FILE_NAME=outputFile,
                title=title,
                description=description,
                googleAPI=googleAPI)
    print("Uploaded To Youtube!")
    
    # Step 4: Cleanup
    print("Removing temp files!")
    # Delete all files made:
    #   Folder videoDirectory
    shutil.rmtree(videoDirectory, ignore_errors=True)
    #   File outputFile
    try:
        os.remove(outputFile)
    except OSError as e:  ## if failed, report it back to the user ##
        print ("Error: %s - %s." % (e.filename, e.strerror))
    print("Removed temp files!")

#We can then call:

#python3 main.py

#When we set our computer to never turn off (I use my really old computer for this), a new compilation video will be posted on our channel every day!