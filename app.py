from flask import Flask, render_template, request, jsonify
import requests
import re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search_movies():
    query = request.args.get('query')
    api_key = '04aae18c13755d9ce23441e1221b3529'
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        movies = response.json()['results']
        formatted_movies = [{
            'id': movie['id'],
            'title': movie['title'],
            'poster_path': movie['poster_path']
        } for movie in movies]
        return jsonify(formatted_movies)
    except Exception as e:
        print('Error fetching movies:', e)
        return "<script>alert(f\"Error fetching movies:', {e}\")", 500

# code below by gabrielzv1233, code above made by DeSu32
@app.route('/movie/<path:tmdb_movie_id>')
def movie(tmdb_movie_id):
    api_key = '04aae18c13755d9ce23441e1221b3529'
    url = f"https://api.themoviedb.org/3/movie/{tmdb_movie_id}?api_key={api_key}"

    response = requests.get(url)
    movie_data = response.json()

    return render_template("movie.html", iframe=get_embed(movie_data['title'].lower()), title=movie_data['title'])
    
def get_embed(title):
    filteredtitle = title.replace(" ", "-")
    url = f"https://w1.nites.is/movies/{filteredtitle}/"
    response = requests.get(url)
    html_content = response.text

    match = re.search('<link itemprop="embedUrl" href="(.*?)">', html_content)
    if match:
        movie_url = match.group(1)
        movie_url = movie_url.replace(r"#038", r"amp")
        movie_url = movie_url.replace(r"&trtype=1", r"&amp;trtype=1")
        iframe = f'<iframe class="movie_iframe" frameborder="0" allowfullscreen="" data-lazy-src="{movie_url}" data-lazy-method="viewport" data-lazy-attributes="src" src="{movie_url}" data-gtm-yt-inspected-6="true"></iframe>'
        return iframe
    else:
        print("No movie URL found.")
        return f"original title{title} filtered {filteredtitle} request url {url}"

if __name__ == '__main__':
    app.run(debug=True)
