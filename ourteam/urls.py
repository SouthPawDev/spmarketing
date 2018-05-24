from django.urls import path
from ourteam import views as ourteam_views


app_name = 'ourteam'

urlpatterns = [
    path('', ourteam_views.OurTeam.as_view(), name='ourteam'),
    path('franchises', ourteam_views.FranchiseListView.as_view(), name='franchise_list'),
    path('franchises/<pk>', ourteam_views.FranchiseDetailView.as_view(), name='franchise_detail'),
    path('franchises/create/', ourteam_views.FranchiseCreateView.as_view(), name='franchise_create'),
    path('franchises/update/<pk>', ourteam_views.FranchiseUpdateView.as_view(), name='franchise_update'),
    path('franchises/delete/<pk>', ourteam_views.FranchiseDeleteView.as_view(), name='franchise_delete')
]
