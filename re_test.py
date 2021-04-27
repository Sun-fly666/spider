import re
string = '<a data-loc-id="3197" target="_blank"><img src="https://i0.hdslb.com/bfs/sycp/creative_img/202104/77daf3bd42352e14428efa21a966cdd3.jpg@880w_388h_1c_95q" alt="桐人向你发起组队邀请">'

print(string)
ex = r'<a data-loc-id="3197".*?><img src=(.*?)@.*?>'

result = re.findall(ex, string, re.S)

print(result)