import tkinter as tk
from textblob import TextBlob
from newspaper import Article

# Function to summarize the article and perform sentiment analysis
def summarize():
    url = urltext.get('1.0', "end").strip()

    # Download and parse the article
    article = Article(url)
    article.download()
    article.parse()

    # Perform natural language processing on the article
    article.nlp()

    # Enable text fields for displaying the results
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    # Clear the previous content
    title.delete('1.0', 'end')
    author.delete('1.0', 'end')
    publication.delete('1.0', 'end')
    summary.delete('1.0', 'end')
    sentiment.delete('1.0', 'end')

    # Update the text fields with the article information
    title.insert('1.0', article.title)
    author.insert('1.0', article.authors)
    publication.insert('1.0', article.publish_date)
    summary.insert('1.0', article.summary)

    # Perform sentiment analysis using TextBlob
    analysis = TextBlob(article.text)
    polarity = analysis.polarity

    # Insert sentiment analysis results into the text field
    sentiment.insert('1.0', f"Polarity: {polarity}, Sentiment: {'positive' if polarity > 0 else 'negative' if polarity < 0 else 'neutral'}")

    # Disable text fields after displaying the results
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

# Create the main window
root = tk.Tk()
root.title('News Summarizer')
root.geometry("1200x600")
root.configure(bg="sky blue")

# Create labels and text fields for displaying the article information
tlabel = tk.Label(root, text='Title')
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='white')
title.pack()

alabel = tk.Label(root, text='Author')
alabel.pack()
author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='white')
author.pack()

plabel = tk.Label(root, text='Publication Date')
plabel.pack()
publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='white')
publication.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()
summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='white')
summary.pack()

selabel = tk.Label(root, text='Sentiment Analysis')
selabel.pack()
sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='white')
sentiment.pack()

ulabel = tk.Label(root, text='URL')
ulabel.pack()
urltext = tk.Text(root, height=1, width=140)
urltext.pack()

btn = tk.Button(root, text='Summarize', command=summarize)
btn.pack()

root.mainloop()
