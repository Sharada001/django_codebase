from django.shortcuts import render

def render_template(request):
    context = {'sp_Person':{'name':'Sam','role':'Manager','id':10},
               'list_of_people':["Jack", "John", "Harry", "Peter"],
               'productivity': 20,
               'reference_page': 'derived_template'}
    return render(request,'main/main_template.html',context)

def render_derived_template(request):
    context = {'sp_Person':{'name':'Sam','role':'Manager','id':10},
               'list_of_people':["Steve", "Henry", "Thomas", "Kane", "Bill"],
               'productivity': 80,
               'reference_page': 'template',
               'average_salary':50000}
    return render(request,'main/derived_template.html', context)
