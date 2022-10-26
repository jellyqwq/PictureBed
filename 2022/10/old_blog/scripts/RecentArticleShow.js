fetch('/config/ArticleConfig.json', {
    method: 'GET',
}).then(res => res.json()).then(data => {
    // console.log(data);

    // 排序
    data.sort((a, b) => {
        if (a.createdTime.timeStamp < b.createdTime.timeStamp) {
            return 1;
        }
        if (a.createdTime.timeStamp > b.createdTime.timeStamp) {
            return -1;
        }
        // timeStamp must be equal
        return 0;
    })

    let result = ''
    let c = 0
    for (var i = 0; i < data.length; i++) {
        if (c == 10) {
            break
        }
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

        let createdTime = dict.createdTime
        let modifiedTime = dict.modifiedTime
        let labelList = ''
        for (var j = 0; j < dict.tagList.length; j++) {
            labelList += `<a href="/archives/?tags=${dict.tagList[j]}">${dict.tagList[j]}</a>`
        }

        let href = `/articles/?aid=${dict.aid}`
        result += `<div class="pre-article"><div class="pre-article-title"><a href="${href}">${title}</a></div><div class="pre-article-show">${detail}</div><div class="pre-article-info">
        <a href="/archives/?year=${createdTime.tm_year}&month=${createdTime.tm_mon}&day=${createdTime.tm_mday}&filter=0">Created: ${dict.createdTime.tm_year}-${dict.createdTime.tm_mon}-${dict.createdTime.tm_mday}</a>
        <a href="/archives/?year=${modifiedTime.tm_year}&month=${modifiedTime.tm_mon}&day=${modifiedTime.tm_mday}&filter=1">Modified: ${dict.modifiedTime.tm_year}-${dict.modifiedTime.tm_mon}-${dict.modifiedTime.tm_mday}</a>
        ${labelList}</div></div>`
        c += 1
    }
    document.getElementById("container").innerHTML = result
});