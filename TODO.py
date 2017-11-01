#TODO
#登录请求
#url:/user/login/
#方法:POST
#参数:{"username",用户名，"password":密码}
#返回方式：HttpResponse
#返回值:登录成功返回1，用户名不存在或密码错误返回0，表单数据无效返回2

#注册请求
#url:/user/signup/
#方法:POST
#参数:{"username",用户名，"password":密码}
#返回方式：HttpResponse
#返回值:注册成功返回1，用户名存在返回0，表单数据无效返回2


#搜索请求
#url:/library/search/
#方法:POST
#参数:{"type":搜索类型,"content":搜索内容,"re":返回结果内容}
#注：
#type :搜索类型,在"id","title","author","seller","description",中选择
#content:搜索内容，搜索包含该内容的信息，id除外
#re :返回结果内容，为"all"时返回书本所有信息，为"id","title","author","seller","description"时返回特定信息
#返回方式: JsonResponse
#返回值: 包含内容的list，re为all时返回如[{"id":1,"title":"abc"...},{"id":2,"title":"cde"...}]
#                       re为"id","title","author","seller","description"时返回如[1,2,3..]或['abc','def',...]

#添加请求
#url: /library/append/
#参数:{"title":标题,"author":作者,"seller":卖家,"description":描述}
#注：不需要id，自动生成
#返回方式:HttpResponse
#返回值:被创建的书的id

#删除请求
#url: /library/remove/
#参数:{"id":id}
#注：只能删除特定id，其他情况先搜索再删除
#返回方式:HttpResponse
#返回值:删除成功返回1,删除失败（不存在）返回0