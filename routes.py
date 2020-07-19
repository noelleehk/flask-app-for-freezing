from flask import Flask, render_template
from pages_data import TIGERS

app = Flask(__name__)

# read the row needed from the data file
def get_values(source, slug):
    for row in source:
        if slug == row["slug"]:
            the_title = row["the_title"]
            image_alt = row["image_alt"]
            image_file = row["image_file"]
            image_credit = row["image_credit"]
            # return these if slug is valid
            return slug, the_title, image_alt, image_file, image_credit
    # if slug is not valid
    return "Unknown", "", "", "", ""


# one decorator, one function
@app.route('/<slug>.html')
def page(slug):
    # get values from data file
    slug, the_title, image_alt, image_file, image_credit = get_values(TIGERS, slug)
    # two options, depending whether slug was valid or not
    if slug == "Unknown":
        # redirect the browser to the error template
        return render_template('404.html', the_title="404 Error - Page Not Found"), 404
    else:
        # create the path to the file containing paragraphs
        filename = 'static/textfiles/' + slug + '.txt'
        # read that file into a variable
        with open(filename) as f:
            textfile = f.read()
        # create complete path to the image file
        image_location = 'images/' + image_file

        # send all the values to the template
        return render_template( 'page.html',
        the_title=the_title,
        image_alt=image_alt,
        image_file=image_location,
        image_credit=image_credit,
        textfile=textfile,
        data=TIGERS )

# route to handle an error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
