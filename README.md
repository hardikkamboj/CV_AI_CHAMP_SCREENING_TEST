# CV_AI_CHAMP_SCREENING_TEST
![Code Vector Labs](https://user-images.githubusercontent.com/53142482/91476170-3b058500-e8ba-11ea-944e-be64dd75d13f.PNG)

## This repository contains my solutions for the screening test for CodeVector AI champ program. We were given four tasks to complete. 
(For more information, do visit the notebooks, i have tried to make them well commented and detailed)
## - Task 1: [Download 50 public profile PDFs of your connections (randomly) from LinkedIn.](/Task_1/)

This folder contains the linkedin profile PDF's of 50 of my connections which are downloaded randomly. The pdf are stored in the [data](https://github.com/hardikkamboj/CV_AI_CHAMP_SCREENING_TEST/tree/master/Task_1/data) folder.
You can view my linkedin profile [here](https://www.linkedin.com/in/hardik-kamboj-61288b19b/) 

## - Task 2: [Extract text from the above PDFs and store them in a CSV.](/Task_2/)
### Library Used
In this task we make the use of [Apache Tika](http://tika.apache.org/0.5/documentation.html) library to extract text from the pdf's that we got from the [previous task](/Task_1/). 
I used [Google Colab](https://colab.research.google.com/drive/1hlpaojcobuF7zuupBXI3NQDEjxJBKRe-) for executing the notebook. <br> 
### Uploading files to Google Colab
In the notebook [Extracting text from pdf](https://github.com/hardikkamboj/CV_AI_CHAMP_SCREENING_TEST/blob/master/Task_2/extracting_text_from_pdf.ipynb), i have shown have we can install tika in notebook with just a line of code. Data can be uploaded on Google Colab from local machine using files from google.colab.<br>
### Getting text from pdf, and getting the result as a csv file.
After importing the data, i have used [parser](https://tika.apache.org/0.7/parser.html) from tika to get the text from pdf. This is then stored in a pandas dataframe, which is then converted to csv file. The output file is [data.csv](https://github.com/hardikkamboj/CV_AI_CHAMP_SCREENING_TEST/blob/master/Task_2/data.csv) which is a csv file having 50 rows and 1 columns. <br> 
In the file each row corresponds to the data that is extracted from each pdf file. And hence it reults in 50 rows.

## - Task 3: [For every profile data (text), find out the most frequent words and essential words used.](/Task_3/)
### Cleaning the data
The [data we got from the last task](https://github.com/hardikkamboj/CV_AI_CHAMP_SCREENING_TEST/blob/master/Task_2/data.csv) contains many characters which are not useful. Therefore we need to clean the data so that it can then be used for further tasks. [In this notebook](https://github.com/hardikkamboj/CV_AI_CHAMP_SCREENING_TEST/blob/master/Task_3/Remove_stop_words_and_clean_data.ipynb), i have used [nltk](https://www.nltk.org/book/ch01.html) library to filter out stop words, words containing special characters, lowering the case for each word etc. The final output of this notebook is the [clean_data.csv](https://github.com/hardikkamboj/CV_AI_CHAMP_SCREENING_TEST/blob/master/Task_3/clean_data.csv), which is a csv flie containing 50 rows and 1 col. 
### Getting most frequent and most important words. 
In the notebook [Getting_most_frequent_words_and_essential_words.ipynb](https://github.com/hardikkamboj/CV_AI_CHAMP_SCREENING_TEST/blob/master/Task_3/Getting_most_frequent_words_and_essential_words.ipynb), i have demonstated how we can use the [clean_data.csv](https://github.com/hardikkamboj/CV_AI_CHAMP_SCREENING_TEST/blob/master/Task_3/clean_data.csv) to get the most frequent words and the most important words. 
#### Most frequent words. 
To get most important words i have used [Counter](https://docs.python.org/3.1/library/collections.html#:~:text=A%20Counter%20is%20a%20dict,including%20zero%20or%20negative%20counts.) from collections library. The file [freq_words_file.csv](https://github.com/hardikkamboj/CV_AI_CHAMP_SCREENING_TEST/blob/master/Task_3/freq_words_file.csv) is the csv file that we get which contains 50 rows, 1 column. For each of the 50 rows, it contains 10 most frequent words. We can attain any k frequent words by changing the agruement of the function find_k_most_frequent in [Getting_most_frequent_words_and_essential_words.ipynb](https://github.com/hardikkamboj/CV_AI_CHAMP_SCREENING_TEST/blob/master/Task_3/Getting_most_frequent_words_and_essential_words.ipynb)
#### Most important words 
To get the most important words, i have used the concept of [tf-idf](http://www.tfidf.com/#:~:text=Thus%2C%20the%20term%20frequency%20is,how%20important%20a%20term%20is.). I have used [Tf-idfVectorizor](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) from sklearn to implement tf idf. In each document, the word having the maximum tf-idf score is considered to be the most important. [Imp_words_file.csv](https://github.com/hardikkamboj/CV_AI_CHAMP_SCREENING_TEST/blob/master/Task_3/imp_words_file.csv) is a csv file which contains k (k = 10) most important words for each profile. We can change the value of k, by changing the arguemtent to the function find_important_words in [Getting_most_frequent_words_and_essential_words.ipynb](https://github.com/hardikkamboj/CV_AI_CHAMP_SCREENING_TEST/blob/master/Task_3/Getting_most_frequent_words_and_essential_words.ipynb)

## Task- 4 [4. Create two web APIs using flask/Django or another framework of your choice.](/Task_4/)
Here i have used Flask for making APIs. 
- ## [a. The first web API should take a PDF file as input and return the text in it in JSON format.](/Task_4/api_1_pdf_to_json/)
![Capture](https://user-images.githubusercontent.com/53142482/91533195-1a2a4780-e92d-11ea-840b-c580f4450c5c.PNG)
This Flask API takes input a pdf file, stores it in a local directory named uploads, uses the tika library that we dicussed in Task_2 , and converts it into a text file and stores it at local directory named downloads. 
This files is then returned as an output as a json file using [jsonify](https://www.fullstackpython.com/flask-json-jsonify-examples.html)  from flask library,
