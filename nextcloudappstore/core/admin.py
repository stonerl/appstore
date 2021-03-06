from django.contrib import admin
from nextcloudappstore.core.models import *


class DatabaseDependencyInline(admin.TabularInline):
    model = DatabaseDependency
    extra = 1


class PhpExtensionDependencyInline(admin.TabularInline):
    model = PhpExtensionDependency
    extra = 1


class AppReleaseAdmin(admin.ModelAdmin):
    inlines = (DatabaseDependencyInline, PhpExtensionDependencyInline)


admin.site.register(App)
admin.site.register(AppRelease, AppReleaseAdmin)
admin.site.register(Screenshot)
admin.site.register(Author)
admin.site.register(ShellCommand)
admin.site.register(Category)
admin.site.register(Database)
admin.site.register(DatabaseDependency)
admin.site.register(PhpExtension)
admin.site.register(PhpExtensionDependency)
