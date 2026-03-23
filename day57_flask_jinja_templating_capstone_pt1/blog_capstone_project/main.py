import requests
from flask import Flask, render_template
from day57_flask_jinja_templating_capstone_pt1.blog_capstone_project.post import Post


""" Send Request for all post - save in an array """
headers = {
    "Content-type": "application/json",
}

# Used myjson.online instead of npoint (it was blocked by ISP)
blog_bin_url = "https://api.myjson.online/v1/records/f9fd64cd-0481-46e6-addb-9e3fd0fc92d2"
response = requests.get(blog_bin_url, verify=False, headers=headers)
all_posts = response.json()

post_array = []
for post in all_posts['data']:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_array.append(post_obj)

app = Flask(__name__)

@app.route('/')
def get_blog():
    return render_template("starter.html", posts=post_array)


@app.route("/post/<int:id>")
def get_post(id):
    selected_post = None
    for blog_post in post_array:
        if blog_post.id == id:
            selected_post = blog_post

    return render_template("post.html", post=selected_post)



if __name__ == "__main__":
    app.run(debug=True)


