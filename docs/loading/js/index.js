var canvas = void 0,ctx = void 0;

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

	var time = Date.now() * 0.001;
	var countA = 13;
	var countB = 5;
	var iCountA = 1 / countA;
	var iCountB = 1 / countB;
	var r = 120;
	var r2 = 40;
	for (var a = 0; a < countA; a++) {
		push();
		var ar = a * iCountA * TAU;
		rotateY(ar + time);
		translate(r, 0, 0);
		for (var b = 0; b < countB; b++) {
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