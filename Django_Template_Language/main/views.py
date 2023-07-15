from django.shortcuts import render

def render_template(request):
    context = {'sp_Person':{'name':'Sam','role':'Manager','id':10},
               'list_of_people':["Jack", "John", "Harry", "Peter"],
               'productivity': 20}
    return render(request,'main/main_template.html',context)
