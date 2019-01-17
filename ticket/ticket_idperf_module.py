# 공연 url - IdPerf 추출하기

import re


def get_idperf (perfUrl) :

    pIdPerf = re.findall("IdPerf=(.*)", perfUrl)[0]

    return pIdPerf
