from django.contrib import admin
from .models import * #Member, ProblemKeep, TryParent, TryAction, Comment, Review, OpinionForTry, Meeting

# Register your models here.
admin.site.register(Member)
admin.site.register(ProblemKeep)
admin.site.register(TryParent)
admin.site.register(TryAction)
admin.site.register(Comment)
admin.site.register(Review)
admin.site.register(OpinionForTry)
admin.site.register(Meeting)
