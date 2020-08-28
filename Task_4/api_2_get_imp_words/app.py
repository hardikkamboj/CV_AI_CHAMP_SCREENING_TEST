import os
import pandas as pd
from flask import jsonify
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from sklearn.feature_extraction.text import TfidfVectorizer



UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'


app = Flask(__name__, static_url_path="/static")
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            get_imp_words(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('index.html')




def get_imp_words(path, filename):
    vectorizor = TfidfVectorizer()
    text_data = pd.read_csv('clean_data.csv')#stored in the same directory
    vectorizor.fit(list(text_data['text']))
    curr_file = open(path,'r')
    line = curr_file.read() #reading data from input file
    response = vectorizer.transform([line])
    feature_array = np.array(vectorizer.get_feature_names())
    tfidf_sorting = np.argsort(response.toarray()).flatten()[::-1]
    top_k = feature_array[tfidf_sorting][:k]
    output = open(app.config['DOWNLOAD_FOLDER'] + filename, 'wb')
    output.write(', '.join(top_k))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return jsonify(send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
