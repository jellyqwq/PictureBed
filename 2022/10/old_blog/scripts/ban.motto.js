import {config} from '../config.js'

const mottoList = config.mottoList
const mottoListLenth = config.mottoList.length
const motto = document.getElementById('motto')

window.onload = (event) => {
    event.preventDefault();
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
}
