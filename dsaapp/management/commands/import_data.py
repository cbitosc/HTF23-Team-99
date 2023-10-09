import json
import random
from django.core.management.base import BaseCommand
from dsaapp.models import Content, Category, Question  # Adjust import based on your actual app and model names

class Command(BaseCommand):
    help = 'Import data from JSON into Django models'

    def handle(self, *args, **options):
        with open('dsa_data.json', 'r') as file:
            json_data = json.load(file)

        self.import_data(json_data)
        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))

    def import_data(self, json_data):
        for content_data in json_data['content']:
            content = Content.objects.create(
                contentPath=content_data['contentPath'],
                contentHeading=content_data['contentHeading'],
                contentSubHeading=content_data['contentSubHeading'],
                contentUserNotes=content_data['contentUserNotes'],
                contentTotalQuestions=content_data['contentTotalQuestions'],
                contentCompletedQuestions=content_data['contentCompletedQuestions'],
            )

            for category_data in content_data['categoryList']:
                category = Category.objects.create(
                    content=content,
                    categoryId=category_data['categoryId'],
                    categoryName=category_data['categoryName'],
                    categoryTotalQuestions=category_data['categoryTotalQuestions'],
                    categoryCompletedQuestions=category_data['categoryCompletedQuestions'],
                )

                for question_data in category_data['questionList']:
                    Question.objects.create(
                        category=category,
                        questionHeading=question_data['questionHeading'],
                        questionLink=question_data['questionLink'],
                        gfgLink=question_data['gfgLink'],
                        leetCodeLink=question_data.get('leetCodeLink'),
                        youTubeLink=question_data['youTubeLink'],
                        isDone=question_data['isDone'],
                        isBookmarked=question_data['isBookmarked'],
                        userNotes=question_data['userNotes'],
                        questionIndex=question_data['questionIndex'],
                        questionId=question_data['questionId'],
                    )
