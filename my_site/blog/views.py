from django.shortcuts import render, get_object_or_404
from .models import Post

all_posts = [
#     {
#         "slug": "hike-in-the-mountains",
#         "image": "mountains.jpg",
#         "author": "Richard",
#         "date": date(2023, 2, 14),
#         "title": "Mountain Hiking",
#         "excerpt" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt",
#         "content" : """
#             Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
#             tempor incididunt ut labore et dolore magna aliqua. At in tellus integer 
#             feugiat scelerisque varius morbi enim. Nec feugiat in fermentum posuere. 
#             Sem viverra aliquet eget sit amet. Vulputate enim nulla aliquet porttitor 
#             lacus luctus. Quis vel eros donec ac odio. Sit amet mattis vulputate enim 
#             nulla aliquet porttitor. Natoque penatibus et magnis dis parturient montes 
#             nascetur. Velit laoreet id donec ultrices tincidunt. Sit amet commodo nulla 
#             facilisi nullam vehicula ipsum a arcu. Quam viverra orci sagittis eu volutpat 
#             odio facilisis mauris. Habitant morbi tristique senectus et netus. Faucibus pulvinar 
#             elementum integer enim neque. Fringilla urna porttitor rhoncus dolor purus non enim 
#             praesent elementum.

#             Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
#             tempor incididunt ut labore et dolore magna aliqua. At in tellus integer 
#             feugiat scelerisque varius morbi enim. Nec feugiat in fermentum posuere. 
#             Sem viverra aliquet eget sit amet. Vulputate enim nulla aliquet porttitor 
#             lacus luctus. Quis vel eros donec ac odio. Sit amet mattis vulputate enim 
#             nulla aliquet porttitor. Natoque penatibus et magnis dis parturient montes 
#             nascetur. Velit laoreet id donec ultrices tincidunt. Sit amet commodo nulla 
#             facilisi nullam vehicula ipsum a arcu. Quam viverra orci sagittis eu volutpat 
#             odio facilisis mauris. Habitant morbi tristique senectus et netus. Faucibus pulvinar 
#             elementum integer enim neque. Fringilla urna porttitor rhoncus dolor purus non enim 
#             praesent elementum.

#             Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
#             tempor incididunt ut labore et dolore magna aliqua. At in tellus integer 
#             feugiat scelerisque varius morbi enim. Nec feugiat in fermentum posuere. 
#             Sem viverra aliquet eget sit amet. Vulputate enim nulla aliquet porttitor 
#             lacus luctus. Quis vel eros donec ac odio. Sit amet mattis vulputate enim 
#             nulla aliquet porttitor. Natoque penatibus et magnis dis parturient montes 
#             nascetur. Velit laoreet id donec ultrices tincidunt. Sit amet commodo nulla 
#             facilisi nullam vehicula ipsum a arcu. Quam viverra orci sagittis eu volutpat 
#             odio facilisis mauris. Habitant morbi tristique senectus et netus. Faucibus pulvinar 
#             elementum integer enim neque. Fringilla urna porttitor rhoncus dolor purus non enim 
#             praesent elementum.
#         """
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "coding.jpg",
#         "author": "Richard",
#         "date": date(2022, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "woods.jpg",
#         "author": "Richard",
#         "date": date(2020, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     }
]

def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })

def post_detail(request, slug):
    # identified_post = Post.object.get(slug=slug)
    identified_post = get_object_or_404(Post, slug=slug)
    
    return render(request, 'blog/post-detail.html', {
        'post': identified_post,
        'post_tags': identified_post.caption.all()
    })