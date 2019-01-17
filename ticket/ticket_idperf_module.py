# 공연 url - IdPerf 추출하기

import re

def get_idperf (URL) :
    try : 
        pIdPerf = re.findall("IdPerf=(.*)&", URL)[0]
    except IndexError:
        pIdPerf = re.findall("IdPerf=(.*)", URL)[0]
    
    return pIdPerf
