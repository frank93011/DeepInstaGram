from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from .models import myUser, Group, GroupRelation
from django.contrib.auth.models import User
import pickle
import json
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
# Create your views here.
# {'1': 'Openness', '2': 'Conscientiousness','3': 'Extraversion','4': 'Agreeableness','5': 'Neuroticism'}
opt = {'1': 'behavior', '2': 'highscore','3': 'lowscore'}
op = {'1': 'O_introduction', '2': 'O_highscore','3': 'O_lowscore'}
con = {'1': 'C_introduction', '2': 'C_highscore','3': 'C_lowscore'}
ex = {'1': 'E_introduction', '2': 'E_highscore','3': 'E_lowscore'}
ag = {'1': 'A_introduction', '2': 'A_highscore','3': 'A_lowscore'}
ne = {'1': 'N_introduction', '2': 'N_highscore','3': 'N_lowscore'}

def homepage(request):
	return render(request, 'homepage.html')

def register(request):
	
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	if (username != '' and password != ''):
		User.objects.create_user(username=username, password=password)
		return HttpResponseRedirect('/intro?page=register')
	return HttpResponseRedirect('/intro?page=1')

def intro(request):
	p = request.GET['page']
	data = {'gg': p+".html"}
	if p == '3':
		if request.user.is_authenticated == True: 
			return HttpResponseRedirect('/realized')
			#return render(request, 'realized.html', data)
		#print('eee')
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')

		user = auth.authenticate(username=username, password=password)

		if user is not None and user.is_active:
			auth.login(request, user)
			#return HttpResponseRedirect('/realized')
			return render(request, 'realized.html', data)

	if p == 'register':
		# username = request.POST.get('username', '')
		# password = request.POST.get('password', '')
		# if (username != '' and password != ''):
		# 	User.objects.create_user(username=username, password=password)
		# 	return HttpResponseRedirect('/intro?page=register')
		# return HttpResponseRedirect('/intro?page=1')
		#print(data)
		# print(request.POST)
		if "register_submit" in request.POST:
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			if (username != '' and password != ''):
				User.objects.create_user(username=username, password=password)
				return HttpResponseRedirect('/intro?page=register')
			return HttpResponseRedirect('/intro?page=1')
		#print('inside')
		return render(request, 'register.html', data)
		#return HttpResponseRedirect('/register')
	if p == 'import':
		if request.user.is_superuser == True:

			pic_file = open('user_data_new', 'rb')
			user_data = pickle.load(pic_file)
			pic_file = open('user_personality', 'rb')
			user_personality = pickle.load(pic_file)
			pic_file = open('user_profile_pic', 'rb')
			user_profile = pickle.load(pic_file)
			pic_file = open('group_data', 'rb')
			user_group = pickle.load(pic_file)
			pic_file = open('group_predictionmac', 'rb')
			mac_group = pickle.load(pic_file)
			pic_file = open('data/individual_prediction_imagelab', 'rb')
			user_lab = pickle.load(pic_file)
			pic_file = open('data/individual_prediction_harley', 'rb')
			user_harley = pickle.load(pic_file)
			pic_file = open('data/individual_prediction_mac', 'rb')
			user_mac = pickle.load(pic_file)
			pic_file = open('data/group_prediction_harley', 'rb')
			group_harley = pickle.load(pic_file)
			pic_file = open('data/group_prediction_mac', 'rb')
			group_mac = pickle.load(pic_file)



			usr_list = [user_lab, user_harley, user_mac]
			group_list = [group_harley, group_mac]

			sheet = pd.read_excel("ig_info.xlsx")

			curr_num = len(sheet)
			email_list = list(sheet['電子郵件地址'])
			ig_list = list(sheet['IG帳號'])


			for j in group_list:
				
				groupName = j['group_name']

				total_user = j['total_user']
				
				big5_openness = j['group_personality']['openness']
				big5_conscientiousness = j['group_personality']['conscientiousness']
				big5_extraversion = j['group_personality']['extraversion']
				big5_agreeableness = j['group_personality']['agreeableness']
				big5_neuroticism = j['group_personality']['neuroticism']

				hobby_outdoor = j['group_hobby']['outdoor']
				hobby_water = j['group_hobby']['water']
				hobby_sport = j['group_hobby']['sport']
				hobby_music = j['group_hobby']['music']
				hobby_dance = j['group_hobby']['dance']
				hobby_photo = j['group_hobby']['photo']
				hobby_drama = j['group_hobby']['drama']
				hobby_game = j['group_hobby']['game']
				hobby_visual = j['group_hobby']['visual']

				style_hiking = j['group_style']['hiking']
				style_infant = j['group_style']['infants']
				style_studying = j['group_style']['reading books']
				style_celebrate = j['group_style']['celebrate']
				style_firework = j['group_style']['firework']
				style_nightclub = j['group_style']['night club']
				style_sports = j['group_style']['sport']
				style_depressed = j['group_style']['depress']
				style_lonely = j['group_style']['loneliness']
				style_selfie = j['group_style']['selfie']
				style_building = j['group_style']['building']
				style_delicious = j['group_style']['delicious']
				style_books = j['group_style']['books']

				official_hiking_percent = j['official_style_percent']['hiking']
				official_infant_percent = j['official_style_percent']['infants']
				official_studying_percent = j['official_style_percent']['reading books']
				official_celebrate_percent = j['official_style_percent']['celebrate']
				official_firework_percent = j['official_style_percent']['firework']
				official_nightclub_percent = j['official_style_percent']['night club']
				official_sports_percent = j['official_style_percent']['sport']
				official_depressed_percent = j['official_style_percent']['depress']
				official_lonely_percent = j['official_style_percent']['loneliness']
				official_selfie_percent = j['official_style_percent']['selfie']
				official_building_percent = j['official_style_percent']['building']
				official_delicious_percent = j['official_style_percent']['delicious']
				official_books_percent = j['official_style_percent']['books']

				liked_hiking = j['official_style_like']['hiking']
				liked_infant = j['official_style_like']['infants']
				liked_studying = j['official_style_like']['reading books']
				liked_celebrate = j['official_style_like']['celebrate']
				liked_firework = j['official_style_like']['firework']
				liked_nightclub = j['official_style_like']['night club']
				liked_sports = j['official_style_like']['sport']
				liked_depressed = j['official_style_like']['depress']
				liked_lonely = j['official_style_like']['loneliness']
				liked_selfie = j['official_style_like']['selfie']
				liked_building = j['official_style_like']['building']
				liked_delicious = j['official_style_like']['delicious']
				liked_books = j['official_style_like']['books']

				total_user = mac_group['total_user']



				Group.objects.create(
					groupName=groupName, 

					total_user = total_user,

					big5_openness = big5_openness,
					big5_conscientiousness = big5_conscientiousness,
					big5_extraversion = big5_extraversion,
					big5_agreeableness = big5_agreeableness,
					big5_neuroticism = big5_neuroticism,

					hobby_outdoor = hobby_outdoor,
					hobby_water = hobby_water,
					hobby_sport = hobby_sport,
					hobby_music = hobby_music,
					hobby_dance = hobby_dance,
					hobby_photo = hobby_photo,
					hobby_drama = hobby_drama,
					hobby_game = hobby_game,
					hobby_visual = hobby_visual,

					style_hiking = style_hiking,
					style_infant = style_infant,
					style_studying = style_studying,
					style_celebrate = style_celebrate,
					style_firework = style_firework,
					style_nightclub = style_nightclub,
					style_sports = style_sports,
					style_depressed = style_depressed,
					style_lonely = style_lonely,
					style_selfie = style_selfie,
					style_building = style_building,
					style_delicious = style_delicious,
					style_books = style_books,

					official_hiking_percent = official_hiking_percent,
					official_infant_percent = official_infant_percent,
					official_studying_percent = official_studying_percent,
					official_celebrate_percent = official_celebrate_percent,
					official_firework_percent = official_firework_percent,
					official_nightclub_percent = official_nightclub_percent,
					official_sports_percent = official_sports_percent,
					official_depressed_percent = official_depressed_percent,
					official_lonely_percent = official_lonely_percent,
					official_selfie_percent = official_selfie_percent,
					official_building_percent = official_building_percent,
					official_delicious_percent = official_delicious_percent,
					official_books_percent = official_books_percent,

					liked_hiking = liked_hiking,
					liked_infant = liked_infant,
					liked_studying = liked_studying,
					liked_celebrate = liked_celebrate,
					liked_firework = liked_firework,
					liked_nightclub = liked_nightclub,
					liked_sports = liked_sports,
					liked_depressed = liked_depressed,
					liked_lonely = liked_lonely,
					liked_selfie = liked_selfie,
					liked_building = liked_building,
					liked_delicious = liked_delicious,
					liked_books = liked_books,

				)


			# for i in user_personality['prediction_prob']['openness'].keys():
			# #for i in ['shizuku_jiang']:
			# 	#print(user_personality['prediction_prob']['openness'][i])
			# 	ig_account = i
			# 	# print(ig_account)
			# 	if i in ig_list:
			# 		usr_idx = ig_list.index(i)
			# 		userEmail = email_list[usr_idx]
			# 		# print(userEmail)
			# 	big5_openness = user_personality['prediction_prob']['openness'][i]
			# 	big5_conscientiousness = user_personality['prediction_prob']['conscientiousness'][i]
			# 	big5_extraversion = user_personality['prediction_prob']['extraversion'][i]
			# 	big5_agreeableness = user_personality['prediction_prob']['agreeableness'][i]
			# 	big5_neuroticism = user_personality['prediction_prob']['neuroticism'][i]

			# 	hobby_outdoor = 999
			# 	hobby_water = 999
			# 	hobby_sport = 999
			# 	hobby_music = 999
			# 	hobby_dance = 999
			# 	hobby_photo = 999
			# 	hobby_drama = 999
			# 	hobby_game = 999
			# 	hobby_visual = 999

			# 	style_hiking = user_data['user_style_percent'][i]['自然樂活']
			# 	style_infant = user_data['user_style_percent'][i]['生氣蓬勃']
			# 	style_studying = user_data['user_style_percent'][i]['勤勉向上']
			# 	style_celebrate = user_data['user_style_percent'][i]['慶典狂歡']
			# 	style_firework = user_data['user_style_percent'][i]['斑斕繽紛']
			# 	style_nightclub = user_data['user_style_percent'][i]['不夜喧囂']
			# 	style_sports = user_data['user_style_percent'][i]['運動']
			# 	style_depressed = user_data['user_style_percent'][i]['壓抑之心']
			# 	style_lonely = user_data['user_style_percent'][i]['無聲孤寂']
			# 	style_selfie = user_data['user_style_percent'][i]['自拍狂熱']
			# 	style_building = user_data['user_style_percent'][i]['建築之美']
			# 	style_delicious = user_data['user_style_percent'][i]['佳餚美饌']
			# 	style_books = user_data['user_style_percent'][i]['典雅書香']

			# 	profile = user_profile[ig_account]

			# 	myUser.objects.create(
			# 		igName=ig_account, 
			# 		userEmail=userEmail,
			# 		big5_openness = big5_openness,
			# 	    big5_conscientiousness = big5_conscientiousness,
			# 	    big5_extraversion = big5_extraversion,
			# 	    big5_agreeableness = big5_agreeableness,
			# 	    big5_neuroticism = big5_neuroticism,

			# 	    hobby_outdoor = hobby_outdoor,
			# 	    hobby_water = hobby_water,
			# 	    hobby_sport = hobby_sport,
			# 	    hobby_music = hobby_music,
			# 	    hobby_dance = hobby_dance,
			# 	    hobby_photo = hobby_photo,
			# 	    hobby_drama = hobby_drama,
			# 	    hobby_game = hobby_game,
			# 	    hobby_visual = hobby_visual,

			# 	    style_hiking = style_hiking,
			# 	    style_infant = style_infant,
			# 	    style_studying = style_studying,
			# 	    style_celebrate = style_celebrate,
			# 	    style_firework = style_firework,
			# 	    style_nightclub = style_nightclub,
			# 	    style_sports = style_sports,
			# 	    style_depressed = style_depressed,
			# 	    style_lonely = style_lonely,
			# 	    style_selfie = style_selfie,
			# 	    style_building = style_building,
			# 	    style_delicious = style_delicious,
			# 	    style_books = style_books,

			# 	    imgUrl = profile
			# 		)
			err_cnt = 0
			for j in usr_list:
			#=================================
				category = ['hiking', 'infants', 'reading books', 'celebrate', 'firework', 'night club', 'sport', 'depress', 'loneliness', 'selfie', 'building', 'delicious', 'books']
				for id, style in j['user_style_percent'].items():
				    for c in category:
				        if c not in style.keys():
				            j['user_style_percent'][id][c] = 0

				for id, style in j['user_style_like_percent'].items():
				    for c in category:
				        if c not in style.keys():
				            j['user_style_like_percent'][id][c] = 0
            #==================================
				for i in j['user_personality_prob']['openness'].keys():
					try:
						ig_account = i
						# print(ig_account)
						
						userEmail = ''
						total_post = j['user_analysis_post'][i]
							# print(userEmail)
						big5_openness = j['user_personality_prob']['openness'][i]
						big5_conscientiousness = j['user_personality_prob']['conscientiousness'][i]
						big5_extraversion = j['user_personality_prob']['extraversion'][i]
						big5_agreeableness = j['user_personality_prob']['agreeableness'][i]
						big5_neuroticism = j['user_personality_prob']['neuroticism'][i]

						#print(j['user_style_percent'][i])

						style_hiking = j['user_style_percent'][i]['hiking']
						style_infant = j['user_style_percent'][i]['infants']
						style_studying = j['user_style_percent'][i]['reading books']
						style_celebrate = j['user_style_percent'][i]['celebrate']
						style_firework = j['user_style_percent'][i]['firework']
						style_nightclub = j['user_style_percent'][i]['night club']
						style_sports = j['user_style_percent'][i]['sport']
						style_depressed = j['user_style_percent'][i]['depress']
						style_lonely = j['user_style_percent'][i]['loneliness']
						style_selfie = j['user_style_percent'][i]['selfie']
						style_building = j['user_style_percent'][i]['building']
						style_delicious = j['user_style_percent'][i]['delicious']
						style_books = j['user_style_percent'][i]['books']

						style_hiking_like = j['user_style_like_percent'][i]['hiking']
						style_infant_like = j['user_style_like_percent'][i]['infants']
						style_studying_like = j['user_style_like_percent'][i]['reading books']
						style_celebrate_like = j['user_style_like_percent'][i]['celebrate']
						style_firework_like = j['user_style_like_percent'][i]['firework']
						style_nightclub_like = j['user_style_like_percent'][i]['night club']
						style_sports_like = j['user_style_like_percent'][i]['sport']
						style_depressed_like = j['user_style_like_percent'][i]['depress']
						style_lonely_like = j['user_style_like_percent'][i]['loneliness']
						style_selfie_like = j['user_style_like_percent'][i]['selfie']
						style_building_like = j['user_style_like_percent'][i]['building']
						style_delicious_like = j['user_style_like_percent'][i]['delicious']
						style_books_like = j['user_style_like_percent'][i]['books']	


						#print(j['user_total_like'])

						hiking_like_percent = j['user_total_like'][i]
						infant_like_percent = j['user_total_like'][i]
						studying_like_percent = j['user_total_like'][i]
						celebrate_like_percent = j['user_total_like'][i]
						firework_like_percent = j['user_total_like'][i]
						nightclub_like_percent = j['user_total_like'][i]
						sports_like_percent = j['user_total_like'][i]
						depressed_like_percent = j['user_total_like'][i]
						lonely_like_percent = j['user_total_like'][i]
						selfie_like_percent = j['user_total_like'][i]
						building_like_percent = j['user_total_like'][i]
						delicious_like_percent = j['user_total_like'][i]
						books_like_percent = j['user_total_like'][i]

						#print(j['user_profile_pic'])
						profile = j['user_profile_pic'][i]

					
					#print(profile)
					#print('hehehehe')
					#print('=======',ig_account, j['group_name'], total_post, big5_openness, j['user_profile_pic']['a0937358083'])
					
						myUser.objects.create(
							igName=ig_account, 
							userEmail=userEmail,
							total_post = total_post,
							big5_openness = big5_openness,
						    big5_conscientiousness = big5_conscientiousness,
						    big5_extraversion = big5_extraversion,
						    big5_agreeableness = big5_agreeableness,
						    big5_neuroticism = big5_neuroticism,

						    style_hiking = style_hiking,
						    style_infant = style_infant,
						    style_studying = style_studying,
						    style_celebrate = style_celebrate,
						    style_firework = style_firework,
						    style_nightclub = style_nightclub,
						    style_sports = style_sports,
						    style_depressed = style_depressed,
						    style_lonely = style_lonely,
						    style_selfie = style_selfie,
						    style_building = style_building,
						    style_delicious = style_delicious,
						    style_books = style_books,

							style_hiking_like = style_hiking_like,
							style_infant_like = style_infant_like,
							style_studying_like = style_studying_like,
							style_celebrate_like = style_celebrate_like,
							style_firework_like = style_firework_like,
							style_nightclub_like = style_nightclub_like,
							style_sports_like = style_sports_like,
							style_depressed_like = style_depressed_like,
							style_lonely_like = style_lonely_like,
							style_selfie_like = style_selfie_like,
							style_building_like = style_building_like,
							style_delicious_like = style_delicious_like,
							style_books_like = style_books_like,

							hiking_like_percent = hiking_like_percent,
							infant_like_percent = infant_like_percent,
							studying_like_percent = studying_like_percent,
							celebrate_like_percent = celebrate_like_percent,
							firework_like_percent = firework_like_percent,
							nightclub_like_percent = nightclub_like_percent,
							sports_like_percent = sports_like_percent,
							depressed_like_percent = depressed_like_percent,
							lonely_like_percent = lonely_like_percent,
							selfie_like_percent = selfie_like_percent,
							building_like_percent = building_like_percent,
							delicious_like_percent = delicious_like_percent,
							books_like_percent = books_like_percent,

						    imgUrl = profile
						)
					except:
						err_cnt +=1
						print(ig_account)
			print(err_cnt)





			return HttpResponseRedirect('/intro?page=1')

	return render(request, 'intro.html', data)
