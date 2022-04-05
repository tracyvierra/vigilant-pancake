# Author: Tracy Vierra
# Date Created: 3/30/2022
# Date Modified: 3/30/2022

# Description: a Python program that will transcribe given mp3 files to text

# Usage:

from functools import reduce
from pathlib import Path

import speech_recognition as sr
from pydub import AudioSegment


def transcribe(wav: Path, start_at=0, iteration=10):
    """Use start_at when transcription hangs and does not work."""
    transcription_path = wav.with_suffix('.txt')
    r = sr.Recognizer()
    with sr.AudioFile(str(wav)) as source, transcription_path.open('a') as out:
        print("STARTING TRANSCRIBING")
        duration = int(source.DURATION + iteration)
        duration_timecode = create_timecode(duration)
        time = start_at
        offset = start_at
        while time < duration:
            timecode = create_timecode(time)
            audio = r.record(source, duration=iteration, offset=offset)
            out.write(f"{timecode}: ")
            try:
                result = r.recognize_google(audio)
                out.write(result)
                print(f"{timecode}/{duration_timecode}")
            except sr.UnknownValueError:
                out.write("UNRECOGNIZABLE")
                print(f"{timecode}/{duration_timecode} FAILED")
            out.write('\n')
            out.flush()
            time += iteration
            offset = 0


def create_timecode(time):
    return f"{time // 60:0>2d}:{time % 60:0>2d}"


def to_seconds(*args):
    """
    to_seconds(seconds)
    to_seconds(1) => 1
    to_seconds(minutes, seconds)
    to_seconds(1, 00) => 60
    to_seconds(1, 1) => 61
    to_seconds(hours, minutes, seconds)
    to_seconds(1, 0, 0) => 3600
    """
    if len(args) > 3:
        raise ValueError("Days not supported")
    if len(args) == 0:
        return ValueError("No arguments supplied")
    return reduce(lambda result, x: result * 60 + x, args)


def mp3_to_wav(mp3: Path):
    print(f"Creating WAV from {str(mp3.absolute())}")
    sound = AudioSegment.from_mp3(str(mp3))
    wav_path = mp3.with_suffix('.wav')
    wav_str = str(wav_path)
    sound.export(wav_str, format="wav")
    print(f"CREATED WAV: {str(wav_path.absolute())}")
    return wav_path


if __name__ == '__main__':
    mp3_path = Path("transcript.mp3")
    wav_path = mp3_to_wav(mp3_path)
    transcribe(wav_path, start_at=to_seconds(0, 0))
