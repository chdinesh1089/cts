import django,sys, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cts.settings")
django.setup()
from django.contrib.auth.models import User
from complaint.models import Profile, Complaint
from django.contrib.auth import authenticate, login,logout
import random

def generate_database():
    for i in range(int(sys.argv[2]),int(sys.argv[3])):
        i= "{0:0=2d}".format(i)
        user_name = sys.argv[1] + str(i)
        pass_word = user_name
        email = user_name+ '@student.nitandhra.ac.in'
        user=User.objects.create_user(user_name, password = pass_word, email= email)
        Complaint.objects.create(author=user, title= "complaint_"+user_name, 
                                 description= "This is a complaint by "+user_name, 
                                 status = random.choice(Complaint.STATUS_CHOICES),
                                 category = random.choice(Complaint.CATEGORY_CHOICES))
        print(user_name)

generate_database()