let width = 720;
let height = 720;
let scale = 10;
function setup(){
    createCanvas(width,height);
}
function mouseWheel(event) {
    background(255)
    event.deltaY < 0?scale-=2:scale+=2;
    if(scale <= 0){
        scale = 10
    }
}
function draw(){
    let curHeight = 0;
    let curWidth = 0;
    let stepWidth = width / scale;
    let stepHeight = height / scale;

    let c = color(0, 126, 255);
    for(let i=-scale/2;i<scale/2;i++){
        i==0?stroke(0):stroke(125);
        line(0,curHeight, width,curHeight)
        line(curWidth,0, curWidth,height)
        curHeight+=stepHeight;
        curWidth+=stepWidth;
    }
    let curY = 0;
    for(let l=-scale/2;l<=scale/2;l++){
        text(l, curWidth/2, curY);
        curY+=stepHeight;
    }
    let curX = 0;
    for(let l=-(scale/2);l<=scale/2;l++){
        text(l, curX, curHeight/2);
        curX+=stepWidth;
    }
}
