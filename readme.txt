**** Info ****

1. This is a html generator system designed using django
2. A custom form was made using the charfield form from "CKEditor"
3. The app ('HTML_generator') can be integrated to any django project
4. Frontend is created using HTML, CSS and bootstrap


**** Project workflow ****

1. Created django project "Text_html"
2. Created django app HTML_generator"
3. Added the app in project settings
4. Created "urls.py" in the app
5. Included the app urls in project urls
6. Created the custom model "Content"
7. Added the model in admin.py
8. Created a custom form using CKEditor's RichTextField
9. Created the frontend
10. Used javascript to fetch data from the form and returned the HTML text from it.


**** Ideas ****

1. The admin.py should contain each custom models for it to show in django admin panel
2. "admin.site.register(Content)" here 'Content' is the custom model