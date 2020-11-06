// static/js/index.js
// console.log('外部js文件加载成功');
// console.log(faderData);

$(function () {
    // 声明本地图片路径
    // var BASE_URL = 'http://127.0.0.1:8000/'
    var BASE_URL = '../static/images/';
    var html = '';//保存拼接的文本内容
    // html += '<li class="silde">'
    // html += '<a href="#">'
    /*
        遍历faderDate,获取数组中的每一个元素(对象)
        将对象的属性依次拼接到html中
        <li class="slide">
            <a href="#">
                <img src="../static/images/banner01.jpg" alt="">
                <span class="imginfo">
                        爬虫微课5小时 Python学习路线!
                </span>
            </a>
        </li>
    */
    $.each(faderData,function(i,o){
        html += '<li class="slide">'
        html += '<a href="#">'
        html += `<img src="${BASE_URL+o.img_url}">`
        html += '<span class="imginfo">'
        html += o.img_info
        html += '</span></a></li>'
    })

    // console.log(html)
    // 添加到页面 找到兄弟元素 追加到兄弟元素上方
    $('.fader_controls').before(html);

    // easyFader()是由jquery.easyfader.min.js提供的函数
    // 导入顺序jquery-->jquery.easyfader-->index
    $('.fader').easyFader();





    // 加载博客
    // 定义一个函数 传入数据 在页面加载指定数量的博客
    // 所有的博客数据保存在blogs.data.js中
    function add_blogs(data){
        var html = ''
        $.each(data,function(i,o){
            var blog = `
            <div class="blogs">
                <h3 class="blogtitle">
                    <a href="#">
                        ${o.blogtitle}
                    </a>
                </h3>
                <div class="blogpic">
                    <a href="#">
                        <img src="${BASE_URL+o.blogpic}">
                    </a>
                </div>
                <div class="blogtext">
                    ${o.blogtext}
                </div>
                <ul>
                    <li><a href="#">${o.bloginfo.author}</a></li>
                    <li class="lmname"><a href="#">
                    ${o.bloginfo.lmname}
                    </a></li>
                    <li class="timer"><a href="#">${o.bloginfo.timer}</a></li>
                    <li class="view"><a href="#">
                    ${o.bloginfo.view}</a></li>
                    <li class="like"><a href="#">${o.bloginfo.like}</a></li>
                </ul>
            </div>
            `
            html += blog
        })//each结束
        // 将 拼接好的内容添加到页面
        $('.blogsbox').append(html);
    }//函数add_blog结束
    // 16:53~17:10
    // 当页面加载时  显示前3条数据
    // blogData.slice(0,3)
    // slice(strat,end)截取 从索引值start位置开始 
    // 到end-1位置结束
    add_blogs(blogData.slice(0,3))


    // 鼠标滚轮滚动事件
    $(document).scroll(function(){
        // console.log('滚啦')
        // 滚动条高度
        var scrollTop = $(document).scrollTop()
        // 当前窗口可视范围高度
        var windowHeight = $(window).height()
        // 完整文档高度
        var documentHeight = $(document).height()

        // console.log(scrollTop,windowHeight,documentHeight)
        if(documentHeight-scrollTop-windowHeight<=200){
            // console.log('马上突破底线了')
            // 获取后5条数据
            // 页面中3条 sclice(3,8)
            // 页面中8条 sclice(8,13)
            // 页面中13条 sclice(13,18)
            // 页面中n条 sclice(n,n+5)
            // 获取页面中博客的数量
            var n = $('.blogs').length;
            // console.log(n)
            // 通过数量获取数据
            var data = blogData.slice(n,n+5);
            if(data.length>0){
                add_blogs(data)
            }else{
                alert('没有数据啦')
            }
        }

    })

})