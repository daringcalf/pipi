import multiprocessing

projectname = 'simplestory'
base = '/home/nobia/django_test/simplestory'

bind = "0.0.0.0:7529"
workers = multiprocessing.cpu_count() * 2 + 1
pythonpath = base
chdir = base
# module = "{}.wsgi:application".format(projectname)