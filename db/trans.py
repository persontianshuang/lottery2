YEAR = '20'

def ss(data):
    def red_blue(num):
        red,blue = num.split('#')
        red = red.split(',')
        blue = blue.split(',')
        return red,blue

    def two_to_one(two):
        raw = two.split(',')
        want = []
        want.append([raw[0]+raw[1]])
        want.append([raw[0]+raw[1]])
        want.append([raw[2]+raw[3]])
        want.append([raw[4]+raw[5]])
        want.append([raw[6]+raw[7]])
        want.append([raw[8]+raw[9]])
        return want



    want = {}
    want['name'] = data['des']
    if data['des']=='双色球':
        want['issueno'] = YEAR + str(data['progress'])
        want['number'],want['refernumber'] = red_blue(data['lottery_num'])
        want['opendate'] = str(data['add_time'].year) +'-'+ data['check_time'].split(' ')[0]



    elif data['des']=='大乐透':
        want['issueno'] = str(data['progress'])
        want['number'],want['refernumber'] = red_blue(data['lottery_num'])
        want['opendate'] = str(data['add_time'].year) +'-'+ data['check_time'].split(' ')[0]

    elif data['des']=='福彩3d':
        want['name'] = '福彩3D'
        want['issueno'] = YEAR + str(data['progress'])
        want['number'] = data['lottery_num'].split(',')
        want['opendate'] = str(data['add_time'].year) +'-'+ data['check_time'].split(' ')[0]

    elif data['des']=='11选5江西':
        want['name'] = '赣11选5'
        want['issueno'] = YEAR + str(data['progress'])
        want['number'] = two_to_one(data['lottery_num'])
        want['opendate'] = str(data['add_time']).split('.')[0]

    elif data['des']=='鲁11选5':
        want['issueno'] = str(data['progress'])
        want['number'] = two_to_one(data['lottery_num'])
        want['opendate'] = str(data['add_time']).split('.')[0]

    elif data['des']=='粤11选5':
        want['issueno'] = YEAR + str(data['progress'])
        want['number'] = two_to_one(data['lottery_num'])
        want['opendate'] = str(data['add_time']).split('.')[0]
    return want


def trans(data):
    if type(data)==dict:
        return ss(data)
    if type(data)==list:
        return [ss(x) for x in data]



# print(trans([d,d]))

