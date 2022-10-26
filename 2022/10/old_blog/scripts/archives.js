// 返回当前页面的浏览器参数列表
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

// 用于生成单篇幅的函数
function RenderArticlesList(data) {
    
    let result = ''
    if (data != null && data.length != 0) {
        for (var i = 0; i < data.length; i++) {
            dict = data[i]
            // 标题缩略
            if (dict.title.length > 30) {
                title = dict.title.slice(0, 30) + '...'
            }
            else {
                title = dict.title
            }

            var converter = new showdown.Converter(),
            detail = converter.makeHtml(dict.detail);
            // console.log(detail);
            // console.log(title);
            // console.log(dict.aid)
            // console.log(dict.tagList)

            let labelList = ''
            let createdTime = dict.createdTime
            let modifiedTime = dict.modifiedTime
            for (var j = 0; j < dict.tagList.length; j++) {
                labelList += `<a href="/archives/?tags=${dict.tagList[j]}">${dict.tagList[j]}</a>`
            }

            let href = `/articles/?aid=${dict.aid}`
            result += `<div class="pre-article"><div class="pre-article-title"><a href="${href}">${title}</a></div><div class="pre-article-show">${detail}</div><div class="pre-article-info">
            <a href="/archives/?year=${createdTime.tm_year}&month=${createdTime.tm_mon}&day=${createdTime.tm_mday}&filter=0">Created: ${dict.createdTime.tm_year}-${dict.createdTime.tm_mon}-${dict.createdTime.tm_mday}</a>
            <a href="/archives/?year=${modifiedTime.tm_year}&month=${modifiedTime.tm_mon}&day=${modifiedTime.tm_mday}&filter=1">Modified: ${dict.modifiedTime.tm_year}-${dict.modifiedTime.tm_mon}-${dict.modifiedTime.tm_mday}</a>
            ${labelList}</div></div>`
        }
        document.getElementById("container").innerHTML = result
    }
    else {
        document.getElementById("container").innerHTML = `<div class="pre-article">空空如也</div>`
    }
    
}

// 数组切割-10个一组
function cutArray(data) {
    let filter = new Array
    let tempLi = new Array
        let g = 0
        for (var i = 0, j = 0; i < data.length; i++, j++) {
            if (j == 10) {
                filter[g] = tempLi
                tempLi = new Array
                g += 1
                j = 0
            }
            tempLi.push(data[i])
        }
        filter[g] = tempLi
    return filter
}

// 创建时间过滤函数
function createdTimeFilter(data, year, month, day) {
    // 无年月日
    if (year == 0 && month == 0 && day == 0) {
        filter = cutArray(data)
    }
    // 有年月无日
    else if (year != 0 && month != 0 && day == 0){
        let temp = new Array
        for (var i = 0; i < data.length; i++) {
            if (data[i].createdTime.tm_year == year && data[i].createdTime.tm_mon == month) {
                temp.push(data[i])
            }
        }
        filter = cutArray(temp)
    }
    // 有年无月日
    else if (year != 0 && month == 0 && day == 0) {
        let temp = new Array
        for (var i = 0; i < data.length; i++) {
            if (data[i].createdTime.tm_year == year) {
                temp.push(data[i])
            }
        }
        filter = cutArray(temp)
    }
    else {
        let temp = new Array
        for (var i = 0; i < data.length; i++) {
            if (data[i].createdTime.tm_year == year && data[i].createdTime.tm_mon == month && data[i].createdTime.tm_mday == day) {
                temp.push(data[i])
            }
        }
        filter = cutArray(temp)
    }
    return filter
}

// 修改时间过滤函数
function modifiedTimeFilter(data, year, month, day) {
    // 无年月日
    if (year == 0 && month == 0 && day == 0) {
        filter = cutArray(data)
    }
    // 有年月无日
    else if (year != 0 && month != 0 && day == 0){
        let temp = new Array
        for (var i = 0; i < data.length; i++) {
            if (data[i].modifiedTime.tm_year == year && data[i].modifiedTime.tm_mon == month) {
                temp.push(data[i])
            }
        }
        filter = cutArray(temp)
    }
    // 有年无月日
    else if (year != 0 && month == 0 && day == 0) {
        let temp = new Array
        for (var i = 0; i < data.length; i++) {
            if (data[i].modifiedTime.tm_year == year) {
                temp.push(data[i])
            }
        }
        filter = cutArray(temp)
    }
    else {
        let temp = new Array
        for (var i = 0; i < data.length; i++) {
            if (data[i].modifiedTime.tm_year == year && data[i].modifiedTime.tm_mon == month && data[i].modifiedTime.tm_mday == day) {
                temp.push(data[i])
            }
        }
        filter = cutArray(temp)
    }
    return filter
}

