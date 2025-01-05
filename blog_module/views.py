from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import BlogModel, CommentModel


class BlogView(View):
    def get(self, request):
        blogs = BlogModel.objects.all()
        return render(request, 'blogs.html', {
            'blogs': blogs
        })


class BlogDetailView(View):
    def get(self, request, id):
        blog = BlogModel.objects.filter(id=id).first()
        comments = CommentModel.objects.filter(blog=blog, is_published=True, parent=None)
        comments_reply = []
        for comment in CommentModel.objects.filter(blog=blog, is_published=True):
            if comment.parent is not None:
                comments_reply.append(comment)

        return render(request, 'blog_detail.html', {
            'blog': blog,
            'comments': comments,
            'comments_reply': comments_reply,
            'count': len(comments)
        })

    def post(self, request: HttpRequest, id):
        blog = BlogModel.objects.filter(id=id).first()
        text = request.POST.get('text')
        parent = request.POST.get('hidden')
        if parent != '':
            new_comment = CommentModel.objects.create(user=request.user, blog=blog, text=text, parent_id=int(parent))
        else:
            new_comment = CommentModel.objects.create(user=request.user, blog=blog, text=text, parent=None)

        return redirect(reverse('blog_details', args=[blog.id]))
