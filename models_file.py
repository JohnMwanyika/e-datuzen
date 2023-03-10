# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Designation(models.Model):
    desig_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'designation'


class Milestone(models.Model):
    mile_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    milestone_statusstatus = models.ForeignKey('MilestoneStatus', models.DO_NOTHING, db_column='milestone_statusStatus_id')  # Field name made lowercase.
    projectproject = models.ForeignKey('Project', models.DO_NOTHING, db_column='projectProject_id')  # Field name made lowercase.
    created_at = models.DateTimeField()
    due_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'milestone'


class MilestoneStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'milestone_status'


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    project_statusstatus = models.ForeignKey('ProjectStatus', models.DO_NOTHING, db_column='project_statusStatus_id')  # Field name made lowercase.
    useruser = models.ForeignKey('User', models.DO_NOTHING, db_column='userUser_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project'


class ProjectStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'project_status'


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'role'


class Session(models.Model):
    id = models.CharField(primary_key=True, max_length=191)
    sid = models.CharField(unique=True, max_length=191)
    data = models.TextField()
    expiresat = models.DateTimeField(db_column='expiresAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'session'


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    milestonemile = models.ForeignKey(Milestone, models.DO_NOTHING, db_column='milestoneMile_id')  # Field name made lowercase.
    projectproject = models.ForeignKey(Project, models.DO_NOTHING, db_column='projectProject_id')  # Field name made lowercase.
    useruser = models.ForeignKey('User', models.DO_NOTHING, db_column='userUser_id')  # Field name made lowercase.
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    task_statusstatus = models.ForeignKey('TaskStatus', models.DO_NOTHING, db_column='task_statusStatus_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'task'


class TaskAssignment(models.Model):
    assignment_id = models.AutoField(primary_key=True)
    tasktask = models.ForeignKey(Task, models.DO_NOTHING, db_column='taskTask_id')  # Field name made lowercase.
    useruser = models.ForeignKey('User', models.DO_NOTHING, db_column='userUser_id')  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'task_assignment'


class TaskStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'task_status'


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    useruser = models.ForeignKey('User', models.DO_NOTHING, db_column='userUser_id')  # Field name made lowercase.
    projectproject = models.ForeignKey(Project, models.DO_NOTHING, db_column='projectProject_id')  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'team'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)
    phone = models.IntegerField(unique=True, blank=True, null=True)
    user_statusstatus = models.ForeignKey('UserStatus', models.DO_NOTHING, db_column='user_statusStatus_id')  # Field name made lowercase.
    rolerole = models.ForeignKey(Role, models.DO_NOTHING, db_column='roleRole_id', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    designationdesig = models.ForeignKey(Designation, models.DO_NOTHING, db_column='designationDesig_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class UserStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'user_status'
