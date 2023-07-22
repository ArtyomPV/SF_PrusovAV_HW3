### Создать двух пользователей (с помощью метода User.objects.create_user).
```
from NewsPaperApp.models import *  
user1 = User.objects.create(username='ArtPV', first_name='Artyom')
user2 = User.objects.create(username='Dima', first_name='Dima')
user3= User.objects.create(username='PassBy', first_name='Walker')
```
### Создать два объекта модели Author, связанные с пользователями.
```
Author.objects.create(author_name=user1)
Author.objects.create(author_name=user2) 
```

### Добавить 4 категории в модель Category.
```
 category1 = Category.objects.create(name='History')
 category2 = Category.objects.create(name='Mathematics') 
 category3 = Category.objects.create(name='IT')          
 category4 = Category.objects.create(name='Phisics')
```
### Добавить 2 статьи и 1 новость.
```
Post.objects.create(author=Author.objects.get(author_name=User.objects.get(username='Dima')), post_type='PT', title='Всё о клей-пене для кладки газобетона', text='То что я расскажу сегодня будет полезно, познавательно и интересно прежде всего для тех, кто только собирается строиться и планирует построить в ближайшем будущем собственный дом своими руками по интересным новым и правильным технологиям. Сегодня речь пойдёт о строительстве стен гаража, а точнее о кладке газобетона на клей-пену в целом. Эта тема достаточно противоречивая. Кто-то уже к этому привык, как я и бригада с которой я работаю. Одни люди активно используют эту технологию, а другие не верят, боятся, думают что это всё развалится и т.д.')
Post.objects.create(author=Author.objects.get(author_name=User.objects.get(username='ArtPV')), post_type='PT', title='Крупнейший на планете айсберг А23а возобновил активный дрейф вдоль берегов Антарктиды', text='Специалисты наблюдают за ходом движения крупнейшего на планете айсберга А23а», — говорится в сообщении. Уточняется, что айсберг начал активный дрейф со скоростью более 150 км в месяц.«В настоящее время айсберг движется в море Уэдделла вдоль берегов Антарктиды», — заявили в институте. Ранее климатолог Алексей Кокорин рассказал, что, по мнению учёных, в перспективе некоторые территории станут непригодны для сельского хозяйства из-за засухи. Это может привести к климатической миграции.')
Post.objects.create(author=Author.objects.get(author_name=User.objects.get(username='ArtPV')), post_type='NW', title='В лесах под Петербургом начали зажигаться светлячки', text='Таинственные огоньки, которые можно заметить в лесах Санкт-Петербурга и Ленинградской области, излучают самки светлячков')  
```
### Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
```
post1=Post.objects.get(pk=1)
post2=Post.objects.get(pk=2) 
post3=Post.objects.get(pk=3) 

Category.objects.create(name='Nature')
Category.objects.create(name='Building')
Category.objects.create(name='Phisics')
Category.objects.create(name='Science')

category_nature=Category.objects.get(pk=1)
category_building=Category.objects.get(pk=2)
category_phisics=Category.objects.get(pk=3)          
category_science=Category.objects.get(pk=4)

post1.category.add(category_nature, category_phisics)
post2.category.add(category_building, category_phisics)
post3.category.add(category_science, category_phisics)
```
### Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
```
Comment.objects.create(comment=Post.objects.get(pk=1),text_comment='comment1', author_comment=User.objects.get(username='PassBy'))
Comment.objects.create(comment=Post.objects.get(pk=1),text_comment='comment1', author_comment=User.objects.get(username='Dima'))
Comment.objects.create(comment=Post.objects.get(pk=2),text_comment='comment1', author_comment=User.objects.get(username='ArtPV'))
Comment.objects.create(comment=Post.objects.get(pk=3),text_comment='comment1', author_comment=User.objects.get(username='PassBy'))
```
### Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
```
Post.objects.get(pk=1).like()
post1.like()
post2.like()
post2.like()
post3.dislike()

Comment.objects.get(pk=1).like()
Comment.objects.get(pk=1).like()
Comment.objects.get(pk=2).like() 
Comment.objects.get(pk=3).dislike() 
Comment.objects.get(pk=4).like()
```
### Обновить рейтинги пользователей.
```
Author.objects.get(author_name=User.objects.get(username='ArtPV')).update_rating()
Author.objects.get(author_name=User.objects.get(username='Dima')).update_rating()
Author.objects.get(author_name=User.objects.get(username='PassBy')).update_rating()
```
### Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
```
best=Author.objects.all().order_by('-rating').values('author_name', 'rating')[0]
print(best)
```
### Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.

### Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.


перезагрузка 

>user1=User.objects.get(pk=1)
>
>Author.objects.create(author_name=user1)


>



>Post.objects.create(author=Author.objects.get(author_name=User.objects.get(username='ArtPV')), post_type='PT', title='Крупнейший на планете айсберг А23а возобновил активный дрейф вдоль берегов Антарктиды', text='Специалисты наблюдают за ходом движения крупнейшего на планете айсберга А23а», — говорится в сообщении. Уточняется, что айсберг начал активный дрейф со скоростью более 150 км в месяц.«В настоящее время айсберг движется в море Уэдделла вдоль берегов Антарктиды», — заявили в институте. Ранее климатолог Алексей Кокорин рассказал, что, по мнению учёных, в перспективе некоторые территории станут непригодны для сельского хозяйства из-за засухи. Это может привести к климатической миграции.')

>
>> Post.objects.create(author=Author.objects.get(author_name=User.objects.get(username='Dima')), post_type='PT', title='Всё о клей-пене для кладки газобетона', text='То что я расскажу сегодня будет полезно, познавательно и интересно прежде всего для тех, кто только собирается строиться и планирует построить в ближайшем будущем собственный дом своими руками по интересным новым и правильным технологиям. Сегодня речь пойдёт о строительстве стен гаража, а точнее о кладке газобетона на клей-пену в целом. Эта тема достаточно противоречивая. Кто-то уже к этому привык, как я и бригада с которой я работаю. Одни люди активно используют эту технологию, а другие не верят, боятся, думают что это всё развалится и т.д.')
>
>> Post.objects.create(author=Author.objects.get(author_name=User.objects.get(username='ArtPV')), post_type='NW', title='В лесах под Петербургом начали зажигаться светлячки', text='Таинственные огоньки, которые можно заметить в лесах Санкт-Петербурга и Ленинградской области, излучают самки светлячков')  


> 
>
> 


> post5=Post.objects.get(pk=5)
> 
> category1 = Category.objects.get(pk=5)
> 
> post5.category.add(category1)

> post2=Post.objects.get(pk=2) 
>
> post3=Post.objects.get(pk=3) 
>
> post4=Post.objects.get(pk=4) 


>
> category_Nature=Category.objects.get(pk=5)  
> category_Building=Category.objects.get(pk=6) 

post4.category.add(category_Building, category_Phisics)

> Comment.objects.create(comment=Post.objects.get(pk=2),text_comment='comment1', author_comment=User.objects.get(username='PassBy'))
>
> Comment: Comment object (1)
>
> Comment.objects.create(comment=Post.objects.get(pk=4),text_comment='comment2', author_comment=User.objects.get(username='Dima'))    
>
> Comment: Comment object (2)
>
> Comment.objects.create(comment=Post.objects.get(pk=5),text_comment='comment3', author_comment=User.objects.get(username='PassBy'))
> 
> Comment: Comment object (3)

>Post.objects.get(pk=1).like()  
> 
> Post.objects.get(pk=1).like() 
> 
> Post.objects.get(pk=2).dislike() 
> 
> Post.objects.get(pk=3).like()
> 
> Post.objects.get(pk=5).like()
> 
> Comment.objects.get(pk=1).like()
> 
> Comment.objects.get(pk=1).like()
> 
> Comment.objects.get(pk=2).like() 
> 
> Comment.objects.get(pk=3).dislike() 


>Author.objects.get(author_name=User.objects.get(username='ArtPV')).update_rating()
>
> a=Author.objects.get(author_name=User.objects.get(username='ArtPV'))              
>
> a.rating


> best=Author.objects.all().order_by('-rating').values('author_name', 'rating')[0] 
> 
> print(best)

