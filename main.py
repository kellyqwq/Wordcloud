from generate_wordcloud import making_cloud

filename = input('Please enter the file name with same directory: ')

try:
    wordcloud = making_cloud(filename)
except:
    print('Error: Fails to open file!')
    quit()

import matplotlib.pyplot as plt
try:
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
except:
    print('Error: Fails to make picture!')

filename = filename.split('.')
print('Finish generating!')
wordcloud.to_file(filename[0] + '.png')
#Saving the file