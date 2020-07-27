from django.apps import AppConfig



class StudyblogAdminConfig(AppConfig):
    name = 'StudyBlog_admin'
    verbose_name=  'вайшнавский университет'
    def ready(self):
        import StudyBlog_admin.signals