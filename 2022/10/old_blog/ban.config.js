export const config = {
    title : '博客',
    navigation : [
        {
            name: '首页',
            href: '/',
            child: []
        },
        {
            name: '归档',
            href: '/',
            child: null
        },
        {
            name: '管理',
            href: '/',
            child: [
                {
                    name: '宝塔',
                    href: '',
                    child: []
                },
                {
                    name: '后台',
                    href: '',
                    child: []
                }
            ]
        },
        {
            name: '社交',
            href: '/',
            child: [
                {
                    name: 'Github',
                    href: '',
                    child: [
                        {
                            name: 'Profile',
                            href: '',
                            child: []
                        },
                        {
                            name: 'Star',
                            href: '',
                            child: []
                        },
                        {
                            name: 'Repos',
                            href: '',
                            child:[]
                        }
                    ]
                },
                {
                    name: 'bilibili',
                    href: '',
                    child: []
                },
                {
                    name: '米游社',
                    href: 'https://bbs.mihoyo.com/ys/',
                    child: []
                }
            ]
        },
        {
            name: '友情链接',
            href: '/',
            child: null
        }
    ],
    mottoList : [
        "Olah! Olah!",
        "Yoyo mosi mita!",
        "Nye,nye mosi mita,",
        "Yeye mosi gusha!",
        "Mosi gusha, mosi tiga",
        "Yeye kucha kucha!"
    ],
    copyright: {
        name: '',
        link: ''
    }
    
}