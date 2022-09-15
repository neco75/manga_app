from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests
import streamlit as st
import requests
from bs4 import BeautifulSoup


icon=('uaN5WRad_400x400.jpg')
st.set_page_config(
     page_title="漫画紹介文閲覧サイト",
     page_icon=icon,
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Report a bug': "https://twitter.com/ocen_UoA30C2",
     }
 )

html = "<h1  style=\"border-width: 0px 7px 0px 7px;  border-color: #99CCFF;  border-style: solid;  padding: 15px 10px;   margin:0px 0px 10px 0px;  background: #F0F0F0;\">漫画紹介文閲覧サイト</h1>"
st.components.v1.html("<center>" + html + "</center>")


param=st.text_input('漫画のタイトル')
btn=st.button('検索')

if btn:
	###マンガペディアで検索後一番上のリンクのURLを取得###

	response = requests.get(f'https://mangapedia.com/tg/{param}')
	soup = BeautifulSoup(response.text, "html.parser")
	elems = soup.find_all('a')
	titleURL='https://mangapedia.com/'+elems[4].attrs['href']






	###画像を取得###
	URL2=requests.get(titleURL)
	soup2 = BeautifulSoup(URL2.text, "html.parser")

	elems2 = soup2.find_all("div",class_="image")
	title = soup2.find("h1")
	lead=soup2.find_all("p",class_='lead')
	cont=soup2.find_all("section")



	elems2=str(elems2)
	s = elems2
	target = 'src='
	idx = s.find(target)
	r = s[idx+5:]  # スライスで半角空白文字のインデックス＋1以降を抽出
	target = 'width'
	idx = r.find(target)
	r = r[:idx-2]  # スライスで半角空白文字よりも前を抽出

	if 'http' in r:
		html="単行本表紙"
		st.components.v1.html("<center>" + html + "</center>")
		st.image(r,caption=title.contents[0],use_column_width=True)

	else:
		st.image('http://design-ec.com/d/e_others_50/l_e_others_500.jpg', caption=title.contents[0],width=500)



	###タイトルを持ってくる###
	#title = soup2.find("h1")
	st.subheader(title.contents[0])



	###紹介文持ってくる###
	#lead=soup2.find_all("p",class_='lead')
	st.write(lead[0].contents[0])



	###あらすじとってくる###
	#cont=soup2.find_all("section")
	st.write(cont[1].get_text().strip())


	###引用元表示###
	html="出典 : <a href=\"https://mangapedia.com/\"><img src=\"https://c.mangapedia.com/img/presskit/logo_200_40_clear.png\" alt=\"マンガペディア - マンガ・アニメの総合百科事典。\" width=\"200\" height=\"40\" border=\"0\"></a>"
	st.components.v1.html("<center>" + html + "</center>")