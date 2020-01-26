from flask import Flask, render_template, redirect, url_for
import flights
import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sakndmsajdnjn2o13n123nndsajkdn'


"""SEARCH PAGE"""


@app.route('/')
# MUST BE @app.route('/') above this
def search():
    form = forms.SearchForm()
    if form.validate_on_submit():
        # save form data
        date = form.date.data
        origin = form.origin.data
        destination = form.destination.data
        redirect(url_for(
            'flights',
            date=date,
            origin=origin,
            destination=destination
        ))
    return render_template('search.html', form=form)


"""FLIGHTS PAGE"""


@app.route('/search/<date>/<origin>/<destination>')
def flights(date, origin, destination):
    # get data
    flights.flights_search(date, origin, destination)
    # render HTML
    return render_template(
        'flights.html',
        flights=flights
    )


"""RUN PROGRAM"""


if __name__ == '__main__':
    app.run(debug=True)
