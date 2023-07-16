from NewsPaperApp.models import *  

user1 = User.objects.create(username='ArtPV', first_name='Artyom')
 
user2 = User.objects.create(username='Dima', first_name='Dima')

user3= User.objects.create(username='PassBy', first_name='Walker')

перезагрузка 

>user1=User.objects.get(pk=1)
>
>Author.objects.create(author_name=user1)


>user2= User.objects.get(pk=2)
>
>user2= User.objects.get(pk=3)
>
>author2=Author.objects.create(author_name=user2) 

> category1 = Category.objects.create(name='History')
> 
> category2 = Category.objects.create(name='Mathematics') 
> 
> category3 = Category.objects.create(name='IT')          
>
> category4 = Category.objects.create(name='Phisics')

>Post.objects.create(author=Author.objects.get(author_name=User.objects.get(username='ArtPV')), post_type='PT', title='title1', text='big text')

>
>> Post.objects.create(author=Author.objects.get(author_name=User.objects.get(username='Dima')), post_type='PT', title='Всё о клей-пене для кладки газобетона', text='То что я расскажу сегодня будет полезно, познавательно и интересно прежде всего для тех, кто только собирается строиться и планирует построить в ближайшем будущем собственный дом своими руками по интересным новым и правильным технологиям. Сегодня речь пойдёт о строительстве стен гаража, а точнее о кладке газобетона на клей-пену в целом. Эта тема достаточно противоречивая. Кто-то уже к этому привык, как я и бригада с которой я работаю. Одни люди активно используют эту технологию, а другие не верят, боятся, думают что это всё развалится и т.д.')
>
>> Post.objects.create(author=Author.objects.get(author_name=User.objects.get(username='ArtPV')), post_type='NW', title='В лесах под Петербургом начали зажигаться светлячки', text='Таинственные огоньки, которые можно заметить в лесах Санкт-Петербурга и Ленинградской области, излучают самки светлячков')  


> category1 = Category.objects.create(name='Nature')
>
> Category.objects.create(name='Building') 


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

> category_history=Category.objects.get(pk=1)
>
> category_mathematics=Category.objects.get(pk=2)
>
> category_IT=Category.objects.get(pk=3)          
>
> category_Phisics=Category.objects.get(pk=4)
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



