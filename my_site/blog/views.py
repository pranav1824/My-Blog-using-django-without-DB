from datetime import date

from django.shortcuts import render

all_posts = [
    {
        "slug": "webdev",
        "image" : "webdev.jpeg",
        "author" : "Pranav",
        "date" : date(2024, 9, 17),
        "title" : "Web Dev",
        "excerpt" : "Web development is the art of creating and maintaining websites and web applications",
        "content" : """
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

                
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

                
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio."""
    },
    {
        "slug": "code",
        "image" : "coding.png",
        "author" : "Pranav",
        "date" : date(2024, 9, 18),
        "title" : "code",
        "excerpt" : "Code in django using python",
        "content" : """
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

                
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

                
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio."""
    },
    {
        "slug": "sql",
        "image" : "pranav.jpeg",
        "author" : "Pranav",
        "date" : date(2024, 9, 19),
        "title" : "sql",
        "excerpt" : "write queries in sql and manage database",
        "content" : """
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

                
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

                
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
                aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
                velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio."""
    }
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts= sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts" : latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })




