// 获取浏览器url中的参数
function getUrlParams() {
    var s = window.location.search.substring(1)
    // console.log(s)
    s = s.split('&')
    var dic = new Array()
    for (var i = 0; i < s.length; i++) {
        var j = s[i].split('=')
        dic[j[0]] = j[1]
    }
    return dic
}

// 给代码块添加类
function writePR() {
    var list = document.getElementsByTagName('code')
    for (var i = 0; i < list.length; i++) {
        list[i].classList.add('prettyprint', 'linenums')
    }
}

// 给table标签套div
function nestedElements() {
    let divElement = document.createElement('div')
    divElement.classList.add('table-box')
    const tabelElement = document.querySelectorAll('table')

    for (var i = 0; i < tabelElement.length; i++) {
        tabelElement[i].parentNode.insertBefore(divElement, tabelElement[i].nextElementSibling)
        divElement.appendChild(tabelElement[i])
    }
}

// 获取aid在data中索引的值
function makeAim(data, aid, addNum) {
    var result = data.findIndex((element, index, array) => {
        if (element.aid == aid) {
            return true
        }
    }) + addNum
    return result
}

// 渲染页面
function RenderArticle(aim, data) {
    if (aim == 0) {
        document.getElementById('ps-left').style.display = 'none'
    }
    else if (aim == data.length-1) {
        document.getElementById('ps-right').style.display = 'none'
    }
    else {
        document.getElementById('ps-left').style.display = ''
        document.getElementById('ps-right').style.display = ''
    }

    let obj = new window.URL(window.location.href);
    obj.searchParams.set('aid', data[aim]['aid']);
    history.replaceState({}, 0, obj.href);
 
    let url = `/articles/${data[aim]['aid']}.md`
    fetch(url, {
        method: 'GET'
    }).then(res => res.text()).then(
        data => {
            text = data
            var converter = new showdown.Converter({tables: true, strikethrough: true, tasklists: true}),
            html = converter.makeHtml(text);
            article.innerHTML = html;
        }
    ).then(() => {
        writePR()
        nestedElements()
        PR.prettyPrint();
    })
}

// 文章信息渲染
function articleInfo(data, aim) {
    // console.log(data[aim])
    let obj = data[aim]
    const articleInfo = document.getElementById("article-info-container")

    let labelList = ''
    for (var j = 0; j < obj.tagList.length; j++) {
        labelList += `<div class="article-info-box"><a href="#">${obj.tagList[j]}</a></div>`
    }
    let result = `<div class="article-info-box">
        <a href="/archives/?year=${obj.createdTime.tm_year}&month=${obj.createdTime.tm_mon}&day=${obj.createdTime.tm_mday}&filter=0">Created: ${obj.createdTime.tm_year}-${obj.createdTime.tm_mon}-${obj.createdTime.tm_mday}</a>
    </div>
    <div class="article-info-box">
        <a href="/archives/?year=${obj.modifiedTime.tm_year}&month=${obj.modifiedTime.tm_mon}&day=${obj.modifiedTime.tm_mday}&filter=1">Modified: ${obj.modifiedTime.tm_year}-${obj.modifiedTime.tm_mon}-${obj.modifiedTime.tm_mday}</a>
    </div>${labelList}`
    
    articleInfo.innerHTML = result
}

let dic = getUrlParams()

if ('aid' in dic) { 
    aid = Number(dic['aid'])
    
    let url = `/articles/${aid}.md`;
    const article = document.getElementById('article');
    fetch(url, {
        method: 'GET'
    }).then(res => res.text()).then(
        data => {
            text = data
            var converter = new showdown.Converter({tables: true, strikethrough: true, tasklists: true}),
            html = converter.makeHtml(text);
            article.innerHTML = html;
        }
    ).then(() => {
        writePR()
        nestedElements()
        PR.prettyPrint();
    })


    fetch('/config/ArticleConfig.json', {
        method: 'GET',
    }).then(res => res.json()).then(data => {
        // console.log(data);

        // 排序
        data.sort((a, b) => {
            if (a.createdTime.timeStamp < b.createdTime.timeStamp) {
                return -1;
            }
            if (a.createdTime.timeStamp > b.createdTime.timeStamp) {
                return 1;
            }
            // timeStamp must be equal
            return 0;
        }) 

        if (aid == data[0]['aid']) {
            document.getElementById('ps-left').style.display = 'none'
        }
        if (aid == data[data.length-1]['aid']) {
            document.getElementById('ps-right').style.display = 'none'
        }
        
        let aim = makeAim(data, aid, 0)
        articleInfo(data, aim)

        // 左翻页
        document.getElementById('ps-left').addEventListener('click', (event) => {
            event.preventDefault();

            let aid = Number(getUrlParams()['aid'])

            let aim = makeAim(data, aid, -1)

            articleInfo(data, aim)

            RenderArticle(aim, data)
        })
        
        // 右翻页
        document.getElementById('ps-right').addEventListener('click', (event) => {
            event.preventDefault();

            let aid = Number(getUrlParams()['aid'])
            
            let aim = makeAim(data, aid, 1)

            articleInfo(data, aim)

            RenderArticle(aim, data)
        })
    })
}
else {
    window.location = "/404.html"
}

