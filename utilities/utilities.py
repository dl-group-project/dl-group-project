# PHONEME_MAPPER is a dictionary that maps the integer phoneme label assigned during voice activity detection to the actual phoneme sound string
PHONEME_MAPPER = {0: 'SIL', 1: 'AE', 2: 'AH', 3: 'AW', 4: 'AY', 5: 'B', 6: 'EH', 7: 'D', 8: 'DH', 9: 'EE', 10: 'FF', 11: 'G', 12: 'HH', 13: 'IH', 14: 'II', 15: 'J', 16: 'K', 17: 'LL', 18: 'MM', 19: 'NN', 20: 'OH', 21: 'OO', 22: 'OW', 23: 'OY', 24: 'P', 25: 'RR', 26: 'SH', 27: 'SS', 28: 'T', 29: 'TH', 30: 'UE', 31: 'UH', 32: 'VV', 33: 'WW', 34: 'YY', 35: 'ZZ'}

# this is just an idea, not finalized
PHONEME_CHARACTERISTICS = {
    'AE': ['vowel', 'low_vowel', 'front_vowel'],
    'AH': ['vowel', 'low_vowel', 'back_vowel'],
    'AW': []
}

# TODO: fill these lists
VOWELS_LIST = ['AE', 'AH']
CONSONANTS_LIST = []

FRONT_VOWELS_LIST = []
BACK_VOWELS_LIST = ['AH']

HIGH_VOWELS_LIST = []
LOW_VOWELS_LIST = ['AH']

SPECIALIZED_TASKS = {
    'vowel_vs_consonant': {
        0: VOWELS_LIST,
        1: CONSONANTS_LIST
    },
    'frontvowel_vs_backvowel': {
        0: FRONT_VOWELS_LIST,
        1: CONSONANTS_LIST
    },
    'highvowel_vs_lowvowel': {
        0: HIGH_VOWELS_LIST,
        1: LOW_VOWELS_LIST
    }
}

