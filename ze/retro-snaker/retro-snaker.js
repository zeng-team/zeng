var grade = document.getElementById('grade');
var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');

//因为蛇跟食物都是方块构成，所以构造方块
function Rect(x, y, w, h, color) {
    this.x = x; //x轴
    this.y = y; //y轴
    this.width = w; //宽
    this.height = h; //高
    this.color = color; // 蛇跟食物是不同颜色
};

//画出方块
Rect.prototype.draw = function () {
    ctx.fillStyle = this.color;
    ctx.fillRect(this.x, this.y, this.width, this.height);
};

//构造蛇
function Snaker() {
    //存放整蛇的方块
    var snakerList = [];

    //设置刚开始蛇的长度：4
    for (var i = 0; i < 4; i++) {
        var rect = new Rect(i * 10, 0, 10, 10, 'black');
        //为了让蛇头始终在数组第一位，所以不能用push
        snakerList.splice(0, 0, rect);
    }

    //数组第一个为蛇头，并且为绿色
    snakerList[0].color = 'green';

    //设置头部跟整蛇数组为属性， 方便后续调用
    this.head = snakerList[0];
    this.snakerList = snakerList;

    //初始运动方向,向右,相当于按下右方向键
    this.direction = 39;
}

//画蛇的方法
Snaker.prototype.draw = function () {
    for (var i = 0; i < this.snakerList.length; i++) {
        this.snakerList[i].draw();
    }
};

//蛇移动的方法
Snaker.prototype.move = function () {
    //新生成一个方块覆盖蛇头，蛇头向前移一位
    var rect = new Rect(this.head.x, this.head.y, this.head.width, this.head.height, 'black');
    this.snakerList.splice(1, 0, rect);

    //如果有吃到食物就增加一个方块，并且生成新的食物，没有就蛇尾去掉一个方块,
    if (isEat()) {
        food = new Food();
        this.grade();
    } else {
        this.snakerList.pop();
    }

    //设置蛇头的运动方向，37 左，38 上，39 右，40 下
    switch (this.direction) {
        case 37:
            this.head.x -= this.head.width;
            break;
        case 38:
            this.head.y -= this.head.height;
            break;
        case 39:
            this.head.x += this.head.width;
            break;
        case 40:
            this.head.y += this.head.height;
            break;
        default:
            break;
    }

    //撞墙判断
    if (this.head.x > canvas.width || this.head.x < 0 || this.head.y > canvas.height || this.head.y < 0) {
        clearInterval(timer);
        drawText('GAME OVER！你撞墙啦！！！')
    }

    //撞自己判断，从1循环，避免跟头部比较
    for (var i = 1; i < this.snakerList.length; i++) {
        if (this.snakerList[i].x === this.head.x && this.snakerList[i].y === this.head.y) {
            clearInterval(timer);
            drawText('GAME OVER！你撞自己啦！！！')
        }
    }
};

var snaker = new Snaker();
snaker.draw();

var food = new Food();

// 定时器
var timer = setInterval(function () {
    ctx.clearRect(0, 0, canvas.width, canvas.height);//清空画布，然后重新绘制
    snaker.draw();
    snaker.move();
    food.draw();
}, 50);

//构建食物对象
function Food() {
    //判断食物是否出现在蛇身上
    var isOnSnaker = true;
    //设置食物随机出现的位置
    while (isOnSnaker) {//while循环，当isOnSnaker为true时再执行一次，比if好用
        isOnSnaker = false;
        var x = parseInt(random(0, canvas.width - 10) / 10) * 10; //食物的坐标只能是十的倍数，不然随机出现的食物可能跟蛇头的坐标对应不上
        var y = parseInt(random(0, canvas.height - 10) / 10) * 10;
        var rect = new Rect(x, y, 10, 10, 'red');
        for (var i = 0; i < snaker.snakerList.length; i++) {
            if (snaker.snakerList[i].x === rect.x && snaker.snakerList[i].y === rect.y) {
                isOnSnaker = true;
                break;
            }
        }
    }
    //返回Rect实例，使得Food的实例有draw方法
    return rect;
}

//键盘事件,if判断为了防止反方向
document.onkeydown = function (e) {
    var ev = e || window.event;
    switch (ev.keyCode) {
        case 37:
            if (snaker.direction !== 39) {
                snaker.direction = 37;
            }
            break;
        case 38:
            if (snaker.direction !== 40) {
                snaker.direction = 38;
            }
            break;
        case 39:
            if (snaker.direction !== 37) {
                snaker.direction = 39;
            }
            break;
        case 40:
            if (snaker.direction !== 38) {
                snaker.direction = 40;
            }
            break;
    }
    ev.preventDefault();
}

//随机函数,获得[min,max]范围的值
function random(min, max) {
    var range = max - min;
    var r = Math.random();
    return Math.round(r * range + min);
}

//判定吃到食物，即头部跟食物重合
function isEat() {
    if (snaker.head.x === food.x && snaker.head.y === food.y) {
        return true;
    } else {
        return false;
    }
}

//蛇的分数，即蛇数组长度-初始长度
Snaker.prototype.grade = function() {
    grade.innerHTML = '分数：' + (this.snakerList.length - 4);
};

//绘制文本
function drawText(text) {
    ctx.font = '20px serif';
    ctx.fillStyle = 'red'
    var textWidth = parseInt(ctx.measureText(text).width);//预先获取文本宽度，然后做到居中
    ctx.fillText(text, (canvas.width-textWidth)/2, (canvas.height-20)/2);
}