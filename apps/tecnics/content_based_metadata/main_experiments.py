# -*- coding: utf-8 -*-
import gc

from apps.tecnics.content_based_metadata.main_by_model_length import \
    pre_load_data_set_and_song_variation_all_combination
from apps.tecnics.content_based_metadata.main_by_song_metadata import with_pre_load_data_set_and_user_variation


def call():
    with_pre_load_data_set_and_user_variation()
    gc.collect()
    pre_load_data_set_and_song_variation_all_combination()
