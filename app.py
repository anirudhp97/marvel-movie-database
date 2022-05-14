from imdb import IMDb
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask
from flask import render_template

app = Flask(__name__)

ia = IMDb()
nltk.download('stopwords')
stop_words = set().union(stopwords.words('english'))

def createDataframe(moviename):
    ia.update(moviename,['reviews'])
    sorted(ia.get_movie_infoset())
    jsonList = [review for review in moviename['reviews'] if review['rating']==None]
    df = pd.DataFrame.from_records(jsonList)
    return df

def wordCloudMorbius(df):
    df['processed_text'] = df['content'].str.lower().str.replace('(@[a-z0-9]+)\w+',' ').str.replace('(http\S+)', ' ').str.replace('([^0-9a-z \t])',' ').str.replace(' +',' ').apply(lambda x: [i for i in x.split(' ') if not i in stop_words])
    bigstring = df['processed_text'].apply(lambda x: ' '.join(x)).str.cat(sep=' ')
    plt.figure(figsize=(12,12))
    wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white',
                          collocations=False,
                          width=1200,
                          height=1000
                         ).generate(bigstring)
    plt.axis('off')
    wordcloud.to_file("static/images/morbius/morbius/morbius.png")
    
def wordCloudDoctorStrange(df):
    df['processed_text'] = df['content'].str.lower().str.replace('(@[a-z0-9]+)\w+',' ').str.replace('(http\S+)', ' ').str.replace('([^0-9a-z \t])',' ').str.replace(' +',' ').apply(lambda x: [i for i in x.split(' ') if not i in stop_words])
    bigstring = df['processed_text'].apply(lambda x: ' '.join(x)).str.cat(sep=' ')
    plt.figure(figsize=(12,12))
    wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white',
                          collocations=False,
                          width=1200,
                          height=1000
                         ).generate(bigstring)
    plt.axis('off')
    wordcloud.to_file("static/images/doctorstrange/doctorstrange/doctorstrange.png")
    
def wordCloudSpidey(df):
    df['processed_text'] = df['content'].str.lower().str.replace('(@[a-z0-9]+)\w+',' ').str.replace('(http\S+)', ' ').str.replace('([^0-9a-z \t])',' ').str.replace(' +',' ').apply(lambda x: [i for i in x.split(' ') if not i in stop_words])
    bigstring = df['processed_text'].apply(lambda x: ' '.join(x)).str.cat(sep=' ')
    plt.figure(figsize=(12,12))
    wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white',
                          collocations=False,
                          width=1200,
                          height=1000
                         ).generate(bigstring)
    plt.axis('off')
    wordcloud.to_file("static/images/spidey/spidey/spidey.png")
    
def wordCloudBlackWidow(df):
    df['processed_text'] = df['content'].str.lower().str.replace('(@[a-z0-9]+)\w+',' ').str.replace('(http\S+)', ' ').str.replace('([^0-9a-z \t])',' ').str.replace(' +',' ').apply(lambda x: [i for i in x.split(' ') if not i in stop_words])
    bigstring = df['processed_text'].apply(lambda x: ' '.join(x)).str.cat(sep=' ')
    plt.figure(figsize=(12,12))
    wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white',
                          collocations=False,
                          width=1200,
                          height=1000
                         ).generate(bigstring)
    plt.axis('off')
    wordcloud.to_file("static/images/blackwidow/blackwidow/blackwidow.png")
    
def wordCloudShangChi(df):
    df['processed_text'] = df['content'].str.lower().str.replace('(@[a-z0-9]+)\w+',' ').str.replace('(http\S+)', ' ').str.replace('([^0-9a-z \t])',' ').str.replace(' +',' ').apply(lambda x: [i for i in x.split(' ') if not i in stop_words])
    bigstring = df['processed_text'].apply(lambda x: ' '.join(x)).str.cat(sep=' ')
    plt.figure(figsize=(12,12))
    wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white',
                          collocations=False,
                          width=1200,
                          height=1000
                         ).generate(bigstring)
    plt.axis('off')
    wordcloud.to_file("static/images/shangchi/shangchi/shangchi.png")
    
def wordCloudVenom2(df):
    df['processed_text'] = df['content'].str.lower().str.replace('(@[a-z0-9]+)\w+',' ').str.replace('(http\S+)', ' ').str.replace('([^0-9a-z \t])',' ').str.replace(' +',' ').apply(lambda x: [i for i in x.split(' ') if not i in stop_words])
    bigstring = df['processed_text'].apply(lambda x: ' '.join(x)).str.cat(sep=' ')
    plt.figure(figsize=(12,12))
    wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white',
                          collocations=False,
                          width=1200,
                          height=1000
                         ).generate(bigstring)
    plt.axis('off')
    wordcloud.to_file("static/images/venom2/venom2/venom2.png")
    
    
