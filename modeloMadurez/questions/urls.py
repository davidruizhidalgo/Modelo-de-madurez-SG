from django.urls import path
from .views import QuestionaryListView, QuestionaryDetailView, QuestionaryCreate, QuestionaryDelete
from .views import QuestionaryUpdate, QuestionaryUpdate_OS, QuestionaryUpdate_GO, QuestionaryUpdate_WAM
from .views import QuestionaryUpdate_TECH, QuestionaryUpdate_CUST, QuestionaryUpdate_VCI, QuestionaryUpdate_SE
from .views import ResultsDetailView, ChartsDetailView 

questionaty_patterns = ([
    path('', QuestionaryListView.as_view(), name='questionaries'),
    path('<int:pk>/<slug:slug>/', QuestionaryDetailView.as_view(), name='questionary'),
    path('results/<int:pk>/<slug:slug>/', ResultsDetailView.as_view(), name='tableresults'),
    path('charts/<int:pk>/<slug:slug>/', ChartsDetailView.as_view(), name='chartresults'),
    path('create/', QuestionaryCreate.as_view(), name='create'),
    path('update/<int:pk>/', QuestionaryUpdate.as_view(), name='update'),
    path('update_os/<int:pk>/', QuestionaryUpdate_OS.as_view(), name='update_OS'),
    path('update_go/<int:pk>/', QuestionaryUpdate_GO.as_view(), name='update_GO'),
    path('update_wam/<int:pk>/', QuestionaryUpdate_WAM.as_view(), name='update_WAM'),
    path('update_tech/<int:pk>/', QuestionaryUpdate_TECH.as_view(), name='update_TECH'),
    path('update_cust/<int:pk>/', QuestionaryUpdate_CUST.as_view(), name='update_CUST'),
    path('update_vci/<int:pk>/', QuestionaryUpdate_VCI.as_view(), name='update_VCI'),
    path('update_se/<int:pk>/', QuestionaryUpdate_SE.as_view(), name='update_SE'),
    path('delete/<int:pk>/', QuestionaryDelete.as_view(), name='delete'),
], 'questionaries')