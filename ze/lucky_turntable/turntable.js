var turntable = {
    lightNum : 18, // 灯泡数量
    lightWrap: null, //转盘容器
    itemNum: [
        {
            type : 1,
            prize : '谢谢惠顾'
        },
        {
            type : 2,
            prize : '1块'
        },
        {
            type : 2,
            prize : '1块'
        },
        {
            type : 2,
            prize : '2块'
        },
        {
            type : 2,
            prize : '2块'
        },
        {
            type : 2,
            prize : '5块'
        }
    ], //转盘内容
    bgWrap: null, //转盘背景容器
    giftWrap: null, //转盘奖品内容容器
    isGoing: false, //转盘是否开始
    init : function () {
        //初始化灯泡
        var lightFragment = document.createDocumentFragment();
        for (var i = 0; i < this.lightNum; i++) {
            var lightItem = document.createElement('span');
            var deg = (360 / this.lightNum) * i;
            lightItem.style.transform = 'rotate(' + deg + 'deg)';
            lightFragment.appendChild(lightItem);
        }
        this.lightWrap.appendChild(lightFragment);

        //初始化转盘背景
        var bgFragment = document.createDocumentFragment();
        for (var i = 0; i < this.itemNum.length; i++) {
            var bgItem = document.createElement('li');
            var deg = (360 / this.itemNum.length) * i;
            bgItem.style.transform = 'rotate(' + deg + 'deg)';
            bgFragment.appendChild(bgItem);
        }
        this.bgWrap.appendChild(bgFragment);
        this.bgWrap.style.transform = 'rotate(' +  360/this.itemNum.length/2 + 'deg)';

        //初始化转盘奖品内容
        var giftFragment = document.createDocumentFragment();
        for (var i= 0; i < this.itemNum.length; i++) {
            var giftItem = document.createElement('li');
            var deg = (360 / this.itemNum.length) * i;
            giftItem.style.transform = 'rotate(' + deg + 'deg)';
            var span = document.createElement('span');
            giftItem.appendChild(span);
            giftFragment.appendChild(giftItem);
        }
        this.giftWrap.appendChild(giftFragment);

        function gameStar() {
            if (this.isGoing) return;
            this.isGoing = true;
        }
    }
}

turntable.lightWrap = document.getElementById('turntable-light');
turntable.bgWrap = document.getElementById('turntable_bg');
turntable.giftWrap = document.getElementById('turntable_gift');
turntable.init();