def Openness(request):
	s = request.GET['sub']
	data = {'option': op[s]+".html"}
	return render(request, 'Openness.html', data)
	
def Conscientiousness(request):
	s = request.GET['sub']
	data = {'option': con[s]+".html"}
	return render(request, 'Conscientiousness.html', data)

def Extraversion(request):
	s = request.GET['sub']
	data = {'option': ex[s]+".html"}
	return render(request, 'Extraversion.html', data)
def Agreeableness(request):
	s = request.GET['sub']
	data = {'option': ag[s]+".html"}
	return render(request, 'Agreeableness.html', data)
def Neuroticism(request):
	s = request.GET['sub']
	data = {'option': ne[s]+".html"}
	return render(request, 'Neuroticism.html', data)
def test(request):
	data = {'gg': "intro.html"}
	return render(request, 'test.html', data)
def realized(request):
	df = pd.read_excel("insta_info.xlsx")
	uid = myUser.objects.get(igName="linweiiihsuan")
	group = Group.objects.get(groupName="mac")
	o, c, e, a, n = cal_score(df.loc[df['IG帳號'] == uid.igName])
	data = {'gg': "intro.html", "uid": uid, "o": o, "c":c, "e":e, "a":a, "n":n, 'group': group}
	return render(request, 'realized.html', data)
	#return render(request, 'realized.html', data)
	if request.user.is_authenticated == True: 
		return HttpResponseRedirect('/realized')
		#return render(request, 'realized.html', data)

	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = auth.authenticate(username=username, password=password)

	if user is not None and user.is_active:
		auth.login(request, user)
		#return HttpResponseRedirect('/realized')
		return render(request, 'realized.html', data)
	else:
		# return render_to_response('3.html')
		return HttpResponseRedirect('/intro?page=3')
def cal_score(row):
	elem = row.iloc[0]
	openness = int(elem[36]) + int(elem[11]) + int(elem[20]) + int(elem[26]) - int(elem[6]) - int(elem[16]) - int(elem[31]) - 3
	conscientiousness = int(elem[38]) + int(elem[8]) + int(elem[13]) + int(elem[18]) + int(elem[28]) - int(elem[23]) - int(elem[33]) - 9
	extraversion = int(elem[15]) + int(elem[5]) + int(elem[10]) + int(elem[35]) + int(elem[30]) - int(elem[21]) - int(elem[25]) - 9
	agreeableness = int(elem[37]) + int(elem[32]) - int(elem[7]) - int(elem[12]) - int(elem[17]) - int(elem[22]) - int(elem[27]) + 9 
	neuroticism = int(elem[14]) + int(elem[19]) + int(elem[29]) - int(elem[4]) - int(elem[9]) - int(elem[24]) - int(elem[34]) + 3
	return openness/14, conscientiousness/14, extraversion/14, agreeableness/14, neuroticism/14
def logout(request):
    auth.logout(request)
    #return HttpResponseRedirect('/intro/')
    return HttpResponseRedirect('/intro?page=1')

