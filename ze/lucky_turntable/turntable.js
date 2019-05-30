//打乱一个数组
Array.prototype.shuffle = function () {
    var array = this;
    var m = array.length,
        t, i;
    while (m) {
        i = Math.floor(Math.random() * m--);
        t = array[m];
        array[m] = array[i];
        array[i] = t;
    }
    return array;
}

var turntable = {
    lightNum: 18, // 灯泡数量
    lightWrap: null, //转盘容器
    turntable: null, //转盘,
    pointer: null, //指针
    itemNum: [
        {
            type: 0,
            prize: '谢谢惠顾',
            pro: [1, 50]
        },
        {
            type: 1,
            prize: '1块',
            pro: [51, 65]
        },
        {
            type: 1,
            prize: '1块',
            pro: [66, 80]
        },
        {
            type: 1,
            prize: '2块',
            pro: [81, 88]
        },
        {
            type: 1,
            prize: '2块',
            pro: [89, 96]
        },
        {
            type: 1,
            prize: '5块',
            pro: [97, 100]
        }
    ], //转盘内容
    bgWrap: null, //转盘背景容器
    giftWrap: null, //转盘奖品内容容器
    classMap: ['no-gift', ''],
    isGoing: false, //转盘是否开始
    result: null,//中奖结果
    init: function () {
        var proList = [];
        for (var i = 1; i <= 100; i++) {
            proList.push(i);
        }
        proList.shuffle();//产生一个随机排序的1-100的数组
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
        this.bgWrap.style.transform = 'rotate(' + 360 / this.itemNum.length / 2 + 'deg)';

        //初始化转盘奖品内容
        var giftFragment = document.createDocumentFragment();
        for (var i = 0; i < this.itemNum.length; i++) {
            var giftItem = document.createElement('li');
            var deg = (360 / this.itemNum.length) * i;
            giftItem.className = this.classMap[this.itemNum[i].type];
            giftItem.style.transform = 'rotate(' + deg + 'deg)';
            var span = document.createElement('span');
            span.innerHTML = this.itemNum[i].prize;
            giftItem.appendChild(span);
            giftFragment.appendChild(giftItem);
        }
        this.giftWrap.appendChild(giftFragment);

        this.pointer.onclick = this.star.bind(this); //给指针绑定事件
    },
    star: function () {
        if (this.isGoing) return;
        this.isGoing = true;

        var ran = Math.ceil(Math.random() * 100); // 生成1-100的随机数

        for (var i = 0; i < this.itemNum.length; i++) {
            if (this.itemNum[i].pro[0] <= ran && ran <= this.itemNum[i].pro[1]) {
                var data = {
                    index: i,
                    prize: this.itemNum[i].prize
                };
                this.result = data;
                break;
            }
        }

        var rotateItemdeg = (this.itemNum.length - this.result.index) * (360 / this.itemNum.length); //最后一圈旋转角度
        var rotate = rotateItemdeg + 5 * 360; //总旋转角度
        var rotateSpeed = (rotateItemdeg / 360 * 1 + 5).toFixed(2); //旋转速度

        this.turntable.removeAttribute('style');//先重置转旋转角度
        setTimeout(function () {
            this.turntable.style.transform = 'rotate(' + rotate + 'deg)';
            this.turntable.style.transition = 'transform ' + rotateSpeed + 's ease-out';
        }.bind(this))

        setTimeout(function () {
            this.isGoing = false;
            alert('中奖结果：' + this.result.prize);
        }.bind(this), rotateSpeed * 1000 + 100); //setTimeout 需要动态绑定this，不然this会指向window
    }
}

turntable.turntable = document.getElementById('turntable');
turntable.lightWrap = document.getElementById('turntable-light');
turntable.bgWrap = document.getElementById('turntable_bg');
turntable.giftWrap = document.getElementById('turntable_gift');
turntable.pointer = document.getElementById('turntable_pointer');
turntable.init();
