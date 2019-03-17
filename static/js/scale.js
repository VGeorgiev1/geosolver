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
let zoomSensitivity = 0.1;
let fontSize = 10;
let strWeight = 1;
let curWidth = 0;
let curHeight = 0;
let centX = 0;
let centY = 0;
let figures = [];

function setup(){
    createCanvas(width,height);
}

function drawRes(res){
    figures = [];
    let myPoints = JSON.parse(res);
    for(var p of myPoints) {
        figures.push(p);
    }
}
function mouseDragged() {
    translateX += mouseX - pmouseX;
    translateY += mouseY - pmouseY;
    centX += mouseX - pmouseX;
    centY -= mouseY - pmouseY;
}
function mouseWheel(event) {
    event.preventDefault();
    let delta = 1 - event.delta * zoomSensitivity;
    if((scaleFactor * delta) > 1){
        scaleFactor*=delta;
        translateX -= mouseX;
        translateY -= mouseY;
        translateX *= delta;
        translateY *= delta;
        translateX += mouseX;
        translateY += mouseY;
    }else{
        scaleFactor = 1.0;
    }
    return false;
}
function drawObjects(stepWidth, stepHeight){
    let len = figures.length
    for(let i=0;i<len - 1;i++){
        stroke(0);
        strokeWeight(strWeight / scaleFactor);
        if(i == len - 2 && len > 2) {
            line(figures[i+1].pointX*stepWidth+360, -figures[i+1].pointY*stepHeight+360,
                figures[0].pointX*stepWidth+360, -figures[0].pointY*stepHeight+360);
        }
        line(figures[i].pointX*stepWidth+360, -figures[i].pointY*stepHeight+360,
        figures[i+1].pointX*stepWidth+360, -figures[i+1].pointY*stepHeight+360);
    }
}
function drawLabels(step){
    textSize(fontSize/scaleFactor);

    let curX = 0;
    let coordWidth = width/step/2;
    for(let i = -coordWidth; i < coordWidth; i++){
        text(i*step, curX, height/2);
        curX+=step;
    }
    let curY = 0;
    let coordHeight = height/step/2;
    for(let i = -coordHeight; i < coordHeight; i++){
        text(-i*step, width/2, curY);
        curY+=step;
    }
}

function drawCoordinates(step){
    curWidth = 0;
    curHeight = 0;
    // draw X
    // curWidth = translateX % scale_z;
    // curHeight = translateY % scale_z;
    for(let i=0;i<Math.ceil(height / step);i++){
        i==Math.floor(Math.floor(height / step)/2)?stroke(0):stroke(200);
        strokeWeight(strWeight / scaleFactor);
        line(0,curHeight, width,curHeight);
        curHeight+=step;
        curWidth+=step;
    }

    curWidth = 0;
    curHeight = 0;
    // draw Y
    // curWidth = translateX % scale_z;
    // curHeight = translateY % scale_z;
    for(let i=0;i<Math.ceil(width / step);i++){
        i==Math.floor(Math.floor(width / step)/2)?stroke(0):stroke(200);
        strokeWeight(strWeight / scaleFactor);
        line(curWidth, 0, curWidth, height);
        curHeight+=step;
        curWidth+=step;
    }
}

let old_factor = scaleFactor;
function draw(){
    // console.log(centX + " - " + centY)
    background(255);
    translate(translateX, translateY);
    scale(scaleFactor);

    if(scaleFactor > old_factor * 2){
        old_factor = scaleFactor;
    }else if(old_factor > scaleFactor * 2){
        old_factor = scaleFactor;
    }
    
    let step = (Math.ceil(width / (scale_z * old_factor)));

    drawCoordinates(step);
    drawLabels(step);
    drawObjects(step, step);
}
