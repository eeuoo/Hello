import urllib.parse as parse
import os.path as path

def getFilename(url) :
    p = parse.urlparse(url).path
    return path.basename(p)

def getHostname(url, withProtocol = False):
    p = parse.urlparse(url)
    if withProtocol:
        return "{}://{}".format(p.scheme, p.hostname)
    else:
        return p.hostname

def urljoin( url, p) :
    return parse.urljoin(url, p)

def q2j(s):
    ps = s.split('&')
    for p in ps:
        pp = p.split('=')
        print("'{}':'{}',".format(pp[0], pp[1]))


if __name__ == '__main__':
    str = "PCID=15470222941355869485375; MainPopup=OK; RecentViewGoods=; __utmz=186092716.1547024504.2.2.utmcsr=yes24.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ASP.NET_SessionId=om5o5c1yymagodfs5egygfkt; __utma=186092716.1855271271.1547022302.1547024504.1547107675.3; __utmc=186092716; __utmt=1; __utma=12748607.1722244286.1547022295.1547024502.1547107755.3; __utmc=12748607; __utmz=12748607.1547107755.3.2.utmcsr=ticket.yes24.com|utmccn=(referral)|utmcmd=referral|utmcct=/Pages/Perf/Detail/DetailSpecial.aspx; __utmt=1; __utmb=12748607.1.10.1547107755; ClientIPAddress=; ServerIPAddress=; MEM_NO=; MEM_ID=; MEM_NM=; FAMILY_PAY_NO=; MEM_GB=; NICK_NM=; BLOG_URL=; CART_NO=; MEM_AGE=; NEW_PID=; ServiceCookies=MTM3MDIxMTJgZGxndXN3bjUxMmDAzMf2wdZgMGAwMWBlZXVvb2BgMTM3MDIxMTJgMjRgQzNMYzg1cVZrQ0l5cy9UTm5VSjlxT3dGOHlZblRhOEVUT0p2Z3dOaXpDL05QU0pWVUtjczZHelhwL2RzblRDVXdzcFhiSlBvcjdiUGlJSit5WDZQSXc9PWAvYzNiWUhneHlxQTNsQ2pKZU9pVEQ5QmE5cThocjlpRlpucUt2RlJCVUJFbVVGN2tsQ0c2TThESml1eTJVWWtPalVxSFdTYmZBeWJCazVpSkhRUkVNSnhsK2RDZVpnL3pncTh1NDFya3NDV0labHhDSXdpeWc0R1JUWTJKMWQrTHdOZDlkMml3SDNsU3R4SERST09SUXA2MWUrZnlqcUtGdnl4UnNiem4ydms9YFY0V1ArL0FJL0xuVzVJSm9rWW9tY3c9PQ==; Mallinmall_CKMN=13702112; Mallinmall_CKMI=dlguswn512; Mallinmall_CKMNM=%c0%cc%c7%f6%c1%d6; Mallinmall_CKMAG=24; EntLoginInfo=ZGxndXN3bjUxMnwyMDE5LTAxLTEwIL/AyMQgNTowOToyOQ==; RecentViewInfo=ReloadTime=Thu%2c+10+Jan+2019+08%3a09%3a29+GMT&First=true; YesTicket=UserNO=219,73,255,90,69,117,142,189,202,180,5,235,31,241,201,237&UserID=153,238,209,56,101,231,77,216,150,189,130,224,103,11,91,130&UserName=27,63,241,180,51,104,182,14,132,246,242,196,122,137,66,49&UserNickName=45,76,196,233,90,83,14,125&Email=153,238,209,56,101,231,77,216,16,34,162,209,40,180,83,77,179,60,249,39,172,1,97,236&ManiaLevel=185,175,224,130,94,14,207,79&MemberStatus=245,54,43,158,39,91,228,116&UserIdentiNumber=33,40,251,46,189,206,203,41,64,132,42,121,166,0,175,45&StarLevel=245,54,43,158,39,91,228,116&PromotionCode=245,54,43,158,39,91,228,116&MemberGB=185,175,224,130,94,14,207,79&UserAge=11,202,76,221,177,78,95,208&ORD_PATH_GB=195,31,27,161,165,198,213,175&ZipCode=131,50,17,32,192,113,12,59&Address=240,119,82,81,197,89,184,133,219,46,29,119,46,8,194,97,81,199,29,66,58,84,47,101,39,116,105,57,162,29,185,255,100,184,226,45,37,45,45,57,31,8,125,19,73,116,18,60,155,46,107,20,164,210,177,65&Addr1=240,119,82,81,197,89,184,133,219,46,29,119,46,8,194,97,81,199,29,66,58,84,47,101,39,116,105,57,162,29,185,255,100,184,226,45,37,45,45,57,190,117,37,221,80,198,206,192&Addr2=42,140,37,210,72,164,94,200&Addr3=240,119,82,81,197,89,184,133,219,46,29,119,46,8,194,97,81,199,29,66,58,84,47,101,33,220,82,44,99,137,172,0,87,218,78,27,224,210,168,22,59,64,110,191,218,211,122,29,110,124,132,134,10,44,20,148&Addr4=170,197,115,59,136,128,140,123,89,45,142,72,163,27,203,34,255,242,24,4,22,102,36,214&Phone=180,27,76,187,35,13,48,127,118,202,46,96,236,214,49,73&Mobile=65,156,252,170,156,88,247,43,26,148,165,216,136,173,203,45&OrgID=13,101,187,16,10,24,135,131&Channel=13,101,187,16,10,24,135,131; __utmb=186092716.2.10.1547107675"
    q2j(str)