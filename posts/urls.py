from django.urls import path, re_path
from .views import ( 
    status_code_view, 
    entry_list, 
    EntryClassDetailView,
    EntryListView,
    post_create,
    EntryFormView
    )

app_name='posts' # will throw an error if not included when using namespace in the include() function in core\urls.py

urlpatterns = [ #/entries/
    #path('', redirect_home, name='red-home'),
    path('',entry_list , name='entry-list'),
    path('el/',EntryListView.as_view() , name='entry-list-class'),
    path('create/',EntryFormView.as_view() , name='entry-create'),
    #re_path('(?P<id>[0-4]{4}/$)', dummy_view, name='entry-detail-2'),
    path('sc/', status_code_view, name='status'),
    
]