### MiniStack 项目接口文档

注意："type" 只能取 "post" 或 "note" 值(字符串)

提示：关于 tag 的实现，后端可以对前端发来的每一个<tag_array>做以下处理：1.将其当做字符串存储在post或note的tag_array属性里；2.将其拆解为一个个的tag存储在tag总表里（注意重复的不加入即可）；举例：查找含有某一个tag的所有post时，查找tag是否在某个post的tag_array字符串里即可

注意："tags_array"的格式为[\<tag\>]，比如在14中，前端请求为：

```
{
  "title": "My Birthday Is Coming Soon!",
  "content": "我上早八。",
  "tags": ["birthday", "我上早八"]
}
```



#### 登录注册

登录接口地址:/auth/login

注册:/auth/register 





#### 1. 展示所有人的 Post 和 Note

- **接口地址**: `/home`

- **请求方法**: `GET`

- 后端返回

  :

  ```
  [
    {
    	"type":"<post_or_note>"
      "id": "<post_or_note_id>",
      "username": "<author_username>",
      "title": "<post_title_or_empty>",
      "content_preview": "<first_two_lines_of_content>",
      "tags": "<tags_array>",
      "date": "<creation_date>"
      "likes": "<like_count>",
      "views": "<view_count>"
    }
  ]
  ```



#### 2. 新的 Post 阅读

- **接口地址**: `/postid/{postid}`

- **请求方法**: `POST`

- 前端请求

  :

  ```
  {
    "user_name": "<current_reader_name>"
  }
  ```

- 后端返回

  :

  ```
  {
    "post_id": "<post_id>",
    "username": "<author_username>",
    "title": "<post_title>",
    "content": "<full_content>",
    "tags": "<tags_array>",
    "date": "<creation_date>"
    "likes": "<like_count>",
    "views": "<view_count>"
  }
  ```

#### 3. 新的 Post 点赞

- **接口地址**: `/postid/{postid}/newlike`

- **请求方法**: `POST`

- 前端请求

  :

  ```
  {
    "user_name": "<current_reader_name>"
  }
  ```

- 后端返回

  :

  ```
  {
    "likes": "<updated_like_count>"
  }
  ```

#### 4. 新的 Note 阅读

- **接口地址**: `/noteid/{noteid}`

- **请求方法**: `POST`

- 前端请求

  :

  ```
  {
    "user_name": "<current_reader_name>"
  }
  ```

- 后端返回

  :

  ```
  {
    "note_id": "<note_id>",
    "username": "<author_username>",
    "content": "<full_content>",
    "tags": "<tags_array>",
    "date": "<creation_date>"
    "likes": "<like_count>",
    "views": "<view_count>"
  }
  ```

#### 5. 新的 Note 点赞

- **接口地址**: `/noteid/{noteid}/newlike`

- **请求方法**: `POST`

- 前端请求

  :

  ```
  {
    "user_name": "<current_reader_name>"
  }
  ```

- 后端返回

  :

  ```
  {
    "likes": "<updated_like_count>"
  }
  ```

#### 6. 获得用户的所有动态信息

- **接口地址**: `/profile/{username}`

- **请求方法**: `GET`

- 后端返回

  :注意recent_posts和recent_notes分别只返回最新的两条记录。

  ```
  {
    "username": username;
    "avatarurl": url;
    "post_count": "<number_of_posts>",
    "note_count": "<number_of_notes>",
    "read_count": "<number_of_reads>",
    "like_count": "<number_of_likes>",
    "following_count": "<number_of_following>",
    "fan_count": "<number_of_fans>",
    "recent_posts": [
      {
        "post_id": "<post_id>",
        "title": "<post_title>"
      }
    ],
    "recent_notes": [
      {
        "note_id": "<note_id>",
        "content_preview": "<first_line_of_note>"
      }
    ]
  }
  ```

#### 7. 获得用户的具体发布过的 Post 信息

- **接口地址**: `/profile/{username}/detailedpost`

- **请求方法**: `GET`

- 后端返回

  :

  ```
  [
    {
      "post_id": "<post_id>",
      "title": "<post_title>",
      "date": "<creation_date>"
    }
  ]
  ```

