from django.urls import path
from .views import ( 
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView
    )

app_name='posts' # will throw an error if not included when using namespace in the include() function in core\urls.py

urlpatterns = [ #/entries/
    path('',PostListView.as_view() , name='entry-list'),
    
    
]