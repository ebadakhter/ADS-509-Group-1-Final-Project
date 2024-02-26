from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class RecipesSearchForm(FlaskForm):
    ingredients_search = StringField('Ingredients Search(Separate multiple ingredients with commas)',
                         validators=[DataRequired(), Length(min=2, max=20)],
                                     render_kw={'style': 'font-size: 18px;'})
    dish_type = SelectField('Dish Type(Select One)',
                            choices=[
                                (None,''),
                                ('Main Dish(chicken)','Main Dish(chicken)'),
                                ('Main Dish(meat)','Main Dish(meat)'),
                                ('Desserts/Sweets','Desserts/Sweets'),
                                ('Sauces/sides/Appetizers', 'Sauces/sides/Appetizers'),
                                ('Salads', 'Salads')
                            ])
    search = SubmitField('Search')







