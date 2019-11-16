from cookbook.Category import Category


class Recipe:

    def __init__(self, ingredients: dict, description: str, category: Category = None, photo: bytes = None):
        self._id = hash(self)
        self.category = category
        self.ingredients = ingredients
        self.description = description
        self.photo = photo

