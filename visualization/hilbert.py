#!/usr/bin/env python

import sys
#import scurve
import hilbert_api as hapi

class HilbertCurve(object):
    def __init__(self, filename, curve='hilbert'):
        self.filename   = filename
        self.file_bytes = open(self.filename, 'rb').read()
        self.hb_map     = hapi.Hilbert(len(self.file_bytes))
        # should eventually take several kinds of curves

    def _hb_index(self, (x,y)):
        return self.hb_map.encode((x,y))

    def _hb_point(self, p):
        return self.hb_map.decode(p)

    def get_range(self, (x,y), amount):
        hb_idx = self._hb_index((x,y))

        min_idx = max(0, hb_idx - amount)
        max_idx = min(len(self.file_bytes), hb_idx + amount + 1)
        result = []
        for i in range(min_idx, max_idx):
            result.append(self._hb_point(i))

        return result

    def get_bytes(self, (x,y), amount):
        ret_bytes = []
        for idx in self.get_range((x,y), amount):
            ret_bytes.append(self.file_bytes[self._hb_index(idx)])
        return ret_bytes

    def get_hilbert_block(self, (x,y), order):
        ''' return the complete hilbert sub-block of order `order`,
spanning coordinate set (x,y).
'''
        pass