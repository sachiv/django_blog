from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog.blog'
    verbose_name = "Blog"
    verbose_name_plural = "Blog"

    def ready(self):
        import blog.blog.signals
        pass