#### 8. 获得用户的具体发布过的 Note 信息

- **接口地址**: `/profile/{username}/detailednote`

- **请求方法**: `GET`

- 后端返回

  :

  ```
  [
    {
      "note_id": "<note_id>",
      "content_preview": "<first_line_of_note>",
      "date": "<creation_date>"
    }
  ]
  ```

#### 9. 获得用户的具体点赞过的 Post 和 Note 信息

- **接口地址**: `/profile/{username}/detailedlikes`

- **请求方法**: `GET`

- 后端返回

  :

  ```
  {
    "posts": [
      {
        "post_id": "<post_id>",
        "title": "<post_title>",
        "date": "<creation_date>"
      }
    ],
    "notes": [
      {
        "note_id": "<note_id>",
        "content_preview": "<first_line_of_note>",
        "date": "<creation_date>"
      }
    ]
  }
  ```

#### 10. 获得用户的具体阅读过的 Post 和 Note 信息

- **接口地址**: `/profile/{username}/detailedreads`

- **请求方法**: `GET`

- 后端返回

  :

  ```
  {
    "posts": [
      {
        "post_id": "<post_id>",
        "title": "<post_title>",
        "date": "<creation_date>"
      }
    ],
    "notes": [
      {
        "note_id": "<note_id>",
        "content_preview": "<first_line_of_note>",
        "date": "<creation_date>"
      }
    ]
  }
  ```

#### 11. 获得用户的关注用户信息

- **接口地址**: `/profile/{username}/detailedfollowing`

- **请求方法**: `GET`

- 后端返回

  :

  ```
  [
    {
      "username": "<followed_user_username>"
    }
  ]
  ```

#### 12. 获得用户的粉丝信息

- **接口地址**: `/profile/{username}/detailedfan`

- **请求方法**: `GET`

- 后端返回

  :

  ```
  [
    {
      "username": "<fan_user_username>"
    }
  ]
  ```

#### 13. 展示关注的人的帖子和笔记

- **接口地址**: `/inbox`

- **请求方法**: `GET`

- 前端请求

  :

  ```
  {
    "user_name": "<user_name>"
  }
  ```

- 响应

  :

  ```
  [
    {
    	"type":"<post_or_note>"
      "id": "<post_or_note_id>",
      "username": "<author_username>",
      "title": "<post_title_or_empty>",
      "content_preview": "<first_two_lines_of_content>",
      "tags": "<tags_array>",
      "date": "<creation_date>"
      "likes": "<like_count>",
      "views": "<view_count>"
    }
  ]
  ```

#### 14.发布新的Post

- **Endpoint**: `/add-post

- **Method**: `POST`

- Request

  :

  ```
  {
    "title": "<post_title>",
    "content": "<post_content>",
    "tags": "<tags_array>"
  }
  ```

- Response

  :

  ```
  {
    "post_id": "<new_post_id>",
    "date": "<creation_date>"
  }
  ```

注意这里后端要建立 tag 的总表，方便后续筛选功能实现，tag 中包含 post 和 note，用来筛选 post 和 note

#### 15. 发布新的Note

- **Endpoint**: `/add-note

- **Method**: `POST`

- Request

  :

  ```
  {
    "content": "<note_content>",
    "tags": "<tags_array>"
  }
  ```

- Response

  :

  ```
  {
    "note_id": "<new_note_id>",
    "date": "<creation_date>"
  }
  ```

和上面的 tag 公用一个 tag 表

#### 16. 根据Tags筛选帖子和笔记

- **Endpoint**: `/filter`

- **Method**: `POST`

- Request

  :

  ```
  {
    "tags": "<tags_array>"
  }
  ```

- Response

  :

  ```
  [
    {
    	"type":"<post_or_note>"
      "id": "<post_or_note_id>",
      "username": "<author_username>",
      "title": "<post_title_or_empty>",
      "content_preview": "<first_two_lines_of_content>",
      "likes": "<like_count>",
      "views": "<view_count>"
    }
  ]
  ```

#### 17. 获取可用Tags列表

- **Endpoint**: `/tags`

- **Method**: `GET`

- Response

  :

  ```
  {
    "tags": [
      "<tag>"
    ]
  }
  ```