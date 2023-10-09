# from django.db import models

# class Question(models.Model):
#     questionHeading = models.CharField(max_length=255)
#     questionLink = models.CharField(max_length=255, blank=True)
#     gfgLink = models.CharField(max_length=255, blank=True)
#     leetCodeLink = models.CharField(max_length=255, blank=True)
#     youTubeLink = models.CharField(max_length=255, blank=True)
#     isDone = models.BooleanField(default=False)
#     isBookmarked = models.BooleanField(default=False)
#     userNotes = models.TextField(blank=True)
#     questionIndex = models.IntegerField()
#     questionId = models.CharField(max_length=255)

# class Category(models.Model):
#     categoryId = models.IntegerField()
#     categoryName = models.CharField(max_length=255)
#     categoryTotalQuestions = models.IntegerField()
#     categoryCompletedQuestions = models.IntegerField()
#     questionList = models.ManyToManyField(Question)

# class Content(models.Model):
#     contentPath = models.CharField(max_length=255)
#     contentHeading = models.CharField(max_length=255)
#     contentSubHeading = models.CharField(max_length=255, blank=True)
#     contentUserNotes = models.TextField(blank=True)
#     contentTotalQuestions = models.IntegerField()
#     contentCompletedQuestions = models.IntegerField()
#     categoryList = models.ManyToManyField(Category)


from django.db import models

class Content(models.Model):
    contentPath = models.CharField(max_length=255)
    contentHeading = models.CharField(max_length=255)
    contentSubHeading = models.CharField(max_length=255, blank=True)
    contentUserNotes = models.TextField(blank=True)
    contentTotalQuestions = models.IntegerField()
    contentCompletedQuestions = models.IntegerField()

    def __str__(self):
        return self.contentHeading


class Category(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='categories')
    categoryId = models.IntegerField()
    categoryName = models.CharField(max_length=255)
    categoryTotalQuestions = models.IntegerField()
    categoryCompletedQuestions = models.IntegerField()

    def __str__(self):
        return self.categoryName


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    questionHeading = models.CharField(max_length=255)
    questionLink = models.CharField(max_length=255, blank=True)
    gfgLink = models.CharField(max_length=255, blank=True)
    leetCodeLink = models.CharField(max_length=255, blank=True)
    youTubeLink = models.CharField(max_length=255, blank=True)
    isDone = models.BooleanField(default=False)
    isBookmarked = models.BooleanField(default=False)
    userNotes = models.TextField(blank=True)
    questionIndex = models.IntegerField()
    questionId = models.CharField(max_length=255)

    def __str__(self):
        return self.questionHeading
