from django.contrib import admin
from .models import (
    Customer,
    CustomerReview,
    Interval,
    NizaJobPosition,
    NizaEmployee,
    Project,
    ProjectFile,
    ProjectTask,
    ActivityLog,
    ActivityLogFile
)
from .forms import CustomerForm
# Register your models here.


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'first_name',
        'last_name',
        'phone_number'
    ]
    search_fields = [
        'first_name',
        'last_name',
        'phone_number',
        'email'
    ]
    form = CustomerForm


@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'created_at',
        'score',
        'customer',
        'title',
        'comment',
        'position'
    ]


@admin.register(Interval)
class IntervalAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'singular'
    ]


@admin.register(NizaJobPosition)
class NizaJobPositionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name'
    ]


@admin.register(NizaEmployee)
class NizaEmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'phone',
        'position'
    ]


class ProjectFileInline(admin.StackedInline):
    model = ProjectFile


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'created_at',
        'image',
        'employee',
        'interval',
        'time'
    ]
    inlines = (
        ProjectFileInline,
    )


@admin.register(ProjectTask)
class ProjectTaskAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'project',
        'task',
        'done',
        'order'
    ]
    list_filter = [
        'project',
    ]


class ActivityLogFileInline(admin.StackedInline):
    model = ActivityLogFile


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'project',
        'name',
        'files',
        'description'
    ]
    inlines = (
        ActivityLogFileInline,
    )

