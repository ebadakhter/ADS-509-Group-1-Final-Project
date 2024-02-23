from flask import Flask, render_template, flash, url_for,redirect
from forms import RecipesSearchForm
import pandas as pd
import json

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd2c44137ec36c4b1e41fcd54565313b4'


all_recipes = pd.read_csv('all_recipes.csv')


@app.route("/", methods=['GET', 'POST'])
def home():
    form = RecipesSearchForm()
    if form.validate_on_submit():
        result_df = all_recipes.loc[all_recipes['Ingredients'].str.contains(form.ingredients_search.data)]
        result = result_df.to_json(orient="records")
        return render_template('home.html', form=form, recipes=json.loads(result))
    return render_template('home.html', form=form)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    print()
    app.run(debug=True)