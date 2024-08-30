# Experimenting AI and webscrapping to perform competitor analysis

# Goal
In this projetc I used **web scrapping** on the website **Trustpilot** to accumulate 1600 bad reviews of two competitor, Hostinger and Bleuhost. Then, with a AI model I was able to **automaticly labeling** a category to each reviews. Which will allow me to perform a competitor analysis, highlighting both strenghts and weakness of those companies.

# AI Model
The task we want to do is **Zero shot classification** of text data.
The model used is "Comprehend-it-base" by Knowledgator. This is a model based on DeBERTaV3-base that was trained on natural language inference datasets as well as on multiple text classification datasets. It demonstrates better quality on the diverse set of text classification datasets in a zero-shot setting than Bart-large-mnli while being almost 3 times smaller. Moreover, the model can be used for multiple information extraction tasks in zero-shot setting.

# Tool
- Selenium
- Pandas
- Matplotlib
- Seaborn
