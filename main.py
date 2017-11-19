from datetime import datetime

from db.settings import mg_lottery
from extra import Shuangseqiu, Fucai3d, Daletou, Jiangxi11xuan5,Lu11xuan5,Yue11xuan5
from req import get_html

from db.mongoeng import Log

response = get_html()

datas = [
    Shuangseqiu(response).main(),
    Daletou(response).main(),
    Fucai3d(response).main(),
    Jiangxi11xuan5(response).main(),
    Lu11xuan5(response).main(),
    Yue11xuan5(response).main(),
         ]



def sk(x):
    search = Log.objects(uid=x['id'],progress=x['progress'])
    if search:
        pass
    else:
        ticket = Log()
        ticket.uid = x['id']
        ticket.des = x['des']
        # ticket.progress = 1
        ticket.progress = int(x['progress'].strip())
        ticket.check_time = x['check_time']
        ticket.lottery_num = x['lottery_num']
        ticket.save()

[sk(k) for k in datas]

# print(Log.objects(uid='001').order_by('-add_time').first().add_time)
