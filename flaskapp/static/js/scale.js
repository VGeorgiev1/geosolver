let width = 720;
let height = 720;
let scale_z = 40;
let mx=0;
let my=0;
let wheelCount = 0;
let zoom=1;
let sensitivity = 0.5
let scaleFactor = 1.0;
let translateX = 0.0;
let translateY = 0.0;
let zoomSensitivity = 0.001
let fontSize = 10;
let strWeight = 1;
function setup(){
    createCanvas(width,height);
}
let figures = []
function drawRes(res){
    figures.push(JSON.parse(res))
}
function mouseDragged() {
    translateX += mouseX - pmouseX;
    translateY += mouseY - pmouseY;
}
function mouseWheel(event) {
    event.preventDefault();
    let delta = 1 - event.delta * zoomSensitivity;
    if((scaleFactor * delta) >1){
        scaleFactor*=delta
        translateX -= mouseX;
        translateY -= mouseY;
        translateX *= delta;
        translateY *= delta;
        translateX += mouseX;
        translateY += mouseY;
    }else{
        scaleFactor = 1.0
    }
    return false;
}
function drawObjects(stepWidth, stepHeight){
    for(let i=0;i<figures.length;i++){
        stroke(0)
        strokeWeight(strWeight / scaleFactor)
        line(figures[i].x1*stepWidth+360,-figures[i].y1*stepHeight+360,figures[i].x2*stepWidth+360,-figures[i].y2*stepHeight+360)
    }
}
function drawLabels(step){
    let curY = 0;
    for(let i=(width/step)/2; i>-width/step/2;i--){
        textSize(fontSize/scaleFactor)
        text(i, width/2, curY);
        curY+=step;
    }
    let curX = 0;
    for(let i=-(width/step)/2; i<width/step/2;i++){
        textSize(fontSize/scaleFactor)
        text(i, curX, height/2);
        curX+=step;
    }
}
let old_factor = scaleFactor
function draw(){
    background(255)
    translate(translateX, translateY);
    scale(scaleFactor);
    let curHeight = 0;
    let curWidth = 0;
    if(scaleFactor > old_factor * 2){
        old_factor = scaleFactor  
    }else if(old_factor > scaleFactor * 2){
        old_factor = scaleFactor
    }
    
    let step = (Math.ceil(width / (scale_z * old_factor)))

    for(let i=0;i<Math.ceil(width / step);i++){
        i==Math.floor(Math.floor(width / step)/2)?stroke(0):stroke(200);
        strokeWeight(strWeight / scaleFactor)
        line(0,curHeight, width,curHeight)
        line(curWidth,0, curWidth,height)
        curHeight+=step;
        curWidth+=step;
    }
    drawLabels(step)
}
