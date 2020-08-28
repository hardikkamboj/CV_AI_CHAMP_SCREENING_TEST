# CV_AI_CHAMP_SCREENING_TEST
![Code Vector Labs](https://user-images.githubusercontent.com/53142482/91476170-3b058500-e8ba-11ea-944e-be64dd75d13f.PNG)

## This repository contains my solutions for the screening test for CodeVector AI champ program. We were given four tasks to complete. 
(Click for more information on each task.)
## - Task 1: [Download 50 public profile PDFs of your connections (randomly) from LinkedIn.](/Task_1/)
This folder contains the directory which contains the profile PDF's of 50 of my connections which are downloaded randomly. The pdf are stored in the [data](https://github.com/hardikkamboj/CV_AI_CHAMP_SCREENING_TEST/tree/master/Task_1/data) folder.
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
