# dl-group-project

In this project, an end-to-end deep learning pipeline was built to discriminate between small vocabularies of confusable phonemes using human-guided AI. First, a dataset for the experiments was generated manually by the team wherein recordings of over 38 isolated phonemes were made in male and female voices. The raw speech data were further processed using a window length of 10 milliseconds and 40 log amplitude features sampled on a Mel scale. The ground truth labels for each frame were bootstrapped using the open-source Google Voice Activity detector. 

The core of the pipeline - the Deep Learning model - is an ensemble of specialized neural networks with architectures designed to be interpretable. Each of the sub-networks was trained to be a high-performance discriminator on specific tasks, such as differentiating between vowels and consonants, high and low vowels, voiced and unvoiced fricatives, and confusable phoneme pairs. The system takes as input a sequence of frames and returns the corresponding frame-level phoneme label - a probability score. This system can be used in isolation as a frame-level phoneme recognizer or can be plugged in as the frontend to a deeper backend system capable of performing specialized tasks like word detection by back-propagating the error all the way to the frontend.

The constraint of interpretability meant that the system had to be simple yet intuitive as opposed to deeper and more complex neural networks that are traditionally “black box” in nature.

