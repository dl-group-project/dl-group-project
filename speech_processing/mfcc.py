'''
Given a .wav file or a list of .wav files of a particular phoneme recorded at a sampling rate of 16000 Hz,
the code breaks the wav file into frames of 10ms duration and labels the utterance frames with their respective
phoneme label. The code was provided by the TAs of 11785 and other sub-sections of signal processing leverage
open source code and libraries as cited and referenced below.
'''

import librosa
import matplotlib.pyplot as plt
import numpy as np
import math
import webrtcvad
import glob
from python_speech_features import mfcc
from python_speech_features import logfbank

filenames = glob.glob("Professor_Sounds/EH.wav")


# Citation: https://github.com/gdebayan/Diarization_BIC/tree/master/DIARIZATION
def vadfn(x, nsh, fs, feat):
    # Making a webrtcvad Object. For more information , Visit: https://github.com/wiseman/py-webrtcvad
    # Setting Mode 3 of 'Aggresiveness'. Visit: https://github.com/wiseman/py-webrtcvad

    vad = webrtcvad.Vad()
    vad.set_mode(3)

    lenx = len(x)
    i = 0
    count = 0
    ind = 0
    Nsh = fs * nsh  # frame window shift in samples
    Nw = fs * 0.010  # frame window size in samples(has to be 10/20/30ms for webrtcvad)

    numfram1 = int(math.ceil(((lenx - Nw) / (Nsh))))  # number of frames with Size Nw and overlapp Nsh
    numfram = min(numfram1,
                  len(feat[1, :]))  # taking min(len(features),numfram) to avoid mismatch. Usually will be same.

    frame = np.zeros((int(Nw), numfram1))  # frame shape

    # dividing audio signal into overlapping frames, with parameters :(Nsh,Nw)

    while (i < lenx - Nw):
        j = 0
        while (j < Nw):
            frame[int(j), int(ind)] = x[int(count)]
            j = j + 1
            count = count + 1
        ind = ind + 1

        i = i + Nsh
        count = i

    feat_1 = feat[:, 0:numfram]
    vad_flag = np.zeros((numfram,))
    # checking each frame if Voiced or Unvoiced.Using webrtcvad library
    for k in range(0, numfram):
        fr = np.int16(frame[:, k] * 32768).tobytes()
        # webrtcvad requires input to be in Byte format, not in 'decimal', hence converting
        a = (vad.is_speech(fr, fs))
        vad_flag[k] = int(a)

    return vad_flag, feat_1, numfram


x_data, y_labels = list(), list()
phoneme_mapper = dict()
counter = 0
phoneme_mapper[counter] = "SIL"
filenames = sorted(filenames)
for filename in filenames:

    # INPUT SIGNAL
    x, fs = librosa.load(filename, sr=16000)
    x = x.reshape(x.shape[0], 1)  # for one-channel signal

    sig, rate = librosa.load(filename)

    mfcc_feat = mfcc(sig, rate, nfilt=40, nfft=2048, lowfreq=100, highfreq=7500,
                     winlen=0.01, winstep=0.01)  # number of frames * number of cep
    fbank_feat = logfbank(sig, rate, nfilt=40, nfft=2048, lowfreq=100, highfreq=7500, winlen=0.01, winstep=0.01)

    feat = fbank_feat.T

    vad_flag, feat_1, numfram = vadfn(x, 0.01, fs, feat)

    phoneme_type = filename.split("/")[1].split(".")[0].upper()

    counter += 1
    phoneme_mapper[counter] = phoneme_type
    temp = list()
    for flag in vad_flag:
        if flag == 1:
            temp.append(counter)
        else:
            temp.append(0)

    x_data = fbank_feat
    y_labels = np.asarray(temp)

    np.save("Word_Sounds/" + phoneme_type + "_word_features.npy", x_data)
    train_split_length = int(0.7 * (numfram)) + 1
    dev_split_length = int(0.15 * (numfram)) + 1

    train_data = x_data[:train_split_length, :]
    np.save("Preprocessed_Data/" + phoneme_type + "_train_features.npy", train_data)
    dev_data = x_data[train_split_length:train_split_length + dev_split_length, :]
    np.save("Preprocessed_Data/" + phoneme_type + "_dev_features.npy", dev_data)
    test_data = x_data[train_split_length + dev_split_length:, :]
    np.save("Preprocessed_Data/" + phoneme_type + "_test_features.npy", test_data)

    train_labels = y_labels[:train_split_length]
    np.save("Preprocessed_Data/" + phoneme_type + "_train_labels.npy", train_labels)
    dev_labels = y_labels[train_split_length:train_split_length + dev_split_length]
    np.save("Preprocessed_Data/" + phoneme_type + "_dev_labels.npy", dev_labels)
    test_labels = y_labels[train_split_length + dev_split_length:]
    np.save("Preprocessed_Data/" + phoneme_type + "_test_labels.npy", test_labels)

    assert (train_data.shape[0] + dev_data.shape[0] + test_data.shape[0]) == numfram
    assert (train_labels.shape[0] + dev_labels.shape[0] + test_labels.shape[0]) == numfram

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.title('Log Mel-filterbank energy features of MFCC for Phoneme ' + str(phoneme_type))
    plt.ylabel('Log power magnitude')
    plt.xlabel('Number of frames')
    plt.imshow(fbank_feat.T)

    plt.subplot(2, 1, 2)
    plt.title('Frame level Voice Activity Detection for Phoneme ' + str(phoneme_type))
    plt.ylabel('Activity Detection')
    plt.xlabel('Number of frames')
    plt.plot(vad_flag)
    plt.savefig('Phoneme_Graphs/' + str(phoneme_type) + ".png")
    plt.show()
