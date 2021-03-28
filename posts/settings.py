LETTERS_PER_STR = 15
POSTS_PER_PAGE = 12

# Group model settings
GROUP_TITLE_VERBOUSE_NAME = 'Название группы'
GROUP_TITLE_MAX_LEN = 200
GROUP_TITLE_HELP_TEXT = 'Напишите название группы'

GROUP_SLUG_VERBOUSE_NAME = 'Ключ для составления адреса'
GROUP_SLUG_MAX_LEN = 100
GROUP_SLUG_HELP_TEXT = 'Укажите адрес сообщества в интернете'

GROUP_DESCRIPTION_VERBOUSE_NAME = 'Информация о группе'
GROUP_DESCRIPTION_HELP_TEXT = 'Напишите что-нибудь о группе'

# Post model settings
POST_TITLE_VERBOUSE_NAME = 'Название рецепта'
POST_TITLE_HELP_TEXT = 'Напишите здесь название рецепта'
POST_TITLE_MAX_LEN = 200

POST_TEXT_VERBOUSE_NAME = 'Рецепт'
POST_TEXT_HELP_TEXT = 'Напишите здесь текст рецепта'

POST_PUB_DATE_VERBOUSE_NAME = 'Дата публикации'

POST_RELATED_NAME = 'posts'

POST_AUTHOR_VERBOUSE_NAME = 'Автор рецепта'
POST_AUTHOR_HELP_TEXT = 'Это пользователь, опубликовавший заметку'

POST_GROUP_VERBOUSE_NAME = 'Группа'
POST_GROUP_HELP_TEXT = 'Можете выбрать группу, к которой будет принадлежать пост'

POST_IMAGE_UPLOAD_TO = 'posts/'
POST_IMAGE_VERBOUSE_NAME = 'Изображение'
POST_IMAGE_HELP_TEXT = 'Можете выбрать картинку к рецепту'

# Comment model settings
COMMENT_RELATED_NAME = 'comments'

COMMENT_POST_VERBOUSE_NAME = 'Рецепт'
COMMENT_POST_HELP_TEXT = 'Рецепт, к которому оставлен комментарий'

COMMENT_AUTHOR_VERBOUSE_NAME = 'Автор'
COMMENT_AUTHOR_HELP_TEXT = 'Автор комментария'

COMMENT_TEXT_VERBOUSE_NAME = 'Текст'
COMMENT_TEXT_HELP_TEXT = 'Текст комментария'

COMMENT_CREATED_VERBOUSE_NAME = 'Дата комментария'

# Follow model settings
FOLLOW_USER_RELATED_NAME = 'follower'
FOLLOW_USER_VERBOUSE_NAME = 'Подписчик'
FOLLOW_USER_HELP_TEXT = 'Подписчик'

FOLLOW_AUTHOR_RELATED_NAME = 'following'
FOLLOW_AUTHOR_VERBOUSE_NAME = 'Автор'
FOLLOW_AUTHOR_HELP_TEXT = 'Автор'

# Form settings
POST_FORM_FIELDS = ('text', 'group', 'image')
POST_COMMENT_FIELDS = ('text',)
