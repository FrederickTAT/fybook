#TODO
#用户登录请求
#url:/user/login/
#方法:POST
#参数:{"username",用户名，"password":密码}
#返回方式：HttpResponse
#返回值:登录成功返回1，用户名不存在或密码错误返回0，表单数据无效返回2

#用户注册请求
#url:/user/signup/
#方法:POST
#参数:{"username",用户名，"password":密码}
#返回方式：HttpResponse
#返回值:注册成功返回1，用户名存在返回0，表单数据无效返回2

#用户信息获得请求
#url:/user/getuser/
#方法:GET
#参数:{"id":用户id,"username":用户名}
#注：
#只搜索id,用户名留空
#只搜索用户名，id设为0
#返回方式:JsonResponse
#返回值:未查到到用户返回空字典，查找到返回字典，如{'id': 2, 'username': 'asd', 'password': '123', 'ifseller': False}

#书本搜索请求
#url:/library/booksearch/
#方法:POST
#参数:{"type":搜索类型,"content":搜索内容,"re":返回结果内容}
#注：
#type :搜索类型,在"id","title","author","seller","description",中选择
#content:搜索内容，搜索包含该内容的信息，id除外
#re :返回结果内容，为"all"时返回书本所有信息，为"id","title","author","seller","description"时返回特定信息
#返回方式: JsonResponse
#返回值: 包含内容的list，re为all时返回如[{"id":1,"title":"abc"...},{"id":2,"title":"cde"...}]
#                       re为"id","title","author","seller","description"时返回如[1,2,3..]或['abc','def',...]
#        未查询到时返回空list，即[]

#书本添加请求
#url: /library/bookadd/
#方法:POST
#参数:{"title":标题,"author":作者,"seller":卖家,"description":描述}
#注：不需要id，自动生成
#返回方式:HttpResponse
#返回值:被创建的书的id

#书本删除请求
#url: /library/bookremove/
#方法:POST
#参数:{"id":id}
#注：只能删除特定id，其他情况先搜索再删除
#返回方式:HttpResponse
#返回值:删除成功返回1,删除失败（不存在）返回0

#订单添加请求
#url:/orders/create/
#方法:POST
#参数:{"book_id":书本id,"customer":购买者}
#返回方式:HttpResponse
#返回值:订单创建成功返回1，订单已存在返回0

#订单删除请求
#url:/orders/delete/
#方法:POST
#参数:{"id":订单id}
#返回方式:HttpResponse
#返回值:订单删除成功返回1，订单不存在返回0

#订单查询请求
#url:/orders/getorder/
#方法:POST
#参数:{"id":订单id}
#返回方式:JsonResponse
#返回值:订单不存在返回空字典，订单存在返回字典，如{'id': 8, 'book_id': 1, 'customer': 'asd', 'ordertime': '2017-11-02 13:47:12', 'dealt': False}

#完成交易请求
#url:/orders/makedeal/
#方法:POST
#参数:{"id":订单id}
#返回方式:HttpResponse
#返回值:成功返回1，订单不存在返回0,订单已完成返回2

#取消交易请求
#url:/orders/canceldeal/
#方法:POST
#参数:{"id":订单id}
#返回方式:HttpResponse
#返回值:成功返回1，订单不存在返回0,订单已撤销返回2

#评论添加请求
#url:/library/commentadd/
#方法:POST
#参数:{"bookid":书本id."user":评论用户名,"content":评论内容,"rank":评分}
#注：rank的值从0,1,2,3,4,5中选择，默认为-1表示未评论
#返回方式:HttpResponse
#返回值:评论成功返回1

#评论删除请求
#url:/library/commentremove/
#方法:POST
#参数:{"id":评论id}
#返回方式:HttpResponse
#返回值:评论删除成功返回1，评论不存在返回0

#评论搜索请求
#url:/library/commentsearch/
#方法:GET
#参数:{"bookid":书本id}
#返回方式:JsonResponse
#返回值:若该book无comment，返回空list，即[],若该book有comment，返回list，如[{'id': 1, 'bookid': 1, 'user': 'unknown', 'time': '2017-11-04 13:15:05', 'content': 'Nothing', 'rank': -1}
#                                                                         ,{'id': 2, 'bookid': 1, 'user': 'unknown', 'time': '2017-11-04 13:15:51', 'content': 'Nothing', 'rank': -1}]
