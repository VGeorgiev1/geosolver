let width = 720;
let height = 720;
let scale_z0 = 40;
let mx=0;
let my=0;
let wheelCount = 0;
let zoom=1;
let sensitivity = 0.5
let scaleFactor = 1.0;
let translateX = 0.0;
let translateY = 0.0;
let zoomSensitivity = 0.001
let fontSize = 20;
let strWeight = 1;
let rescale = false 
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
    if(event.delta > 0){
       rescale = true
    }
    let delta = 1 - event.delta * zoomSensitivity;
    if((scaleFactor * delta) >1){
        scaleFactor*=delta
       
        translateX -= mouseX;
        translateY -= mouseY;
        translateX *= delta;
        translateY *= delta;
        translateX += mouseX;
        translateY += mouseY;
        
    }
    return false;
}
function calculate() {
    console.log(translateX * scaleFactor)
}
function draw(){
    background(255)
    translate(translateX, translateY);
    scale(scaleFactor);
    const scale_z = scale_z0 // scaleFactor
    let curHeight = 0;
    let curWidth = 0;
    let stepWidth = width / (scale_z );
    let stepHeight = height / (scale_z );
    for(let i=0;i<figures.length;i++){
        stroke(0)
        strokeWeight(strWeight / scaleFactor)
        line(figures[i].x1*stepWidth+360,-figures[i].y1*stepHeight+360,figures[i].x2*stepWidth+360,-figures[i].y2*stepHeight+360)
    }
    
    let c = color(0, 126, 255);
    for(let i=-scale_z/2;i<scale_z/2;i++){
        i==0?stroke(0):stroke(125);
        strokeWeight(strWeight / scaleFactor)
        line(0,curHeight, width,curHeight)
        line(curWidth,0, curWidth,height)
        curHeight+=stepHeight;
        curWidth+=stepWidth;
    }
    let curY = 0;
    for(let l=-scale_z/2;l<=scale_z/2;l++){
        textSize(fontSize/scaleFactor)
        text(-l, curWidth/2, curY);
        curY+=stepHeight;
    }
    let curX = 0;
    for(let l=-(scale_z/2);l<=scale_z/2;l++){
        textSize(fontSize/scaleFactor)
        text(l, curX, curHeight/2);
        curX+=stepWidth;
    }
}
