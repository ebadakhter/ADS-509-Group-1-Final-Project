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
        ingredients_list = [ingredient.strip().lower() for ingredient in form.ingredients_search.data.split(',')]

        # Initialize an empty list to store matching recipes
        matching_recipes = []

        # Iterate through each recipe
        for _, recipe in all_recipes.iterrows():
            recipe_ingredients = recipe['Ingredients'].lower()

            # Check if all specified ingredients are in the recipe
            if all(ingredient in recipe_ingredients for ingredient in ingredients_list):
                matching_recipes.append(recipe.to_dict())

        result = json.dumps(matching_recipes)
        return render_template('home.html', form=form, recipes=json.loads(result))

    return render_template('home.html', form=form)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    print()
    app.run(debug=True)