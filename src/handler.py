#!/usr/bin/env python3
import runpod
from AIvoifu.client_pipeline import tts_pipeline
import uuid
import base64 # for encoding the audio file
import os # for removing the temp file
import shutil
model = tts_pipeline(tts_model_selection='gtts', vc_model_selection='ayaka-jp', hubert_model='zomehwh-hubert-base', language='en')
def handler(job):
    name = str(uuid.uuid4()) # this is to be the audio name, it'll be unique most of the time
    fpath = f'audio_cache/{name}.wav'  
    try:  
        job_input = job['input']

        text = job_input.get('text')
        if text is None or not isinstance(text, str):
            return {'error': 'text is required'}
        
        os.makedirs('audio_cache', exist_ok=True)
        model.tts(text, voice_conversion=True, save_path=fpath) # saved to file as there's no return bytes by the current version of AIvoifu
        with open(fpath, 'rb') as f:
            audio = f.read()
        os.remove(fpath) # remove the temp file
        return {'audio': base64.b64encode(audio).decode('utf-8')}
    except Exception as e: # if anything goes wrong, return an error, remove the temp file
        if os.path.exists(fpath):
            os.remove(fpath)
        return {'error': str(e)}

runpod.serverless.start({"handler": handler})