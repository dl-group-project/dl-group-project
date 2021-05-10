# dl-group-project

In this project, an end-to-end deep learning pipeline was built to discriminate between small vocabularies of confusable phonemes using human-guided AI. First, a dataset for the experiments was generated manually by the team wherein recordings of over 38 isolated phonemes were made in male and female voices. The raw speech data were further processed using a window length of 10 milliseconds and 40 log amplitude features sampled on a Mel scale. The ground truth labels for each frame were bootstrapped using the open-source Google Voice Activity detector. 

The core of the pipeline - the Deep Learning model - is an ensemble of specialized neural networks with architectures designed to be interpretable. Each of the sub-networks was trained to be a high-performance discriminator on specific tasks, such as differentiating between vowels and consonants, high and low vowels, voiced and unvoiced fricatives, and confusable phoneme pairs. The system takes as input a sequence of frames and returns the corresponding frame-level phoneme label - a probability score. This system can be used in isolation as a frame-level phoneme recognizer or can be plugged in as the frontend to a deeper backend system capable of performing specialized tasks like word detection by back-propagating the error all the way to the frontend.

The constraint of interpretability meant that the system had to be simple yet intuitive as opposed to deeper and more complex neural networks that are traditionally “black box” in nature.

The directory structure is as follows:

1 sound_detectors_classifiers - This folder contains all the classifier models that we have experimented with.
- The Shallow Detectors notebook is used to distinguish each of the phonemes with silence.
- The Frame to Phoneme classifier notebook is used to classify each frame to their respective phonemes.
- The specialized shallow detector notebook contains the models to perform specific tasks. These tasks are present in the appendix section of our report.
- The complete network is the final deep network consisting of each of our detectors and classifiers.

2 preprocessed_data - This folder contains our preprocessed data in npy format as well as the utilities file.
- phoneme_train_features.npy - The training data features (melspectograms) for the respective phoneme.
- phoneme_dev_features.npy - The validation data features (melspectograms) for the respective phoneme.
- phoneme_test_features.npy - The testing data features (melspectograms) for the respective phoneme.

- phoneme_train_labels.npy - The frame level training data labels for the respective phoneme.
- phoneme_dev_labels.npy - The frame level validation data labels for the respective phoneme.
- phoneme_test_labels.npy - The frame level testing data labels for the respective phoneme.


3 graphs - This folder contains visualizations such as the phoneme melspectograms and voice activity detectors.

4 speech processing - This folder contains numerous signal processing code that we tried to perform our feature engineering.
The one that worked is called mfcc.py which has melspectogram code provided by the TAs as well as other open source code.

5 utilities - This folder contains the helper file called utilities.py - A Python file containing the utilities necessary for data engineering required during model building
and training. Currently contains a dictionary called PHONEME_MAPPER that maps the integer representation of each phoneme
present in each frame labels to it's respective phoneme string. (e.g 0 maps to 'SIL' or Silence and 1 maps to 'AE').
It also contains dictionaries to support categories for our various classificiation tasks.

6 phoneme_utterances - Contains the wav files for each isolated phoneme utterance that we used.

7 evaluation - This folder contains sub folders which has code to evaluate our detectors and classifiers as well as the respective updated reports.

8 reports - This folder contains our project reports

9 voice_detection - This folder contains some of our initial voice activity detection code which was not finally used.

10 autoencoders - This folder contains code for our autoencoder model which was not finally used.





