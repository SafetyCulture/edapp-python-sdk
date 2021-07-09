from edapp_python_sdk import edapppy, main
import pandas as pd
import os

os.chdir(r'C:\Users\mills\Google Drive\Current Work\PowerBI\EdApp\PBI-Connector')
frames = main.export_all()
users = pd.DataFrame(frames['users'])
user_groups = pd.DataFrame(frames['user_groups'])
user_group_children = pd.DataFrame(frames['user_group_children'])
group_users = pd.DataFrame(frames['group_users'])
courses = pd.DataFrame(frames['courses'])
custom_fields = pd.DataFrame(frames['custom_fields'])
lessons = pd.DataFrame(frames['lessons'])
survey_answers = pd.DataFrame(frames['survey_answers'])
attempts = pd.DataFrame(frames['attempts'])
courseprogress = pd.DataFrame(frames['courseprogress'])
coursestatistics = pd.DataFrame(frames['coursestatistics'])