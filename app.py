#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

__all__ = []

import flask
import requests

app = flask.Flask(__name__)


@app.route("/css/arXiv.css")
def css():
    return flask.send_file("arXiv.css")


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    r = requests.get("http://arxiv.org/" + path,
                     params=flask.request.args)
    if r.status_code != requests.codes.ok:
        return flask.abort(r.status_code)
    return flask.Response(r.content, content_type=r.headers["content-type"])


if __name__ == "__main__":
    app.debug = True
    app.run()
