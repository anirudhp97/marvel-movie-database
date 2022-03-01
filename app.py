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
    df = createDataframe(spiderMan)
    wordCloudSpidey(df)
    return render_template('spiderman.html', url='static/images/spidey/spidey/spidey.png')


@app.route('/venom2')
def Venom2():
    Venom2 = ia.get_movie('7097896')
    df = createDataframe(Venom2)
    wordCloudVenom2(df)
    return render_template('venom2.html', url='/static/images/venom2/venom2/venom2.png')

@app.route('/blackwidow')
def Blackwidow():
    blackWidow = ia.get_movie('3480822')
    df = createDataframe(blackWidow)
    wordCloudBlackWidow(df)
    return render_template('blackwidow.html', url='/static/images/blackwidow/blackwidow/blackwidow.png')

@app.route('/shangchi')
def Shangchi():
    shangChi = ia.get_movie('9376612')
    df = createDataframe(shangChi)
    wordCloudShangChi(df)
    return render_template('shangchi.html', url='/static/images/shangchi/shangchi/shangchi.png')

@app.route('/eternals')
def Eternals():
    Eternals = ia.get_movie('9032400')
    df = createDataframe(Eternals)
    wordCloudEternals(df)
    return render_template('eternals.html', url='/static/images/eternals/eternals.png')

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)