let canvas, ctx;

function setup() {
	canvas = createCanvas(windowWidth, windowHeight, WEBGL);
	ctx = canvas.drawingContext;
}

function draw() {
	background(0);
	
	// ambientLight(48, 0, 0);
	pointLight(255, 255, 255, 255, 400, 200, 100);
	
	// noStroke();
	// specularMaterial(255, 255, 255);
	stroke(255);
	fill(0);
	
	rotateX(-PI * 0.25);
	
	let time = Date.now() * 0.001;
	let countA = 13;
	let countB = 5;
	let iCountA = 1 / countA;
	let iCountB = 1 / countB;
	let r = 120;
	let r2 = 40;
	for(let a = 0; a < countA; a++) {
		push();
		let ar = a * iCountA * TAU;
		rotateY(ar + time);
		translate(r, 0, 0);
		for(let b = 0; b < countB; b++) {
			push();
			rotateZ(b * iCountB * TAU - ar * iCountB + time);
			translate(r2, 0, 0);
			box(120, 60, 60);
			pop();
		}
		pop();
	}
}

function windowResized() {
	resizeCanvas(windowWidth, windowHeight);
}