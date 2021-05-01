# PHONEME_MAPPER is a dictionary that maps the integer phoneme label assigned during voice activity detection to the actual phoneme sound string
PHONEME_MAPPER = {0: 'SIL', 1: 'AE', 2: 'AH', 3: 'AW', 4: 'AY', 5: 'B', 6: 'EH', 7: 'D', 8: 'DH', 9: 'EE', 10: 'FF', 11: 'G', 12: 'HH', 13: 'IH', 14: 'II', 15: 'J', 16: 'K', 17: 'LL', 18: 'MM', 19: 'NN', 20: 'OH', 21: 'OO', 22: 'OW', 23: 'OY', 24: 'P', 25: 'RR', 26: 'SH', 27: 'SS', 28: 'T', 29: 'TH', 30: 'UE', 31: 'UH', 32: 'VV', 33: 'WW', 34: 'YY', 35: 'ZZ'}

# Baker's categories
VOWELS_LIST = ['EE', 'IH', 'EH', 'AE', 'UH', 'ER', 'AH', 'AW', 'OO', 'UE']  # deliberately leaving out diphthongs
CONSONANTS_LIST = ['FF', 'HH', 'MM', 'NN', 'NG', 'RR', 'SS', 'SH', 'VV', 'WW', 'YY', 'ZZ']  # leaving out semivowels and stops

HIGH_VOWELS_LIST = ['EE', 'IH', 'UE', 'OO']
LOW_VOWELS_LIST = ['AE', 'AH', 'AW']

VOICED_FRICATIVES = ['DH', 'VV', 'ZZ']
UNVOICED_FRICATIVES = ['FF', 'SS', 'SH', 'TH']

SPECIALIZED_TASKS = {
    '1_vowel_vs_consonant': {
        0: VOWELS_LIST,
        1: CONSONANTS_LIST
    },
    '3_highvowel_vs_lowvowel': {
        0: HIGH_VOWELS_LIST,
        1: LOW_VOWELS_LIST
    },
    '4_voiced_vs_unvoiced_fricatives': {
        0: VOICED_FRICATIVES,
        1: UNVOICED_FRICATIVES
    },
    '5_ss_vs_zz': {
        0: ['SS'],
        1: ['ZZ']
    },
    '6_b_vs_p': {
        0: ['B'],
        1: ['P']
    },
    '7_dh_vs_th': {
        0: ['DH'],
        1: ['TH']
    },
    '8_ww_vs_yy': {
        0: ['WW'],
        1: ['YY']
    },
    '9_ee_vs_aw': {
        0: ['EE'],
        1: ['AW']
    },
    '10_ah_vs_aw': {
        0: ['AH'],
        1: ['AW']
    },
    '11_mm_vs_nn': {
        0: ['AH'],
        1: ['AW']
    },
}
