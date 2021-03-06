from flask import (
    Flask,
    render_template,
    Markup,
    url_for,
    flash,
    redirect,
    request
)

import sendgrid
from datetime import date

app = Flask(__name__)
app.config["SECRET_KEY"] = "some_really_long_random_string_here"
app.config['TESTING'] = True

'''sendgrid_file = "sendgrid.txt"
sendgrid_details = []

with open(sendgrid_file) as f:
    sendgrid_details = f.readlines()
    sendgrid_details = [x.strip("\n") for x in sendgrid_details] 
    
    '''

products_info = [
    {
        "id": "101",
        "name": "GUCCI",
        "img": "shirt-101.jpg",
        "price": 180,
        "paypal": "LNRBY7XSXS5PA",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "102",
        "name": "Louis Vuitton",
        "img": "shirt-102.jpg",
        "price": 350,
        "paypal": "XP8KRXHEXMQ4J",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "103",
        "name": "BAPE",
        "img": "shirt-103.jpg",
        "price": 100,
        "paypal": "95C659J3VZGNJ",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "104",
        "name": "Supreme x LV",
        "img": "shirt-104.jpg",
        "price": 500,
        "paypal": "Z5EY4SJN64SLU",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "105",
        "name": "ASSC",
        "img": "shirt-105.jpg",
        "price": 70,
        "paypal": "RYAGP5EWG4V4G",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "106",
        "name": "Tommy Hilfiger",
        "img": "shirt-106.jpg",
        "price": 50,
        "paypal": "QYHDD4N4SMUKN",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "107",
        "name": "COM DES GARCON",
        "img": "shirt-107.jpg",
        "price": 100,
        "paypal": "RSDD7RPZFPQTQ",
        "sizes": ["Small", "Medium", "Large"]
    },

    {
        "id": "108",
        "name": "PALACE",
        "img": "shirt-108.jpg",
        "price": 40,
        "paypal": "LFRHBPYZKHV4Y",
        "sizes": ["Small", "Medium", "Large"]
    }
]



def get_list_view_html(product):

    output = ""
    image_url = url_for("static", filename=product["img"])
    shirt_url = url_for("shirt", product_id=product["id"])
    output = output + "<li>"
    output = output + '<a href="' + shirt_url + '">'
    output = (
        output + '<img src="' + image_url +
        '" al  t="' + product["name"] + '">')
    output = output + "<p>View Details</p>"
    output = output + "</a>"
    output = output + "</li>"

    return output


# Routes
# All functions should have a page_title variables if they render templates

@app.route("/")
def index():
    context = {"page_title": "HYPEBEAST STORE", "current_year": date.today().year}
    counter = 0
    product_data = []
    for product in products_info:
        counter += 1
        if counter < 5:  # Get first 4 shirts
            product_data.append(
                Markup(get_list_view_html(product))
            )
    context["product_data"] = Markup("".join(product_data))
    flash("do not buy anything")
    return render_template("index.html", **context)


@app.route("/shirts")
def shirts():
    context = {"page_title": "HYPEBEAST STORE", "current_year": date.today().year}
    product_data = []
    for product in products_info:
        product_data.append(Markup(get_list_view_html(product)))
    context["product_data"] = Markup("".join(product_data))
    flash("do not buy anything")
    return render_template("shirts.html", **context)


@app.route("/shirt/<product_id>")
def shirt(product_id):
    context = {"page_title": "HYPEBEAST STORE", "current_year": date.today().year}
    my_product = ""
    for product in products_info:
        if product["id"] == product_id:
            my_product = product
    context["product"] = my_product
    flash("do not buy anything")
    return render_template("shirt.html", **context)


@app.route("/receipt")
def receipt():

    context = {"page_title": "HYPEBEAST STORE", "current_year": date.today().year}
    return render_template("receipt.html", **context)


@app.route("/contact")
def contact():
    context = {"page_title": "HYPEBEAST STORE", "current_year": date.today().year}
    return render_template("contact.html", **context)


@app.route("/send", methods=['POST'])
def send():
#    sendgrid_object = sendgrid.SendGridClient(sendgrid_details[0], sendgrid_details[1])
    message = sendgrid.Mail()
    sender = request.form["email"]
    subject = request.form["name"]
    body = request.form["message"]
    message.add_to("charlie.thomas@attwoodthomas.net")
    message.set_from(sender)
    message.set_subject(subject)
    message.set_html(body)
 #   sendgrid_object.send(message)
    flash("Email sent.")
    return redirect(url_for("contact"))


if __name__ == "__main__":
    app.run(debug=True)
