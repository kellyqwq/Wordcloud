from wordcloud import WordCloud

def making_cloud(filename):
    txtfile = open(filename,'r').read()
    print('Finish read files... \nThe picture is generating...')
    wordcloud =  WordCloud(background_color = "white",width=1000, height=860, margin=2).generate(txtfile)
    return wordcloud
    # width,height,margin can be customised
    # generate is analysying the txt files
