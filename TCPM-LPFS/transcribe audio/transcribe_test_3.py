# Author: Tracy Vierra
# Date Created: 3/30/2022
# Date Modified: 3/30/2022

# Description: a Python program that will transcribe given mp3 files to text

# Usage:

from types import FunctionType
from typing import Type
from PyQt5 import QtCore
from moviepy.editor import VideoFileClip
import os
from os import path
from mutagen.mp3 import MP3
import math
from pydub import AudioSegment
import speech_recognition
from scipy.io import wavfile
import numpy
import logging
import datetime


class Transcriber(QtCore.QObject):
    """
    MP3/MP4 files transcriber class.
    """
    finished = QtCore.pyqtSignal()
    init_progress = QtCore.pyqtSignal(int)
    tsb_progress = QtCore.pyqtSignal(int)

    def __init__(self) -> None:
        super().__init__()
        self.transcription = ""

    def run(self, file_path: str, language: str = "it-IT") -> None:
        """
        Main function executed by the transcriber.

        Parameters
        ----------
        file_path : str
            Path of the MP3 or MP4 file to transcribe.
        language : str, optional
            Language to consider in transcription, by default "it-IT"
        """
        self.transcription = self._get_transcription(file_path=file_path,
                                                     language=language)
        self.finished.emit()

    def update_init_progress(self, percent: float) -> None:
        """
        Updates the file initialization progress bar.

        Parameters
        ----------
        percent : float
            New percentage value to set.
        """
        self.init_progress.emit(percent)

    def update_tsb_progress(self, percent: float) -> None:
        """
        Updates the file transcription progress bar.

        Parameters
        ----------
        percent : float
            New percentage value to set.
        """
        self.tsb_progress.emit(percent)

    def _get_transcription(self,
                           file_path: str,
                           language: str = "it-IT") -> str:
        """
        Transcribes the file located on file_path.

        Parameters
        ----------
        file_path : str
            Path of the MP3 or MP4 file to transcribe.
        language : str, optional
            Language to consider in transcription, by default "it-IT"

        Returns
        -------
        str
            Transcripted test

        Raises
        ------
        ValueError
            If the file is not an mp3 or mp4 file.
        """

        # file type check
        if not (file_path.endswith(".mp3") or file_path.endswith(".mp4")):
            raise ValueError("Only .mp3 or .mp4 files are accepted.")
        else:
            self.update_init_progress(percent=16)

        # mp4 to mp3
        if file_path.endswith(".mp4"):
            mp3_to_delete = True
            file_path = self._mp4_to_mp3(mp4_file_path=file_path)
        else:
            mp3_to_delete = False

        self.update_init_progress(percent=32)

        transcription = self._mp3_to_txt(mp3_file_path=file_path,
                                         language=language,
                                         save_file=False,
                                         mp3_to_delete=mp3_to_delete)
        return transcription

    def _mp4_to_mp3(self, mp4_file_path: str) -> str:
        """
        Converts an MP4 file to an MP3 format

        Parameters
        ----------
        mp4_file_path : str
            MP4 file full path.

        Returns
        -------
        str
            MP3 file full path.

        Raises
        ------
        ValueError
            If input file is not an .mp4 file.
        """
        if not mp4_file_path.endswith(".mp4"):
            raise ValueError("Input file is not an .mp4 file.")
        else:
            # gets mp3 file path being sure to not overwrite an existing file
            base_file_path = mp4_file_path[:mp4_file_path.rfind(".mp4")]
            mp3_file_path = "".join((base_file_path, ".mp3"))

            while os.path.exists(mp3_file_path):
                base_file_path = "".join(base_file_path, str(
                    datetime.datetime.now().timestamp()))
                mp3_file_path = "".join((base_file_path, ".mp3"))

            # converts the mp4 into an mp3 and saves it on a file
            logging.info("Converting .mp4 to .mp3...")
            video = VideoFileClip(mp4_file_path)  # path.join(mp4_file_path)
            video.audio.write_audiofile(mp3_file_path)
            video.audio.close()
            logging.info(".mp4 file converted to .mp3.")

        return mp3_file_path

    def _mp3_to_txt(self,
                    mp3_file_path: str,
                    language: str = "it-IT",
                    save_file: bool = False,
                    mp3_to_delete: bool = False) -> str:
        """
        Transcribes an MP3 file.

        Parameters
        ----------
        mp3_file_path : str
             MP3 file full path.
        language : str, optional
            Language to consider in transcription, by default "it-IT"
        save_file : bool, optional
            If True, transcription is automatically saved on the same
            directory of source MP3 file, by default False.
        mp3_to_delete : bool, optional
            If True, MP3 file is deleted after use, by default False.

        Returns
        -------
        str
            Transcripted test.

        Raises
        ------
        ValueError
            If input file is not an .mp3 file.
        """

        S_PER_STEP = 200
        """
        Audio seconds per transcription step.
        """

        tsb_list = []
        """
        List of transcripted frames.
        """
        # input file type check
        if not mp3_file_path.endswith(".mp3"):
            raise ValueError("Input file is not an .mp3 file.")

        # generation of the list of audio records to transcribe
        audio_list = self._generate_audio_records(mp3_file_path=mp3_file_path,
                                                  s_per_step=S_PER_STEP,
                                                  mp3_to_delete=mp3_to_delete)

        self.update_init_progress(percent=100)

        r = speech_recognition.Recognizer()

        # audio records transcription
        for step, audio in enumerate(audio_list):

            # gui update informations
            self.update_tsb_progress(percent=int(step/(len(audio_list))*100))
            d = S_PER_STEP if step != len(audio_list)-1 else None
            logging.info(
                f"From {step*S_PER_STEP} s to {' '.join((str((step+1)*S_PER_STEP), 's'))  if d else 'end'}")

            method = "recognize_google"

            try:
                logging.info(
                    f"Transcripting file step {step +1} of {len(audio_list)}...")
                result = str(r.recognize_google(audio, language=language))

            except speech_recognition.RequestError:
                logging.info(
                    f"{method} (step {step +1} of {len(audio_list)}). Error: API unavailable")
                result = ""

            except speech_recognition.UnknownValueError:
                logging.info(
                    f"{method} (step {step +1} of {len(audio_list)}). Error: Unable to recognize speech")
                result = ""

            except Exception as e:
                logging.info(
                    f"{method} (step {step +1} of {len(audio_list)}). Error: Got exception {e}")
                result = ""

            else:
                logging.info(
                    f"{method} (step {step +1} of {len(audio_list)}): Transcription completed successfully.")

            finally:
                tsb_list.append(result)
                if step == len(audio_list)-1:
                    self.update_tsb_progress(percent=100)
                else:
                    self.update_tsb_progress(percent=int(
                        (step+1)/(len(audio_list))*100))

        transcription = " ".join(tsb_list)

        # txt file saving
        if save_file:
            with open(f"{mp3_file_path}_tsb.txt", "w") as file:
                file.write(transcription)

        self.update_tsb_progress(percent=100)

        return transcription

    def _generate_audio_records(self,
                                mp3_file_path: str,
                                s_per_step: int,
                                mp3_to_delete: bool) -> list:
        """
        Generates a list of audio records to transcribe from .mp3 file

        Parameters
        ----------
        mp3_file_path : str
            .mp3 file full path
        s_per_step : int
            Duration of each audio record [s]. 
        mp3_to_delete : bool
            If True, .mp3 file is deleted after audio records generation.

        Returns
        -------
        list
            List of generated audio records (as AudioData instances).

        Raises
        ------
        ValueError
            If:
                - input file is not an .mp3 file
                - s_per_step is not positive
        """
        # input file type check
        if not mp3_file_path.endswith(".mp3"):
            raise ValueError("Input file is not an .mp3 file.")

        elif s_per_step <= 0:
            raise ValueError(
                f"'s_per_step' parameter must be positive (got {s_per_step})")

        # get audio duration in seconds
        duration_s = MP3(mp3_file_path).info.length
        steps = int(math.ceil(duration_s/s_per_step))
        self.update_init_progress(percent=48)

        # generates the .wav mono audio file
        wav_file_path = self._mp3_to_wav(mp3_file_path=mp3_file_path,
                                         mp3_to_delete=mp3_to_delete)

        # generates the audio records list from .wav file
        logging.info(f"Transcribing file {wav_file_path}...")
        audio_list = []
        r = speech_recognition.Recognizer()
        with speech_recognition.AudioFile(filename_or_fileobject=wav_file_path) as source:
            for step in range(steps):
                audio_list.append(r.record(source,
                                           duration=s_per_step if step != steps-1 else None))
                self.update_init_progress(percent=(80 + int((step+1)/steps*20)))

        os.remove(wav_file_path)

        return audio_list

    def _mp3_to_wav(self,
                    mp3_file_path: str,
                    mp3_to_delete: bool) -> str:
        """
        Converts an .mp3 file into a .wav mono file.

        Parameters
        ----------
        mp3_file_path : str
            .mp3 file full path
        mp3_to_delete : bool
            True if mp3 file has to be deleted after conversion.

        Returns
        -------
        wav_file_path
            Generated .wav file full path

        Raises
        ------
        ValueError
            If input file is not an .mp3 file.
        """
        # input file type check
        if not mp3_file_path.endswith(".mp3"):
            raise ValueError("Input file is not an .mp3 file.")

        # get wav file path
        base_file_path = mp3_file_path[:mp3_file_path.rfind(".mp3")]
        wav_file_path = "".join((base_file_path, ".wav"))

        sound = AudioSegment.from_mp3(file=mp3_file_path)

        # deletes mp3 file if got from mp4 file
        if mp3_to_delete:
            os.remove(mp3_file_path)

        sound.export(out_f=wav_file_path, format="wav")
        self.update_init_progress(percent=64)

        # converts the .wav file from stereo to mono
        samplerate, audiodata = wavfile.read(wav_file_path)
        audiodata = audiodata.astype(float)
        d = audiodata.sum(axis=1) / 2
        wavfile.write(wav_file_path, samplerate, numpy.array(d, dtype='int16'))

        self.update_init_progress(percent=80)

        return wav_file_path