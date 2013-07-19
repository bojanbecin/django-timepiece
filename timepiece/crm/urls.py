from django.conf.urls import patterns, url

from timepiece.crm import views


urlpatterns = patterns('',
    url(r'^search/$', views.search, name='search'),

    # Users
    url(r'^user/settings/$',
        views.edit_settings,
        name='edit_settings'),
    url(r'^user/$',
        views.list_users,
        name='list_users'),
    url(r'^user/create/$',
        views.create_edit_user,
        name='create_user'),
    url(r'^user/(?P<user_id>\d+)/$',
        views.ViewUser.as_view(),
        name='view_user'),
    url(r'^user/(?P<user_id>\d+)/edit/$',
        views.create_edit_user,
        name='edit_user'),
    url(r'^user/(?P<user_id>\d+)/delete/$',
        views.DeleteUser.as_view(),
        name='delete_user'),
    url(r'^user/(?P<user_id>\d+)/timesheet/' +
                '(?:(?P<active_tab>overview|all-entries|daily-summary)/)?$',
        views.view_user_timesheet,
        name='view_user_timesheet'),
    url(r'^user/(?P<user_id>\d+)/timesheet/reject/$',
        views.reject_user_timesheet,
        name='reject_user_timesheet'),
    url(r'^user/(?P<user_id>\d+)/timesheet/(?P<action>verify|approve)/$',
        views.change_user_timesheet,
        name='change_user_timesheet'),

    # Projects
    url(r'^project/$',
        views.list_projects,
        name='list_projects'),
    url(r'^project/create/$',
        views.create_edit_project,
        name='create_project'),
    url(r'^project/(?P<project_id>\d+)/$',
        views.ViewProject.as_view(),
        name='view_project'),
    url(r'^project/(?P<project_id>\d+)/edit/$',
        views.create_edit_project,
        name='edit_project'),
    url(r'^project/(?P<project_id>\d+)/delete/$',
        views.DeleteProject.as_view(),
        name='delete_project'),
    url(r'^project/(?P<project_id>\d+)/timesheet/$',
        views.ProjectTimesheet.as_view(),
        name='view_project_timesheet'),
    url(r'^project/(?P<project_id>\d+)/timesheet/csv/$',
        views.ProjectTimesheetCSV.as_view(),
        name='view_project_timesheet_csv'),

    # Businesses
    url(r'^business/$',
        views.list_businesses,
        name='list_businesses'),
    url(r'^business/create/$',
        views.create_edit_business,
        name='create_business'),
    url(r'^business/(?P<business_id>\d+)/$',
        views.ViewBusiness.as_view(),
        name='view_business'),
    url(r'^business/(?P<business_id>\d+)/edit/$',
        views.create_edit_business,
        name='edit_business'),
    url(r'^business/(?P<business_id>\d+)/delete/$',
        views.DeleteBusiness.as_view(),
        name='delete_business'),

    # Project relationships
    url(r'^relationship/create/$',
        views.create_relationship,
        name='create_relationship'),
    url(r'^relationship/edit/$',
        views.edit_relationship,
        name='edit_relationship'),
    url(r'^relationship/delete/$',
        views.delete_relationship,
        name='delete_relationship'),
)
