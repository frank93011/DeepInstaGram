from django.shortcuts import render
from django.http import HttpResponse

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

def realized(request):
	data = {'gg': "intro.html"}
	return render(request, 'realized.html', data)
