let width = 500;
let height = 500;
let scaleFactor = 1.0;

// center coordinates
let centX = 0;
let centY = 0;

// translates
let transX = 0;
let transY = 0;

// infinite graph
let xMove = 0;
let yMove = 0;

// cells
let cellW = 10;
let cellH = 10;

let strWeight = 1;

// zooming
var zoom = 5.00;
var zMin = 0.05;
var zMax = 10.00;
var sensativity = 0.05;

let figures = [];

function setup() {
    createCanvas(width,height);
}

function drawCoordinates() {
    stroke(150);
    strokeWeight(strWeight / zoom);


    let halfW = width /  2;
    let halfH = height / 2;

    // infinite graph
    xMove = transX % cellW;
    yMove = transY % cellH;

    console.log(halfH + " - " + yMove + " - " + centY)
    // draw Xs
    for (var i = -halfH; i < halfH; i += cellH) {
        i+yMove == centY ? stroke(0) : stroke(150);
        line(-halfW+xMove, i+yMove, halfW+xMove, i+yMove);
    }

    // draw Ys
    for (var i = -halfW; i < halfW; i += cellW) {
        i+xMove == centX ? stroke(0) : stroke(150);
        line(i+xMove, -halfH+yMove, i+xMove, halfH+yMove);
    }
}

function draw() {
    background(255);
    translate(width/2, height/2);
    
    scale(zoom)

    drawCoordinates()
    drawObjects()
}

function mouseWheel(event) {
    zoom -= sensativity * event.delta;
    zoom = constrain(zoom, zMin, zMax);
    return false;
}

function mouseDragged() {
    transX += mouseX - pmouseX;
    transY += mouseY - pmouseY;
    centX += mouseX - pmouseX;
    centY += mouseY - pmouseY;
}

function drawRes(res){
    figures = [];
    let myPoints = JSON.parse(res);
    for(var p of myPoints) {
        figures.push(p);
    }
}

function drawObjects(){
    let len = figures.length
    for(let i=0;i<len - 1;i++){
        stroke(0);
        strokeWeight(strWeight / zoom);
        if(i == len - 2 && len > 2) {
            line(figures[i+1].pointX*cellW+transX, -figures[i+1].pointY*cellH+transY,
                figures[0].pointX*cellW+transX, -figures[0].pointY*cellH+transY);
        }
        line(figures[i].pointX*cellW+transX, -figures[i].pointY*cellH+transY,
        figures[i+1].pointX*cellW+transX, -figures[i+1].pointY*cellH+transY);
    }
}