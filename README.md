Django_form 简易使用收录

## 项目为一个 APP 可以看看对应的 Views.py , forms.py, html 了解下述相关说明。  


`wiget` 定义的是详情页中的`class `和相关窗体的属性(例如`ID`, `placeforder`(提示)等);

如果没有指定` form.FormField() `构造方法中的` forms.xInput(wiget) `那么就会默认`"id" = str(id_)+"name" `
	
### 另外理解Form构造的原理；
- 1, 自带一个检验。
- 2, 可以在后台完成相关属性 `Input` 的设置。

### 解释
- 实际设置了Form之后, 通过调用产生了成熟的Html中表单的声明。所以当不知道某些字段 FormField 对象的使用, 可以在Django后台的html中查看, 下面给出一个示例; 当然也可以查看官方文档; 
### 举例
**例如直接抽取出来后加载admin相关的静态文件就可以完成上面的步骤。**

```
	<form enctype="multipart/form-data" action="/gjk/test/" method="post" > <!--id="focusarticle_form" novalidate--> 
	<!-- <input type='hidden' name='csrfmiddlewaretoken' value='YQT3Uk3995RZq1kfkmhqfMt8bLJYb1cvcIUAHru6YbwXNOwMimYOEEBEQusotBO0' /> -->

<div>
  <fieldset class="module aligned ">
    {% csrf_token %}
        <!--
        <div class="form-row field-toutiao">
                <div class="checkbox-row">
                        <input id="id_toutiao" name="toutiao" type="checkbox" /><label class="vCheckboxLabel" for="id_toutiao">设为头条</label>       
                </div>
        </div>

        <div class="form-row field-pic">
                <div>                
                        <label class="required" for="id_pic">头条图片436*200:</label>      
                            <input id="id_pic" name="pic" type="file" />
                </div>
        </div>
    -->	<div class="form-row" field-tag>
```

接着 `commit` 提交表单的时候使用 `request.POST("name")` 获取表单输入即可。省略了自定义Form的过程, 所以不是用`Form(request.POST)` ; 但是仍然具有基础验证的功能。

### 后记

**基本上表单都能解决，并且本方法上手简单至极。**
