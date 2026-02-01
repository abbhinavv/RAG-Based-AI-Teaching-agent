import os,subprocess

files = os.listdir('videos')

for file in files:
    file_number = file.split('.')[0].split('#')[1]
    file_name = file.split('_')[0]
    subprocess.run(['ffmpeg','-i' , f'videos/{file}', f'audios/{file_number}_{file_name}.mp3'])