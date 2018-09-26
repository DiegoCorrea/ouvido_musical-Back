# -*- coding: utf-8 -*-
import gc

from apps.tecnics.content_based_metadata.main_by_model_length import with_pre_load_data_set_and_song_variation
from apps.tecnics.content_based_metadata.main_by_song_metadata import with_pre_load_data_set_and_user_variation

with_pre_load_data_set_and_song_variation()
gc.collect()
with_pre_load_data_set_and_user_variation()
