from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(User):
    phone_number = models.CharField(
        max_length=12
    )

    class Meta:
        verbose_name_plural = 'Customers'
        verbose_name = 'Customer'


class CustomerReview(models.Model):
    created_at = models.DateField(
        auto_now_add=True
    )
    score = models.PositiveIntegerField()
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=50
    )
    comment = models.TextField()
    position = models.CharField(
        max_length=30
    )

    class Meta:
        verbose_name = 'Customer Review'
        verbose_name_plural = 'Cusomter Reviews'


class Interval(models.Model):
    name = models.CharField(
        max_length=10
    )
    singular = models.CharField(
        max_length=20
    )

    class Meta:
        verbose_name = 'Interval'
        verbose_name_plural = 'Intervals'

    def __str__(self):
        return '{}'.format(
            self.name
        )


class NizaJobPosition(models.Model):
    name = models.CharField(
        max_length=50
    )

    class Meta:
        verbose_name = 'Niza Job Position'
        verbose_name_plural = 'Niza Jobs positions'

    def __str__(self):
        return self.name


class NizaEmployee(models.Model):
    name = models.CharField(
        max_length=50
    )
    phone = models.CharField(
        max_length=10
    )
    position = models.ForeignKey(
        NizaJobPosition,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Niza Employee'
        verbose_name_plural = 'Niza Employees'

    def __str__(self):
        return '{} - {} # {}'.format(
            self.name,
            self.position,
            self.phone
        )


class Project(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    description = models.TextField()
    image = models.ImageField(upload_to='project_cover')
    employee = models.ForeignKey(
        NizaEmployee,
        on_delete=models.CASCADE
    )
    interval = models.ForeignKey(
        Interval,
        on_delete=models.CASCADE
    )
    time = models.PositiveIntegerField()
    order_id = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return '{} - {}'.format(
            self.customer,
            self.order_id
        )


class ProjectFile(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='files'
    )
    name = models.CharField(
        max_length=50,
        default='Archivo Niza'
    )
    file = models.FileField(
        upload_to='project_files'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Project File'
        verbose_name_plural = 'Project Files'


class ProjectTask(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    task = models.CharField(
        max_length=50
    )
    done = models.BooleanField(
        default=False
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-order']
        verbose_name = 'Project Task'
        verbose_name_plural = 'Project Tasks'


class ActivityLog(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='logs'
    )
    name = models.CharField(
        max_length=50
    )
    description = models.TextField()

    class Meta:
        verbose_name = 'Activity Log'
        verbose_name_plural = 'Activities Logs'

    def files(self):
        return ActivityLogFile.objects.filter(log=self).only('id').count()


class ActivityLogFile(models.Model):
    log = models.ForeignKey(
        ActivityLog,
        on_delete=models.CASCADE,
        related_name='logs'
    )
    file = models.FileField(
        upload_to='project_files'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Activity Log File'
        verbose_name_plural = 'Activities Logs File'