// 浏览器无刷新修改url
function reloadBrowserUrl(obj) {
    let _obj = new window.URL(window.location.href);
    for (var key in obj) {
        if (key == 'tags') {
            let temp = ''
            if (obj[key].size == 0) {
                _obj.searchParams.set(key, temp)
            }
            else {
                for (var c of obj[key]) {
                    temp += `${c},`
                }
                // 编码
                temp = encodeURI(temp)
                // 去除末尾逗号
                if (temp != '') {
                    temp = temp.substring(0, temp.length-1)
                }
                _obj.searchParams.set(key, temp)
            }
        }
        else {
            _obj.searchParams.set(key, obj[key]);
        }
    }
    history.replaceState({}, 0, _obj.href);
}

// 读取input框内的年月日
function readYMD() {
    var year = document.getElementById('fc-year').value
    var month = document.getElementById('fc-month').value
    var day = document.getElementById('fc-day').value

    return year, month, day
}

// 排序选择
function makeFilter(data, _filter, sn, year, month, day, tagsSet) {
    // 标签筛选
    let dataTemp = new Array()
    if (tagsSet.size != 0) {
        for (var i = 0; i < data.length; i++) {
            let dl = data[i].tagList
            for (var j = 0; j < dl.length; j++) {
                if (tagsSet.has(dl[j])) {
                    dataTemp.push(data[i])
                }
            }
        }
        data = dataTemp
    }

    let filter = null
    if (!_filter) {
        data.sort((a, b) => {
            if (a.createdTime.timeStamp < b.createdTime.timeStamp) {
                return sn;
            }
            if (a.createdTime.timeStamp > b.createdTime.timeStamp) {
                return -sn;
            }
            // timeStamp must be equal
            return 0;
        })
        filter = createdTimeFilter(data, year, month, day)
    }
    else {
        data.sort((a, b) => {
            if (a.modifiedTime.timeStamp < b.modifiedTime.timeStamp) {
                return sn;
            }
            if (a.modifiedTime.timeStamp > b.modifiedTime.timeStamp) {
                return -sn;
            }
            // timeStamp must be equal
            return 0;
        })
        filter = modifiedTimeFilter(data, year, month, day)
    }
    return filter;
}

// 按钮显示
function buttonShow(nowPage, filter) {
    let psLeft = document.getElementById('ps-left')
    let psRight = document.getElementById('ps-right')
    
    psLeft.style.display = ''
    psRight.style.display = ''
    
    if (nowPage == 0) {
        psLeft.style.display = 'none'
    }
    if (nowPage == filter.length-1) {
        psRight.style.display = 'none'
    }
}

// 标签渲染 => 返回集合(存放既在url也在data中的标签)
function renderTags(data, urlTags) {
    // console.log(data, urlTags)
    let tagsSet = new Set();
    let urlTagsSet =  new Set();

    for (var i = 0; i < data.length; i++) {
        var tagList = data[i].tagList

        for (var j = 0; j < tagList.length; j++) {
            tagsSet.add(tagList[j])
        }
    }

    for (var i = 0; i < urlTags.length; i++) {
        urlTagsSet.add(decodeURI(urlTags[i]))
    }

    // console.log(tagsSet)
    // console.log(urlTagsSet)

    let result = ''
    let newTagsSet = new Set()

    for (var i of tagsSet) {
        // console.log(i)
        // console.log(urlTagsSet.has(i))
        if (urlTagsSet.has(i)) {
            newTagsSet.add(i)
            result += `<div class="fc-tag tag-option">${i}</div>`
        }
        else {
            result += `<div class="fc-tag tag-default">${i}</div>`
        }
    }
    document.getElementById("fc-tagList").innerHTML = result

    return newTagsSet
}

// 返回所有选中标签的集合
function allOptionTags() {
    let tagOption = document.getElementsByClassName('tag-option')
    let tagsSet = new Set()

    for (let t = 0; t < tagOption.length; t++) {
        tagsSet.add(tagOption[t].innerText)
    }

    return tagsSet
}