def wordCloudEternals(df):
    df['processed_text'] = df['content'].str.lower().str.replace('(@[a-z0-9]+)\w+',' ').str.replace('(http\S+)', ' ').str.replace('([^0-9a-z \t])',' ').str.replace(' +',' ').apply(lambda x: [i for i in x.split(' ') if not i in stop_words])
    bigstring = df['processed_text'].apply(lambda x: ' '.join(x)).str.cat(sep=' ')
    plt.figure(figsize=(12,12))
    wordcloud = WordCloud(stopwords=STOPWORDS,
                          background_color='white',
                          collocations=False,
                          width=1200,
                          height=1000
                         ).generate(bigstring)
    plt.axis('off')
    wordcloud.to_file("static/images/eternals/eternals.png")
    
@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/spiderman')
def spiderMan():
    spiderMan = ia.get_movie('10872600')
    spidey_rating_fetch = ia.get_movie('10872600', 'vote details')
    spidey_rating = spidey_rating_fetch.get('arithmetic mean')
    df = createDataframe(spiderMan)
    wordCloudSpidey(df)
    return render_template('spiderman.html', url='static/images/spidey/spidey/spidey.png', spideyrating='Rating: {}/10'.format(spidey_rating))

@app.route('/morbius')
def Morbius():
    morbius = ia.get_movie('5108870')
    morbius_rating_fetch = ia.get_movie('5108870', 'vote details')
    morbius_rating = morbius_rating_fetch.get('arithmetic mean')
    df = createDataframe(morbius)
    wordCloudMorbius(df)
    return render_template('morbius.html', url='static/images/morbius/morbius/morbius.png', morbiusrating='Rating: {}/10'.format(morbius_rating))

@app.route('/venom2')
def Venom2():
    Venom2 = ia.get_movie('7097896')
    venom2_rating_fetch = ia.get_movie('7097896', 'vote details')
    venom2_rating = venom2_rating_fetch.get('arithmetic mean')
    df = createDataframe(Venom2)
    wordCloudVenom2(df)
    return render_template('venom2.html', url='/static/images/venom2/venom2/venom2.png', venomrating='Rating: {}/10'.format(venom2_rating))

@app.route('/blackwidow')
def Blackwidow():
    blackWidow = ia.get_movie('3480822')
    blackWidow_rating_fetch = ia.get_movie('3480822', 'vote details')
    blackWidow_rating = blackWidow_rating_fetch.get('arithmetic mean')
    df = createDataframe(blackWidow)
    wordCloudBlackWidow(df)
    return render_template('blackwidow.html', url='/static/images/blackwidow/blackwidow/blackwidow.png', blackwidowrating='Rating: {}/10'.format(blackWidow_rating))

@app.route('/shangchi')
def Shangchi():
    shangChi = ia.get_movie('9376612')
    shangchi_rating_fetch = ia.get_movie('9376612', 'vote details')
    shangchi_rating = shangchi_rating_fetch.get('arithmetic mean')
    df = createDataframe(shangChi)
    wordCloudShangChi(df)
    return render_template('shangchi.html', url='/static/images/shangchi/shangchi/shangchi.png', shangchirating='Rating: {}/10'.format(shangchi_rating))

@app.route('/eternals')
def Eternals():
    Eternals = ia.get_movie('9032400')
    eternals_rating_fetch = ia.get_movie('9032400', 'vote details')
    eternals_rating = eternals_rating_fetch.get('arithmetic mean')
    df = createDataframe(Eternals)
    wordCloudEternals(df)
    return render_template('eternals.html', url='/static/images/eternals/eternals.png', eternalsrating='Rating: {}/10'.format(eternals_rating))

@app.route('/doctorstrange')
def Doctorstrange():
    Doctorstrange = ia.get_movie('9419884')
    doctorstrange_rating_fetch = ia.get_movie('9419884', 'vote details')
    doctorstrange_rating = doctorstrange_rating_fetch.get('arithmetic mean')
    df = createDataframe(Doctorstrange)
    wordCloudDoctorStrange(df)
    return render_template('doctorstrange.html', url='/static/images/doctorstrange/doctorstrange.png', doctorstrangerating='Rating: {}/10'.format(doctorstrange_rating))

@app.route('/thorloveandthunder')
def Thor():
    #Thor = ia.get_movie('10648342')
    #thor_rating_fetch = ia.get_movie('10648342', 'vote details')
    #thor_rating = thor_rating_fetch.get('arithmetic mean')
    #df = createDataframe(Thor)
    #wordCloudThor(df)
    return render_template('thorloveandthunder.html')

@app.route('/blackpanther')
def BlackPanther():
    #BlackPanther = ia.get_movie('10648342')
    #blackpanther_rating_fetch = ia.get_movie('10648342', 'vote details')
    #blackpanther_rating = blackpanther_rating_fetch.get('arithmetic mean')
    #df = createDataframe(BlackPanther)
    #wordCloudBlackPanther(df)
    return render_template('blackpanther.html')

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)