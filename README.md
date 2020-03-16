# DIG - Deep InstaGram 

## Description
This projects is a demo version of our **Instagram users analysis system**.
It did not contain any visual or language model. if you want to understand more of this projects please contact me.

This system was built under python Django.
To run the project, please enter the venv and activate the environment. Then run:
```python=
    python manage.py runserver
```
then open your browser and open: http://127.0.0.1:8000/

## Demo Video
{%youtube 1CAoO7Lk6Ms %}
## Motivation
* Can we reveal our true personality based on what we post on social media?
* Can computer identify a "Style" of a photo?

## What we want to achieve 
**Categorize the common style that people will post on instagram**
→ Using these data we can summerize the IG users' most common style. 
→ We can therefore find the matching brands or products that we can recommand to them.

**Based on their posts, finding out the BIG5 Personality of the IG users**
→ Human Resourse department can therefore use it as a selection standard.

## How we do it
First we catgorized 13 ig common posts styles:
* Adventure
* Cute animals & Infants
* Studying
* Night Club or Party
* Colorful Sky
* Fireworks and Night View
* Sports
* Depressed 
* Lonely
* Selfies
* Architecture
* Delicacy
* Illustration or others

Then we parse down the related hashtagged pictures in 500px.
Using these images as training data to build our CNN models.
We use VGG16 and MobileNet as a base of our transfer Learning Model.
reference: https://github.com/keras-team/keras-applications

### Heatmap for our image prediciton
![](https://i.imgur.com/SzFp0tX.png)


**AVG F1-Score:** 0.74

We then move on to the next step. The team and I design an servey form to collect Instagram users' BIG5 Personality data for about 500 people participated in. We then asked them to provide their IG Posts as training materials.

We discover that the text parts of user's posts have more influence on their possible personality. therefore we build up 5 different SVM model to predict each users' significance on each personalitys:
* Openness
* Conscientoiusness
* Extraversion
* Aggreeableness
* Neuroticism

### Accuracy for our personality significance prediction
![](https://i.imgur.com/dc5bxyx.png)

**AVG F1-Score:** 0.81

We also use users' posts text to predicts their possible habbits(also servey in our form)
the performance is showing below:
### Accuracy for our possible habbits prediction
![](https://i.imgur.com/EviSLng.png)

-----
**For more about this project report, you can see also this slide:**
https://docs.google.com/presentation/d/1PQR7ECnQ1DND_mHhxyqPbA9TDbbAYnDEml8o3siWXBI/edit?usp=sharing