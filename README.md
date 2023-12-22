# **Venatus Discord Bot**
## **CAUTION BEFORE RUNNING**<br />
-> Change all "single back slash" in path used in windows to "/" for linux or error occurs (-in file votebot.py path to the asset image)
<br /><br />
->For windows add  'executable': r"./assets/ffmpeg/bin/ffmpeg.exe", in the FFMPEG settings and for linux no need to add this.<br><br>
## *DEPENDANCE PRE-REQUISITES MAYBE NEEDED AND FIXES*<br />
-> pip3 install youtube-search-python
-> pip3 install pytube 
-> INSTALL FFMPEG IN LINUX by using 'sudo apt-get install ffmpeg' only and in windows use FFMPEG exe files and store in assets folder.<br />
-> If bot dont join voice channel refer to https://github.com/Rapptz/discord.py/issues/337 . In short use command 'python3 -m pip install -U discord.py[voice]'<br />
-> If the youtube_dl is still not fixed in future then refer to this post https://github.com/ytdl-org/youtube-dl/issues/32226#:~:text=i%20used%20then-,here,-it%20is%20( 
     and download the Source Code.zip from https://github.com/ytdl-patched/youtube-dl/releases using wget command and download ling after wget. Then copy the "youtube_dl"      folder inside the main folder which has "Youtube_DL.py" and paste the youtube_dl folder in the library path replacing the pip installed version of youtube_dl.<br />


<br /><br />
## **FOR CONVERSION HELP**<br />
-> bot.event --> commands.Cog.listener <br />              
-> bot.command --> commands.command <br />                               
-> ctx.response.send_message(embed=embed) --> ctx.channel.send(embed=embed) <br />

-> Bot_token.py in gitignore<br />
-> Ffmpeg folder in gitignore for windows and for linux install ffmpeg<br />

<br /><br />
## **FOR ANY FURTHER ISSUE CONTACT THE WORKING TEAM or Not_Blackbuck#4912 on discord**<br />

