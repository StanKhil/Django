from django.urls import path
from main.views import *

urlpatterns = [
    path("prediction/", prediction),

    path("random/number/", random_number),
    path("random/number/range/", random_number_range),
    path("random/number/set/", random_number_set),

    path("poems/random/", random_poem),
    path("poems/random/author/<int:author_id>/", random_poem_by_author),
    path("poems/random/theme/<int:theme_id>/", random_poem_by_theme),

    path("authors/", authors_list),
    path("themes/", themes_list),
    path("poems/author/<int:author_id>/", poems_by_author),
    path("poems/theme/<int:theme_id>/", poems_by_theme),
]