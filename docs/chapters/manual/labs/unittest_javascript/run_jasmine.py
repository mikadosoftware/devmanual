from flask import Flask, make_response

app = Flask(__name__)


def write_page():
    """Elements are some or all of
       project_list_table

    use some form of templating??? FOr now just string fomratting
    """

    tmpl = open('tmpl.html').read()
    return tmpl


@app.route("/")
def dashboard_home():

    return write_page()


@app.route("/workspace/")
def workspace():
    jsonstr = """ {"modules": [{"module_id": "6be277d4-373c-4533-947a-b5440951e5fd", "module_title": "fakeajaxresponse"}, {"module_id": "e725e723-e2a7-4cbf-98a1-7a745dd7999e", "module_title": "A title"}, {"module_id": "cb9ba131-6c0c-4b36-a3f1-aabb684c62d9", "module_title": "foobar"}]}"""

    jsonstr = open("/home/pbrian/src/public/pyhowto.examples/unittest_javascript/static/decl.json").read()

    resp = make_response(jsonstr)
    resp.content_type='application/json'
    resp.headers["Access-Control-Allow-Credentials"]= "true"
    return resp


if __name__ == "__main__":
    app.run(debug=True, port=5001)
