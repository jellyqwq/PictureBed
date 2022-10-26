let config = null
fetch('/config/config.json', {
    method: 'GET',
}).then(res => res.json()).then(data => {
    config = data
    // title insert
    document.getElementsByTagName('title')[0].innerText = config.title

    // site title insert
    document.getElementsByClassName('site-title')[0].innerText = config.title

    // bottom info insert
    document.getElementById('copyright-name').innerText = config.copyright.name
    document.getElementById('copyright-link').href = config.copyright.link

    // 多级导航生成
    let outputList = config.navigation
    let oneLock = false
    let twoLock = false
    let alstr = ''
    let maxDistance = 0
    let maxDistanceCompare = 0

    // 对象检测,是否为数组 ? 是则返回返回数组, 否则返回空数组
    function isList(obj) {
        if (obj) {
            if (obj instanceof Array) {
                return obj
            }
            else {
                return []
            }
        }
        else {
            return []
        }
    }

    // 递归生成结构
    function rescircle(list) {
        list = isList(list)
        if (!oneLock) {
            if (list.length == 0) {
                alstr = ''
            }
            else {
                let containerList = []
                let animationTime = 0.6
                for (var i = 0; i < list.length; i++) {
                    var listChild = isList(list[i].child)
                    if (listChild.length != 0) {
                        oneLock = true
                        containerList.push(`<li class="nav-link" style="--i: ${animationTime}s"><a href="javascript:void(0);">${list[i].name}</a>${rescircle(list[i].child)}</li>`)
                        animationTime += 0.25
                    }
                    else {
                        containerList.push(`<li class="nav-link" style="--i: ${animationTime}s"><a href="${list[i].href}">${list[i].name}</a></li>`)
                        animationTime += 0.25
                    }
                }
                var tempStr = ''
                for (var i = 0; i < containerList.length; i++) {
                    tempStr += containerList[i]
                }
                alstr = `<ul>${tempStr}</ul>`
            }
        }
        else {
            if (!twoLock) {
                let containerList = []
                for (var i = 0; i < list.length; i++) {
                    var listChild = isList(list[i].child)
                    if (listChild.length == 0) {
                        containerList.push(`<li class="dropdown-link"><a href="${list[i].href}">${list[i].name}</a></li>`)
                    }
                    else {
                        twoLock = true
                        containerList.push(`<li class="dropdown-link"><a href="javascript:void(0);">${list[i].name}</a>${rescircle(list[i].child)}</li>`)
                        if (maxDistanceCompare > maxDistance) {
                            maxDistance = maxDistanceCompare
                            maxDistanceCompare = 0
                        }
                    }
                    var tempStr = ''
                    for (var j = 0; j < containerList.length; j++) {
                        tempStr += containerList[j]
                    }
                }
                oneLock = false
                return `<div class="dropdown"><ul>${tempStr}</ul></div>`
            }
            else {
                let containerList = []
                for (var i = 0; i < list.length; i++) {
                    var listChild = isList(list[i].child)
                    if (listChild.length == 0) {
                        containerList.push(`<li class="dropdown-link"><a href="${list[i].href}">${list[i].name}</a></li>`)
                    }
                    else {
                        containerList.push(`<li class="dropdown-link"><a href="javascript:void(0);">${list[i].name}</a>${rescircle(list[i].child)}</li>`)
                    }
                    var tempStr = ''
                    for (var j = 0; j < containerList.length; j++) {
                        tempStr += containerList[j]
                    }
                }
                oneLock = false
                twoLock = false
                maxDistanceCompare += 1
                return `<div class="dropdown second"><ul>${tempStr}</ul></div>`
            }
        } 
    }
    rescircle(outputList)
    document.getElementById('nav-box-1').innerHTML = alstr


    // motto module
    const mottoList = config.mottoList
    const mottoListLenth = config.mottoList.length
    const motto = document.getElementById('motto')

    let mottoString = '';
    let mottoCharIndex = 0
    let mottoSentenceIndex = 0
    let isPositive = true

    setInterval(() => {
        // 比较句子个数
        if (mottoSentenceIndex < mottoListLenth) {
            // 获取每个句子的长度
            let mottoCharLenth = mottoList[mottoSentenceIndex].length
            if (!isPositive) {
                mottoCharIndex--
                if (mottoCharIndex < 0) {
                    mottoSentenceIndex++
                    isPositive = true
                    mottoCharIndex = 0
                }
                else {
                    mottoString = mottoString.slice(0, mottoCharIndex)
                    motto.innerText = mottoString
                }
            }
            else if (mottoCharIndex < mottoCharLenth && isPositive) {
                mottoString += mottoList[mottoSentenceIndex][mottoCharIndex]
                motto.innerText = mottoString
                mottoCharIndex++
            }
            else {
                isPositive = false
            }
        }
        else {
            mottoSentenceIndex = 0
        }
    }, 200)
});