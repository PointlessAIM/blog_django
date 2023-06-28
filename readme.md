# Important steps to develop a Django project

## Create a virtual environment
    make sure to have venv downloaded.
    in the command prompt type 'python -m venv <name of your environment>'
    after this you can install all the modules required for your project

## create a requirements.txt file
    you need to specify all the packages that are needed in your project and the corresponding version
    if you are not sure of the version you need, google it typing '<module> pypi'. 
    When you're done go to the command propmt and type 'pip install -r requirements.txt' and
    all the packages you need will be installed

## .gitignore file
    you can use this file for telling git to ignore files with sensitive information or files you don't
    want to share, such as .env, chache (...) if you are not sure of what those files may be, google
    'gitignore <language>'

## Django
    with django you can perform several administrative tasks that you can take advantage of, some are
    key commands for your project to take shape. 
    * Go to the command prompt and type 'django-admin startproject <project name> .', this will create a 
      folder with the basic composition of files needed in a django project.
    * every time you need a new app type in your command prompt 'django-admin startapp <app name>'.
    * once you've created an app, make sure to go to 'settings.py', then installed apps and inside type
      the name of your new app. Django won't recognize it otherwise.
    * each time you make a change in the 'models.py' file, it's recommended to run the command
      'python manage.py makemigrations' followed by 'python manage.py migrate'.
### Models
    Django has its own ORM and each time you start an app the 'models.py' file will be generated inside.
    each table will be represented as a class that inherits from 'models.Model', example: 
    'class User(models.Model):' (...), inside the class you will declare the attributes and configure the 
    specifics. 
    As the DB tables are represented with classes, you can create objects to populate with data and save
    the changes so the data can be persistent. If you want to experiment with it use the Django shell.

### Shell
    As stated earlier, you can perform different administrative tasks with django, one of its features is
    the interactive shell and one of its use cases may be testing your models and how data will be handled.
    Here some examples:
    ** first go to he command prompt and type 'python manage.py shell', this will activate django's shell

    *** inside the shell

    >>> >>> from <app name>.models import User, Website, <any other class you'll use>
    >>> u = User(first_name='John', last_name='Doe', <any other attribute>)
    >>> u.save()    #if you don't save, django won't recognize your inputs
    >>> type(u)
    <class 'users.models.User'>
    >>> u
    <User: User object (1)>
    >>> import datetime     
    >>> date = datetime.date(2023,4,27)
    >>> w = Website(name = 'website', url = 'https://website.com', release_date = date, rating = 10, status = 'N', owner = u)
    >>> w.save()
    >>> w
    <Website: Website object (1)>
    >>> u.first_name
    'John'
    >>> w.name
    'website'
    >>> w.release_date
    datetime.date(2023, 4, 27)
    >>> w.url
    'https://website.com'
    >>> w.status 
    'N'
    >>> w.get_status_display()
    'Not Reviewed'
    
    *** check the documentation for more information on how to use the shell and the ORM

### Querysets/Lookups

    previously you saw how to store data through django shell. Here's another case.

    *****

    from posts.models import Blog, Entry
    >>> import datetime
    >>> Blog.objects.all()
    <QuerySet [<Blog: buenas>]>
    >>> b=Blog.objects.first()
    >>> Entry.objects.all()
    <QuerySet [<Entry: a man of culture, i see>]>
    >>> entry = Entry.objects.first()
    >>> entry
    <Entry: a man of culture, i see>
    >>> b
    <Blog: buenas>
    >>> b2 = Blog(name="another blog", tagline="blog tag") 
    >>> b2.save()
    >>> b2
    <Blog: another blog>
    >>> entry.blog
    <Blog: buenas>
    >>> entry.blog=b2
    >>> entry.save()
    >>> entry.blog    
    <Blog: another blog>
    >>> from posts.models import Author
    >>> a = Author(name="John", email="mail@mail.com")
    >>> a.save()
    >>> entry.authors  #if typed like this, django will show you the space in memory of the object     
    >>> entry.authors.add(a)
    >>> entry.save()
    >>> entry.authors.first() # if typed like this, it will show what's stored in the object
    <Author: John>
    >>> a2=Author.objects.create(name="Doe", email="doe@mail.com")
    >>> a2
    <Author: Doe>
    >>> a3=Author.objects.create(name="Foo", email="foo@mail.com") 
    >>> entry.authors.add(a2,a3)
    >>> entry.save()
    >>> entry.authors.all()
    <QuerySet [<Author: John>, <Author: Doe>, <Author: Foo>]>
    >>> Blog.objects.filter(name="new name") #you can filter through objects like this. more examples below.
    <QuerySet []>
    >>> Entry.objects.filter(pub_date__year=2023) #you can specify how you want to filter adding '__' + <filter>
    <QuerySet [<Entry: a man of culture, i see>]>
    >>> Entry.objects.filter(rating__gte=5)       
    <QuerySet [<Entry: a man of culture, i see>]>
    >>> entry.rating
    10
    >>> Entry.objects.filter(headline__startswith="a").exclude(pub_date__year=2020).filter(rating__gte=7) #stack filters
    <QuerySet [<Entry: a man of culture, i see>]>
    >>> Entry.objects.filter(headline__startswith="a").exclude(pub_date__year=2020).filter(rating__lte=7) 
    <QuerySet []>
    >>> Entry.objects.get(id=1) #use get if you know exactly what you're looking for
    <Entry: a man of culture, i see>
    >>> Entry.objects.all()[:10] you can apply slicing for limiting the amount of data you want to receive
    >>> Entry.objects.filter(headline__exact="a man of culture, i see") #case sensitive lookup
    <QuerySet [<Entry: a man of culture, i see>]>
    >>> Entry.objects.filter(headline__iexact="a man of cultuRe, I seE") 
    <QuerySet [<Entry: a man of culture, i see>]>
    >>> Blog.objects.filter(entry__authors__name__icontains="o") #3 authors with 'o' in their name
    <QuerySet [<Blog: another blog>, <Blog: another blog>, <Blog: another blog>]> #created the same blog
    
    queryset = Entry.objects.all() #efficient way to query from DB
    >>> print([e.headline for e in queryset])
    ['a man of culture, i see'] #django caches data retreived if you want to query again

#### Q Lookups
    >>> from django.db.models import Q
    >>> Entry.objects.filter(Q(pub_date__year=2020)|Q(pub_date__year=2023)) #OR
    <QuerySet [<Entry: a man of culture, i see>]>
    >>> Entry.objects.filter(Q(pub_date__year=2020)|Q(pub_date__year=2023), Q(rating__gte=7)) #OR, AND 
    <QuerySet [<Entry: a man of culture, i see>]>

#### Related objects
    for making many-to-many-field queries easier to read, you can add a related name to the field
        authors = models.ManyToManyField(Author, related_name="entries")
    after that you can go to the shell and query what you need

    ** before 

    from posts.models import Author
    >>> a = Author.objects.get(name="Foo")
    >>> a.entry_set.all()
    <QuerySet [<Entry: a man of culture, i see>]>    

    ** after

    from posts.models import Author
    >>> a = Author.objects.get(name="Foo")
    >>> a.entries.all()
    <QuerySet [<Entry: a man of culture, i see>]>









