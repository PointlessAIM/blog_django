from django.urls import path
from .views import ( 
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    like
    )

app_name='posts' # will throw an error if not included when using namespace in the include() function in core\urls.py

urlpatterns = [ #/entries/
    path('',PostListView.as_view() , name='entry-list'),
    path("create/", PostCreateView.as_view(), name="create"),
    path("<slug>/", PostDetailView.as_view(), name="detail"),
    path("<slug>/update", PostUpdateView.as_view(), name="update"),
    path("<slug>/delete", PostDeleteView.as_view(), name="delete"),
    path("<slug>/like", like, name="like")
    
    
]