from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
# def home_page(request):
#     return HttpResponse("This is our home page!")
# def python_intro(request):
#     return HttpResponse("And this is Pyhton introduction page!")
# def django_basics(request):
#     return HttpResponse("Now,\nCome to the next topic.\n" \
#     "That is Django basic!\n Here i am learning django basics")

# def home_page(request):
#     return HttpResponse("<h1>This is home page!!<h1/>")


# def blog_post(request,blog):
#     if blog == 'advance_math':
#         return HttpResponse("<h1>this page for advance math!<h1/>")
#     elif blog == 'python':
#         return HttpResponse("<h1>And this is Pyhton introduction page!<h1/>")
#     elif blog == 'django':
#         return HttpResponse("<h1>Now,\nCome to the next topic.\n" \
#                             "That is Django basic!\n Here i am learning django basics<h1/>")
    
#     return HttpResponseNotFound("<h1>Blog not found<h1/>")

# def for_int(int,blog):
#     return HttpResponse(f"<h1>int:{blog}<h1/>")
# def for_str(str,blog):
#     return HttpResponse(f"you entered a string!:{blog}")

# def blog_posts(request,blog):
#     url_name = {
#     'math'   :  "<h1>this page for advance math!<h1/>",
#     'python' :  "<h1>And this is Pyhton introduction page!<h1/>",
#     'django' :  "<h1>Now,\nCome to the next topic.\n That is Django basic!\n Here i am learning django basics<h1/>"
#     }


#     content = url_name.get(blog)

#     if content != None:
#       return HttpResponse (content)
#     else:
#       return HttpResponseNotFound("<h1>Blog not found<h1/>")

# def all_posts(request):
#         data2 = """
#     <h1>This is our All blog posts!!<h1/>

#     <ul>
#         <li>
#             <a href = "/all-posts/math/" > Math </a>
#         </li>
#          <li>    
#             <a href = "/all-posts/python/" > Python </a>
#         </li>
#          <li>
#              <a href = "/all-posts/django/" > Django </a>
#         </li>
#          <li>
#              <a href = "/all-posts/regex/" > Regex </a>
#         </li>
#          <li>
#              <a href = "/all-posts/oops/" > OOPs </a>
#         </li>
#     </ul>

#     """
#         return HttpResponse(data2)    









url_name = {
    'math'   :"This page for advance math!",
    'python' :"And this is Pyhton introduction page!",
    'django' :"Now,Come to the next topic. That is Django basic! Here i am learning django basics",
    'regex'  :"Regular Expression in Python! ",
    'oops'   :"Object oriented programing in Python! ",
    'tkinter': None
    }  


def home_page(request):
    return render(request,"blogs/01. index.html") 
    # res_data = render_to_string("index.html")
    # return HttpResponse(res_data)

def all_posts(request):
    blog_list = list(url_name.keys())
    
    return render(request,"blogs/02. blog_list.html",{"bloglist": blog_list}) 

    # list_items = ""
    # blog_list = list(url_name.keys())

    # for b in blog_list:
    #     blog_path = reverse("allposts",args = [b])
    #     list_items += f"<li> <a href = {blog_path}> {b.capitalize()} </a> </li>"
    # data2 = f"<h1> This is our All blog posts!! <ul> {list_items} </ul> </h1>"    

    return render(request,"blogs/02. blog_list.html")    


# def process_blog_name():
#     blog_list = blog.split("-")   
#     return " ".join(blog_list).title()

def blog_posts(request,blog):
    try:
        res =  url_name[blog]
        # return render(request,"blogs/posts.html",{"blog_text":res,  "url_name" : blog.title()})
        return render(request,"blogs/03. posts.html",{"blog_text":res,  "url_name" : blog})
    except KeyError:
        return HttpResponseNotFound("<h1>Blog not found </h1>")









# def blog_posts(request,blog):
#     try:
#         res = url_name[blog]
#     # except Exception:
#     except KeyError:
#         return HttpResponseNotFound(request,"blogs/posts.html")
#     else:
#         return HttpResponse(res)