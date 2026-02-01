# How to use this RAG AI Teaching assistant on your own data
## Step 1 - Collect your videos
Move all your video files to the videos folder

## Step 2 - Convert to mp3
Convert all the video files to mp3 by ruunning videos_to_mp3.py

## Step 3 - Convert mp3 to json 
Convert all the mp3 files to json by ruunning mp3_to_json.py

## Step 4 - Convert the json files to Vectors
Use the file preprocess_json.py to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

## Step 5 - Prompt generation and feeding to LLM

Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it to the LLM using process_incoming.py

# Whisper model for transaltion from mp3/m4a to json file is kept in models/whisper folder 
Model is large-v2.pt

## For converting video files to audios we have used FFMPEG
## For converting audio file to json we have used whisper model
## For converting json files to vectors we have used Ollama bge-m3 and saved it to a joblib picklefile
## Loading the file through joblib and for inference with llm we have used Ollama phi4-mini model(also other models should be triend)
## phi4-mini came after 2-3 model testings.