#  EASY Logic Project by @w3nabil 

from flask import Flask, render_template, send_from_directory, request
import os, random , string

app = Flask(__name__, template_folder='public')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/short' , methods=['POST'])
def short():
  if request.method == 'POST':
    def shortlink_id():
      id = "".join(random.choice(string.ascii_lowercase) for i in range(6))
      return id
    id = shortlink_id() 
    url = request.form['url']
    os.makedirs(f"./go/{id}")
    with open(f"./go/{id}/index.html", "w") as g:
      g.write(f'<script>location.replace("{url}")</script>')
    return render_template('short.html', id=id, url=url)

@app.route('/go/<path:subdir>')
def serve_subdir_index(subdir):
    folder_path = os.path.join(os.getcwd(), 'go', subdir)
    return send_from_directory(folder_path, 'index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def run():
  app.run(host="0.0.0.0", port=5000, debug=True)

run()
