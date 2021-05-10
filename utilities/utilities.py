# PHONEME_MAPPER is a dictionary that maps the integer phoneme label assigned during voice activity detection to the actual phoneme sound string
PHONEME_MAPPER = {0: 'SIL', 1: 'AE', 2: 'AH', 3: 'AW', 4: 'AY', 5: 'B', 6: 'EH', 7: 'D', 8: 'DH', 9: 'EE', 10: 'FF', 11: 'G', 12: 'HH', 13: 'IH', 14: 'II', 15: 'J', 16: 'K', 17: 'LL', 18: 'MM', 19: 'NN', 20: 'OH', 21: 'OO', 22: 'OW', 23: 'OY', 24: 'P', 25: 'RR', 26: 'SH', 27: 'SS', 28: 'T', 29: 'TH', 30: 'UE', 31: 'UH', 32: 'VV', 33: 'WW', 34: 'YY', 35: 'ZZ', 36: 'CH', 37: 'ER', 38: 'NG'}

# Baker's categories
VOWELS_LIST = ['EE', 'IH', 'EH', 'AE', 'UH', 'ER', 'AH', 'AW', 'OO', 'UE']  # deliberately leaving out diphthongs
CONSONANTS_LIST = ['FF', 'HH', 'MM', 'NN', 'NG', 'RR', 'SS', 'SH', 'VV', 'WW', 'YY', 'ZZ']  # leaving out semivowels and stops
TASK1_NONE = [phoneme_tag for phoneme_index, phoneme_tag in PHONEME_MAPPER.items() if phoneme_tag not in VOWELS_LIST + CONSONANTS_LIST]

HIGH_VOWELS_LIST = ['EE', 'IH', 'UE', 'OO']
LOW_VOWELS_LIST = ['AE', 'AH', 'AW']
TASK3_NONE = [phoneme_tag for phoneme_index, phoneme_tag in PHONEME_MAPPER.items() if phoneme_tag not in HIGH_VOWELS_LIST + LOW_VOWELS_LIST]

VOICED_FRICATIVES = ['DH', 'VV', 'ZZ']
UNVOICED_FRICATIVES = ['FF', 'SS', 'SH', 'TH']
TASK4_NONE = [phoneme_tag for phoneme_index, phoneme_tag in PHONEME_MAPPER.items() if phoneme_tag not in VOICED_FRICATIVES + UNVOICED_FRICATIVES]

SPECIALIZED_TASKS = {
    '1_vowel_vs_consonant': {
        0: TASK1_NONE,
        1: VOWELS_LIST,
        2: CONSONANTS_LIST
    },
    '3_highvowel_vs_lowvowel': {
        0: TASK3_NONE,
        1: HIGH_VOWELS_LIST,
        2: LOW_VOWELS_LIST
    },
    '4_voiced_vs_unvoiced_fricatives': {
        0: TASK4_NONE,
        1: VOICED_FRICATIVES,
        2: UNVOICED_FRICATIVES
    },
    '5_ss_vs_zz': {
        0: [phoneme_tag for phoneme_index, phoneme_tag in PHONEME_MAPPER.items() if phoneme_tag not in ["SS", "ZZ"]],
        1: ['SS'],
        2: ['ZZ']
    },
    '6_b_vs_p': {
        0: [phoneme_tag for phoneme_index, phoneme_tag in PHONEME_MAPPER.items() if phoneme_tag not in ["B", "P"]],
        1: ['B'],
        2: ['P']
    },
    '7_dh_vs_th': {
        0: [phoneme_tag for phoneme_index, phoneme_tag in PHONEME_MAPPER.items() if phoneme_tag not in ["DH", "TH"]],
        1: ['DH'],
        2: ['TH']
    },
    '8_ww_vs_yy': {
        0: [phoneme_tag for phoneme_index, phoneme_tag in PHONEME_MAPPER.items() if phoneme_tag not in ["WW", "YY"]],
        1: ['WW'],
        2: ['YY']
    },
    '9_ee_vs_aw': {
        0: [phoneme_tag for phoneme_index, phoneme_tag in PHONEME_MAPPER.items() if phoneme_tag not in ["EE", "AW"]],
        1: ['EE'],
        2: ['AW']
    },
    '10_ah_vs_aw': {
        0: [phoneme_tag for phoneme_index, phoneme_tag in PHONEME_MAPPER.items() if phoneme_tag not in ["AH", "AW"]],
        1: ['AH'],
        2: ['AW']
    },
    '11_mm_vs_nn': {
        0: [phoneme_tag for phoneme_index, phoneme_tag in PHONEME_MAPPER.items() if phoneme_tag not in ["MM", "NN"]],
        1: ['MM'],
        2: ['NN']
    },
}
