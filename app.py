from __future__ import print_function

from flask import Flask, render_template
from flask_restful import Api, Resource

from utils import get_videoDetails, search_similar


app = Flask(__name__)
api = Api(app)

# app.config.from_object('config.Config')
app.config.from_object('config.DevelopmentConfig')


@app.route('/')
def index():
    return render_template('index.html')


class SearchResults(Resource):
    def get(self, v_title, lang, ch_category):

        outLimit = 50

        video_details = get_videoDetails(v_title, [ch_category])
        video_sources = [
            v['_source'] for v in video_details['hits']['hits']
            if video_details.get('hits')
        ]

        data = []
        if len(video_sources) > 0:
            for video_source in video_sources:
                clust_num = video_source['clustNum']
                title = video_source['v_title_x']

                search_data = search_similar(
                    [lang], [ch_category], clust_num, title, outLimit)

                data.append(search_data)

        out = [item["_id"] for item in data["hits"]["hits"]]
        #print(out)
        outDict = {"user_id":1000021,"category":ch_category,"language":lang,"video_ids":out}
        
        return data


api.add_resource(SearchResults, '/search/<v_title>/<lang>/<ch_category>')


if __name__ == '__main__':
    app.run()
