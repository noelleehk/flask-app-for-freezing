# Example Flask App for Freezing

The template file `base.html` is used as a shell following Jinja2 template rules. The template file `page.html` is used by all five pages in this site. There is only one route for all the pages.

## Explore the app

After installing all dependencies, run the app by entering its folder and typing:

`$ python routes.py`

Explore the five pages in your browser, and then study the file structure in the repo.

* Note that there is only ONE route for all five pages.
* Note that the pages are essentially generated from a data file and some text files.

## See how “freezing” works

Shut down Flask's web server with Control-c. Then type:

`$ python freeze.py`

Now explore the new folder, **build**, that was created. Open the pages inside that folder in both your browser and your text editor.
