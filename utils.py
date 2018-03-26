from elasticsearch import Elasticsearch


esConn = Elasticsearch(
    ['https://332b40d7283f80a6eb76542bd42f1ab8.ap-northeast-1.aws.found.io:9243/'],
    scheme='https',
    http_auth=('elastic', '19Svvwxyf3jKqtaY9RQVcfbv'),
    verify_certs=False)


def get_videoDetails(title, chCategory):

        query = {
            "_source": ['v_title_x', 'lang_vtitle', 'clustNum'],
            "query": {
                "bool": {
                    "must": [
                        {
                            "multi_match": {
                                "query": title
                            }
                        },
                        {"terms": {"chCategory": chCategory}},

                    ],
                }
            }
        }

        return esConn.search(
            index="videos",
            doc_type="doc",
            body=query
        )


def search_similar(lang, chCategory, clustNum, title, outLimit):
    query = {
        "_source": ['v_title_x', 'lang_vtitle', 'clustNum'],
        "query": {
            "bool": {
                "must": [
                    {
                        "multi_match": {
                            "query": title
                            # "fields": ["entities", "v_title_x"],
                            # "operator": "OR",
                        }
                    },
                    {"terms": {"lang_vtitle": lang}},
                    {"terms": {"chCategory": chCategory}},
                    # {"terms": {"clustNum": clustNum}},
                ],
            }
        }
    }

    return esConn.search(
        index="test-index",
        doc_type="doc",
        body=query,
        size=outLimit
    )
