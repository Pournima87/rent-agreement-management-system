import os
import tempfile
import subprocess

import speech_recognition as sr


FFMPEG_EXE = (
    r"C:\Users\DELL\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"
)



def convert_voice(
    audio_bytes
):


    # ==========================
    # Save microphone audio
    # ==========================

    with tempfile.NamedTemporaryFile(
        suffix=".webm",
        delete=False
    ) as webm_file:


        webm_file.write(
            audio_bytes
        )


        webm_path = webm_file.name



    wav_path = webm_path.replace(
        ".webm",
        ".wav"
    )


    # ==========================
    # Convert WEBM → WAV
    # ==========================

    subprocess.run(
        [
            FFMPEG_EXE,
            "-y",
            "-i",
            webm_path,
            wav_path
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


    # ==========================
    # Speech Recognition
    # ==========================

    recognizer = sr.Recognizer()


    with sr.AudioFile(
        wav_path
    ) as source:


        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )


        audio = recognizer.record(
            source
        )


    try:


        text = recognizer.recognize_google(
            audio,
            language="mr-IN"
        )


    except sr.UnknownValueError:


        text = "आवाज समजला नाही, पुन्हा बोला"


    except sr.RequestError:


        text = "Speech service error"



    # ==========================
    # Remove temp files
    # ==========================

    if os.path.exists(
        webm_path
    ):

        os.remove(
            webm_path
        )


    if os.path.exists(
        wav_path
    ):

        os.remove(
            wav_path
        )


    return text