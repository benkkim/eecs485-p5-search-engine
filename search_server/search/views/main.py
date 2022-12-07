"""main.py."""
from threading import Thread
from search.config import SEARCH_INDEX_SEGMENT_API_URLS
import flask
import search
import search.model
import requests

# import threading
# import pathlib

def search_index(url, q_res, w_res, results, idx):
    """Search index."""
    end_point = f"{url}?q={q_res}&w={w_res}"
    try:
        response = requests.get(end_point)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err) from err
    res = response.json()
    results[idx] = res

@search.app.route("/", methods=["GET"])
def index():
    """Search"""
    q_res = flask.request.args.get("q", default=None, type=str)
    w_res = flask.request.args.get("w", default=None, type=float)
    context = {}
    if q_res is None:
        context["docs"] = []
        context["num_docs"] = 0
        return flask.render_template("index.html", **context), 200
    threads = []
    results = [[] for _ in range(len(SEARCH_INDEX_SEGMENT_API_URLS))]
    for idx, url in enumerate(SEARCH_INDEX_SEGMENT_API_URLS):
        thread = Thread(target=search_index, args=(url, q_res, w_res, results, idx))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    result_hits = []
    for result in results:
        result_hits.append(result["hits"])

    doc_ids = []
    for result in result_hits:
        for doc in result:
            doc_ids.append(doc)

    doc_ids.sort(key=lambda x: x["score"], reverse=True)

    if len(doc_ids) > 10:
        doc_ids = doc_ids[:10]

    con = search.model.get_db()

    for doc in doc_ids:
        cur = con.execute(
            "SELECT title, summary, url FROM Documents WHERE docid = ?",
            (doc["docid"],)
        )
        doc["doc"] = cur.fetchone()

    docs = [doc["doc"] for doc in doc_ids]
    context["docs"] = docs
    context["num_docs"] = len(docs)

    return flask.render_template("index.html", **context), 200
