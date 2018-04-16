# -*- coding:utf-8 -*-
import urllib

from util.con_MySQL import Dba

ora = Dba()
CaiJia_Sql = """
            INSERT INTO HOME_BUS_STOP(village,village_name,name,type,typecode,address,distance,location,tel) values('%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s')
            """
# data = '{"status":"1","count":"40","info":"OK","infocode":"10000","suggestion":{"keywords":[],"cities":[]},"pois":[{"id":"B00156EQ50","name":"中国建设银行24小时自助银行(上海华漕支行)","type":"金融保险服务;自动提款机;中国建设银行ATM","typecode":"160303","biz_type":[],"address":"保乐路与金丰路交叉口西50米","location":"121.284992,31.202070","tel":[],"distance":"814","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B00156EQ5C","name":"中国建设银行(上海华漕支行)","type":"金融保险服务;银行;中国建设银行","typecode":"160106","biz_type":[],"address":"金丰路492号(保乐路)","location":"121.284999,31.202154","tel":"021-62219902;021-62219903","distance":"818","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B00155FCUP","name":"中国农业银行24小时自助银行(华漕支行)","type":"金融保险服务;自动提款机;中国农业银行ATM","typecode":"160304","biz_type":[],"address":"北翟路5201号","location":"121.297872,31.204918","tel":[],"distance":"875","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B00155FCUO","name":"中国农业银行(华漕支行)","type":"金融保险服务;银行;中国农业银行","typecode":"160107","biz_type":[],"address":"北翟路5201号(近诸翟广场)","location":"121.297768,31.205025","tel":"021-62211161","distance":"879","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B00155FGE7","name":"中国邮政储蓄银行(诸翟邮局营业部)","type":"金融保险服务;银行;中国邮政储蓄银行","typecode":"160139","biz_type":[],"address":"华漕镇纪翟路200号","location":"121.294305,31.207384","tel":"021-62213749;95580","distance":"999","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B0FFF03NMC","name":"中国邮政储蓄银行24小时自助银行(诸翟支行)","type":"金融保险服务;自动提款机;中国邮政储蓄银行ATM","typecode":"160336","biz_type":[],"address":"纪翟路200号","location":"121.294299,31.207419","tel":[],"distance":"1003","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B00155QLS4","name":"中国工商银行24小时自助银行(华漕支行)","type":"金融保险服务;自动提款机;中国工商银行ATM","typecode":"160302","biz_type":[],"address":"保乐路128号","location":"121.290507,31.207610","tel":[],"distance":"1026","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B00155QLS2","name":"中国工商银行(华漕支行)","type":"金融保险服务;银行;中国工商银行","typecode":"160105","biz_type":[],"address":"保乐路128号(近诸新路)","location":"121.290507,31.207610","tel":"021-24283736","distance":"1026","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B0FFI09MGU","name":"上海浦东发展银行(绿地·旭辉E天地支行)","type":"金融保险服务;银行;上海浦东发展银行","typecode":"160115","biz_type":[],"address":"华漕镇纪翟路256号绿地·旭辉E天地F1","location":"121.291509,31.207949","tel":"95528","distance":"1051","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B0FFH5GH7E","name":"交通银行ATM","type":"金融保险服务;自动提款机;交通银行ATM","typecode":"160305","biz_type":[],"address":"保乐路大润发1层","location":"121.293088,31.210301","tel":[],"distance":"1310","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B0FFHJEUTH","name":"中国建设银行(国家会展中心支行)","type":"金融保险服务;银行;中国建设银行","typecode":"160106","biz_type":[],"address":"盈港东路158号国家会展中心","location":"121.300617,31.188810","tel":"021-69280250","distance":"1331","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B0FFGDZJ71","name":"上海农商银行24小时自助银行(诸翟支行)","type":"金融保险服务;自动提款机;上海农商银行ATM","typecode":"160347","biz_type":[],"address":"繁兴路333号","location":"121.293533,31.210708","tel":[],"distance":"1357","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B00156ELPD","name":"上海农商银行(诸翟支行)","type":"金融保险服务;银行;上海农商银行","typecode":"160150","biz_type":[],"address":"繁兴路333号(近保乐路)","location":"121.293533,31.210708","tel":"021-62213011;4006696198","distance":"1357","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B0FFIMT5CJ","name":"恒丰银行ATM","type":"金融保险服务;自动提款机;自动提款机","typecode":"160300","biz_type":[],"address":"申滨路473号新华联购物中心F1","location":"121.309303,31.200931","tel":[],"distance":"1623","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B0FFHDS0U4","name":"中国银行(虹桥会展中心支行)","type":"金融保险服务;银行;中国银行","typecode":"160104","biz_type":[],"address":"涞港路77号国家会展中心C栋101室中国银行","location":"121.306404,31.188401","tel":"021-69721315","distance":"1741","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B0FFI9BMEQ","name":"九江银行","type":"金融保险服务;银行;银行","typecode":"160100","biz_type":[],"address":"泰虹路268弄6号","location":"121.310703,31.201150","tel":"95316","distance":"1758","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B0FFG4TQ7R","name":"中国工商银行24小时自助银行","type":"金融保险服务;自动提款机;中国工商银行ATM","typecode":"160302","biz_type":[],"address":"宁虹路1175弄23号","location":"121.308550,31.207640","tel":[],"distance":"1834","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B0FFFEHRNQ","name":"中国工商银行(新虹支行)","type":"金融保险服务;银行;中国工商银行","typecode":"160105","biz_type":[],"address":"宁虹路1175弄23、25、27号1层","location":"121.308538,31.207686","tel":"021-54380983","distance":"1836","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B001579IGD","name":"中国银行ATM","type":"金融保险服务;自动提款机;自动提款机","typecode":"160300","biz_type":[],"address":"宁虹路1199号","location":"121.308488,31.208150","tel":[],"distance":"1861","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]},{"id":"B00156NQQP","name":"中国银行(宁虹路支行)","type":"金融保险服务;银行;中国银行","typecode":"160104","biz_type":[],"address":"宁虹路1199号1层A","location":"121.308505,31.208145","tel":"021-54312561","distance":"1862","biz_ext":[],"importance":[],"shopid":[],"shopinfo":"2","poiweight":[]}]}'
# village = "elxy"
# village_name = "二联馨苑"
# location = '&location=121.292485,31.198543'  # 二联馨苑

