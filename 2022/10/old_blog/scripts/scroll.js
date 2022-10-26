// 上滑隐藏导航栏, 下滑显示导航栏
// 第一种
// 检测touchmove的坐标
const slider = document.getElementById('main');
let moveDirection = null;
let moveCount = 0;

slider.addEventListener('touchmove', (event) => {
    if (event.type == 'touchmove') {
        moveCount ++;
    }
    
    if (slider.getBoundingClientRect().top == 44) {
        document.getElementsByTagName('header')[0].classList.remove('is-hide')
    }

    if (moveDirection && moveCount > 5) {
        move_num = event.changedTouches[0].clientY - moveDirection;
        if (move_num > 0) {
            document.getElementsByTagName('header')[0].classList.remove('is-hide');
        }
        else if (move_num < 0 && slider.getBoundingClientRect().top < 0) {
            document.getElementsByTagName('header')[0].classList.add('is-hide');
        }
        moveCount = 0;
    }
    else {
        moveDirection = event.changedTouches[0].clientY
    }
})



// 滚轮事件
document.getElementById('main').addEventListener('wheel', (event) => {
    if (event.deltaY > 0 && slider.getBoundingClientRect().top < 0) {
        document.getElementsByTagName('header')[0].classList.add('is-hide')
    }
    else {
        if (event.deltaY < 0) {
            document.getElementsByTagName('header')[0].classList.remove('is-hide')
        }
    }
});
