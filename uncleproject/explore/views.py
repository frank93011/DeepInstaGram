from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from .models import User, Group, GroupRelation
import pickle
import json
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
			#print(user_personality)
			#print(user_personality['prediction_prob']['openness'])
			# data = json.dumps(data,ensure_ascii=False, sort_keys = False, indent = 4, separators=(',', ': '))
			for i in user_personality['prediction_prob']['openness'].keys():
			#for i in ['shizuku_jiang']:
				#print(user_personality['prediction_prob']['openness'][i])
				ig_account = i
				#print(ig_account)
				big5_openness = user_personality['prediction_prob']['openness'][i]
				big5_conscientiousness = user_personality['prediction_prob']['conscientiousness'][i]
				big5_extraversion = user_personality['prediction_prob']['extraversion'][i]
				big5_agreeableness = user_personality['prediction_prob']['agreeableness'][i]
				big5_neuroticism = user_personality['prediction_prob']['neuroticism'][i]

				hobby_outdoor = 999
				hobby_water = 999
				hobby_sport = 999
				hobby_music = 999
				hobby_dance = 999
				hobby_photo = 999
				hobby_drama = 999
				hobby_game = 999
				hobby_visual = 999

				style_hiking = user_data['user_style_percent'][i]['自然樂活']
				style_infant = user_data['user_style_percent'][i]['生氣蓬勃']
				style_studying = user_data['user_style_percent'][i]['勤勉向上']
				style_celebrate = user_data['user_style_percent'][i]['慶典狂歡']
				style_firework = user_data['user_style_percent'][i]['斑斕繽紛']
				style_nightclub = user_data['user_style_percent'][i]['不夜喧囂']
				style_sports = user_data['user_style_percent'][i]['運動']
				style_depressed = user_data['user_style_percent'][i]['壓抑之心']
				style_lonely = user_data['user_style_percent'][i]['無聲孤寂']
				style_selfie = user_data['user_style_percent'][i]['自拍狂熱']
				style_building = user_data['user_style_percent'][i]['建築之美']
				style_delicious = user_data['user_style_percent'][i]['佳餚美饌']
				style_books = user_data['user_style_percent'][i]['典雅書香']

				profile = []
				profile.append(user_profile[ig_account])

				User.objects.create(igName=ig_account, 
					userEmail='hehe@email.com',
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

				    imgUrl = profile
					)

			return HttpResponseRedirect('/intro?page=1')
		# else:
		# 	# return render_to_response('3.html')
		# 	return HttpResponseRedirect('/intro?page=3')
	'''if p not in ['1', '2','3','4']:
		data = {'gg': "1.html"}
	elif p=='2':

		s = request.GET['sub']
		o = request.GET['opt']
		if s == '1':
			if o == '1':
				behavior = '這是openess的behavior'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'behavior': behavior}
			elif o == '2':
				highscore = '這是openess的highscore'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'highscore': highscore}
			elif o == '3':
				lowscore = '這是openess的lowscore'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'lowscore': lowscore}


		elif s == '2':
			if o == '1':
				behavior = '這是Conscientiousness的behavior'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'behavior': behavior}
			elif o == '2':
				highscore = '這是Conscientiousness的highscore'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'highscore': highscore}
			elif o == '3':
				lowscore = '這是Conscientiousness的lowscore'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'lowscore': lowscore}

		elif s == '3':
			if o == '1':
				behavior = '這是Extraversion的behavior'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'behavior': behavior}
			elif o == '2':
				highscore = '這是Extraversion的highscore'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'highscore': highscore}
			elif o == '3':
				lowscore = '這是Extraversion的lowscore'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'lowscore': lowscore}

		elif s == '4':
			if o == '1':
				behavior = '這是Agreeableness的behavior'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'behavior': behavior}
			elif o == '2':
				highscore = '這是Agreeableness的highscore'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'highscore': highscore}
			elif o == '3':
				lowscore = '這是Agreeableness的lowscore'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'lowscore': lowscore}

		elif s == '5':
			if o == '1':
				behavior = '這是Neuroticism的behavior'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'behavior': behavior}
			elif o == '2':
				highscore = '這是Neuroticism的highscore'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'highscore': highscore}
			elif o == '3':
				lowscore = '這是Neuroticism的lowscore'
				data = {'gg': "2.html",'personality':sub[s]+".html", 'option':opt[o]+".html", 'lowscore': lowscore}

		else:
			data = {'gg': "2.html"}

	else:
		data = {'gg': p+".html"}'''

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
	data = {'gg': "intro.html"}
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
def logout(request):
    auth.logout(request)
    #return HttpResponseRedirect('/intro/')
    return HttpResponseRedirect('/intro?page=1')