village = "zhjy"
village_name = "中虹家园"
location = '&location=121.672462,31.28271'  # 中虹家园

# village = "dxy"
# village_name = "丁香园"
# location = '&location=121.415404,31.14585'  # 丁香园


keywords = '&keywords=公交站'
type = '&types='
other = '&radius=2000&offset=20&page=1&extensions=base'

amap_url = 'http://restapi.amap.com/v3/place/around?key=eb38430327c843a503698c6eb015ec48' + location + keywords + type + other
page = urllib.urlopen(amap_url)
data = page.read()

for data in data.split('{"')[3:]:
    ll = data.split(',"')
    distance = ""
    name = ""
    type = ""
    typecode = ""
    address = ""
    location = ""
    tel = ""
    for l in ll:
        if l.split(':"')[0].strip("\"") == "name":
            name = l.split(':"')[1].strip("\"")
        if l.split(':"')[0].strip("\"") == "address":
            address = l.split(':"')[1].strip("\"")
        if l.split(':"')[0].strip("\"") == "tel":
            tel = l.split(':"')[1].strip("[]")
        if l.split(':"')[0].strip("\"") == "location":
            location = l.split(':"')[1].strip("\"")
        if l.split(':"')[0].strip("\"") == "type":
            type = l.split(':"')[1].strip("\"")
        if l.split(':"')[0].strip("\"") == "typecode":
            typecode = l.split(':"')[1].strip("\"")
        if l.split(':"')[0].strip("\"") == "distance":
            distance = l.split(':"')[1].strip("\"")
        # rank_date=time.strptime(str(rank_date),"%Y-%m-%d")
    sql = CaiJia_Sql % (village,
                        village_name,
                        name,
                        type,
                        typecode,
                        address,
                        distance,
                        location,
                        tel.strip("\"")
                        )
    try:
        ora.cux_sql_base(ora.connect(), sql)
        # cursor.execute(sql, (name, low_price, high_price, ave_price, unit))
        # conn.commit()
    except Exception as e:
        print(e)
