
def split_1(_seat):

    seat_list = _seat.split('^')

    real_seat_list = []

    for i in seat_list :
        sl = i.split('@')
        real_seat_list.append(sl)

    for j, k in enumerate(real_seat_list):
        
        if real_seat_list[j][0] == '' :
            continue
        else :
            aa = real_seat_list[j][4] + ' ' + real_seat_list[j][2] + '원' + " " + real_seat_list[j][3] + '석'

        print(aa)


def split_2(_seat):

    seat_list = _seat.split('^')

    real_seat_list = []

    for i in seat_list:
        sl = i.split('@')
        real_seat_list.append(sl)

    for j, k in enumerate(real_seat_list):
        
        if real_seat_list[j][0] == '' :
            continue
        else :
            aa = real_seat_list[j][0] + ' ' + real_seat_list[j][1] + '/' + real_seat_list[j][2] + '석'

        print(aa)