fetch('/config/ArticleConfig.json', {
    method: 'GET',
}).then(res => res.json()).then(data => {
    // console.log(data);
    
    param = getUrlParams()

    let year = 0
    let month = 0
    let day = 0

    if ('year' in param && !isNaN(param['year'])) {
        year = Number(param['year'])
        let date = new Date()
        if (year < 0 || (0 < year && year < 2022) || year > date.getFullYear()) {
            year = 0
        }
    }
    if ('month' in param && !isNaN(param['month'])) {
        month = Number(param['month'])
        if (month < 0 || month > 12) {
            month = 0
        }
    }
    if ('day' in param && !isNaN(param['day'])) {
        day = Number(param['day'])
        if (day < 0 || day > 31) {
            day = 0
        }
    }

    // 0为是order, 1是reverse order
    let order = 0
    if ('order' in param) {
        if (!isNaN(param['order'])) {
            if (!Number(param['order'])) {
                order = 0
            }
            else {
                order = 1
            }
        }
        else {
            order = 0
        }
    }
    
    let urlTags = []
    if ('tags' in param) {
        var tags = param['tags']
        urlTags = tags.split('%2C')
    }

    // 依据order值修改按钮显示的文本
    let sn = 1
    if (order) {
        sn = -1
        document.getElementById('archives-order').innerText = 'Reverse order'
    }
    else {
        sn = 1
        document.getElementById('archives-order').innerText = 'Order'
    }

    // 0是created, 1是modified
    let _filter = 0
    if ('filter' in param && !isNaN(param['filter'])) {
        if (!Number(param['filter'])) {
            _filter = 0
            document.getElementById('archives-filter').innerText = 'Created'
        }
        else {
            _filter = 1
            document.getElementById('archives-filter').innerText = 'Modified'
        }
    }
    else {
        _filter = 0
        document.getElementById('archives-filter').innerText = 'Created'
    }

    let tagsSet = renderTags(data, urlTags)

    // 数组排序
    let filter = makeFilter(data, _filter, sn, year, month, day, tagsSet)

    // 将浏览器获取的参数回填进搜所栏中
    document.getElementById('fc-year').value = year
    document.getElementById('fc-month').value = month
    document.getElementById('fc-day').value = day

    // 无刷新url参数修改
    reloadBrowserUrl({
        'year': year,
        'month': month,
        'day': day,
        'order': order,
        'filter': _filter,
        'tags': tagsSet
    })

    // 渲染页面初始化
    let nowPage = 0

    // 渲染缩略文章
    RenderArticlesList(filter[nowPage])

    // 按钮渲染
    buttonShow(nowPage, filter)

    // 左翻页
    document.getElementById('ps-left').addEventListener('click', (event) => {
        event.preventDefault();

        nowPage--
        RenderArticlesList(filter[nowPage])
        buttonShow(nowPage, filter)
    })
    
    // 右翻页
    document.getElementById('ps-right').addEventListener('click', (event) => {
        event.preventDefault();

        nowPage++
        RenderArticlesList(filter[nowPage])
        buttonShow(nowPage, filter)
    })

    // 搜索
    document.getElementById('archives-search').addEventListener('click', (event) => {
        event.preventDefault();

        year, month, day = readYMD()

        tagsSet = renderTags(data, urlTags)

        reloadBrowserUrl({
            'year': year,
            'month': month,
            'day': day,
            'order': order,
            'filter': _filter,
            'tags': tagsSet
        })

        // 数组排序
        let filter = makeFilter(data, _filter, sn, year, month, day, tagsSet)

        nowPage = 0
        RenderArticlesList(filter[nowPage])
        buttonShow(nowPage, filter)
    })

    // 排序
    document.getElementById('archives-order').addEventListener('click', (event) => {
        event.preventDefault();

        // 取反
        order = !order

        // 修改标签显示
        let sn = 1
        if (order) {
            sn = -1
            document.getElementById('archives-order').innerText = 'Reverse order'
        }
        else {
            sn = 1
            document.getElementById('archives-order').innerText = 'Order'
        }

        year, month, day = readYMD()

        tagsSet = allOptionTags()

        reloadBrowserUrl({
            'year': year,
            'month': month,
            'day': day,
            'order': order,
            'filter': _filter,
            'tags': tagsSet
        })

        // 数组排序
        let filter = makeFilter(data, _filter, sn, year, month, day, tagsSet)
        
        nowPage = 0
        RenderArticlesList(filter[nowPage])
        buttonShow(nowPage, filter)
    })

    // 修改时间 | 创建时间过滤
    document.getElementById('archives-filter').addEventListener('click', (event) => {
        event.preventDefault();

        year, month, day = readYMD()

        // 修改_filter的值
        if (_filter) {
            _filter = 0
            document.getElementById('archives-filter').innerText = 'Created'
        }
        else {
            _filter = 1
            document.getElementById('archives-filter').innerText = 'Modified'
        }

        tagsSet = allOptionTags()

        reloadBrowserUrl({
            'year': year,
            'month': month,
            'day': day,
            'order': order,
            'filter': _filter,
            'tags': tagsSet
        })

        // 数组排序
        let filter = makeFilter(data, _filter, sn, year, month, day, tagsSet)

        nowPage = 0
        RenderArticlesList(filter[nowPage])
        buttonShow(nowPage, filter)
    })

    // 按钮点击变换颜色同时改变url的显示,还要刷新文章过滤
    let fcTag = document.getElementsByClassName('fc-tag')
    for (let i = 0; i < fcTag.length; i++) {
        fcTag[i].addEventListener('click', (event) => {
            event.preventDefault();

            let cl = fcTag[i].classList

            if (cl.contains('tag-default')) {
                cl.replace('tag-default', 'tag-option')
            }
            else if (cl.contains('tag-option')) {
                cl.replace('tag-option', 'tag-default')
            }

            year, month, day = readYMD()
            // tagsSet = renderTags(data, urlTags)

            tagsSet = allOptionTags()

            reloadBrowserUrl({
                'year': year,
                'month': month,
                'day': day,
                'order': order,
                'filter': _filter,
                'tags': tagsSet
            })

            // 数组排序
            let filter = makeFilter(data, _filter, sn, year, month, day, tagsSet)

            nowPage = 0
            RenderArticlesList(filter[nowPage])
            buttonShow(nowPage, filter)
        })
    }
})