#-*- coding: utf-8 -*-
#
#
#
#
# Author: 
# Copyright (c) SomeCorp.

import sys

def gen_relevant_data(pocket_ids, json_from_pocket_api, 
                      fields=['given_title',     'given_url',    'resolved_title',   'resolved_url', 
                              'excerpt',         'word_count',   'time_to_read',     'top_image_url']):
    
    json = json_from_pocket_api['list']
    json_keys = json.keys()
    
    print(f'json_keys: {json_keys}', file=sys.stderr)
    print(f'pocket_ids: {pocket_ids}', file=sys.stderr)
    print(f'json_from_pocket_api: {json_from_pocket_api}', file=sys.stderr)
    
    for pocket_id in pocket_ids:
        if pocket_id in json_keys:
            item = json[pocket_id]
            yield {key: item[key] for key in [f for f in fields if f in item.keys()] } if fields else item
        else:
            yield {'not_found': pocket_id}
    


