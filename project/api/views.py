from rest_framework.views import APIView
from rest_framework.response import Response
from requests import get as get_page
from rest_framework import status

from .models import Comment, Post


class CommentsView(APIView):
    def get(self, request):
        comments = get_page("https://jsonplaceholder.typicode.com/comments").json()
        count_comments = round(len(comments) * 0.75)

        created = False
        for n, comment in enumerate(comments):
            n += 1

            if n < count_comments:
                comment_id = comment.get("id")
                post_id = comment.get("postId")

                if not Post.objects.filter(id=post_id).exists():
                    Post.objects.create(id=post_id)

                if not Comment.objects.filter(id=comment_id).exists():
                    created = True
                    Comment.objects.create(
                        id=comment_id,
                        name=comment["name"],
                        email=comment["email"],
                        body=comment["body"],
                        postId_id=post_id
                    )

        return Response(comments[:count_comments], status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
