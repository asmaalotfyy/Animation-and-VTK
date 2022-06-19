#include <math.h>
#include <GL/glut.h>
#include "glm.h"

static float fingerBase = 0.0, fingerUp = 0.0, rhip = 0.0, rhip2 = 0.0, rknee = 0.0, lknee = 0.0, lhip = 0.0, lhip2 = 0.0, lmove = 0.0, Dmove = 0.0, umove = 0.0, Umove = 0.0, dmove = 0.0, rmove = 0.0;
static int shoulder = 0, elbow = 0, shoulderAngle = 0, shoulder2 = 0, elbow2 = 0, shoulderAngle2 = 0;
static int r_thigh = 0, R_thigh = 0, l_thigh = 0, L_thigh = 0, r_knee = 0, l_knee = 0;
static int fullbody = 0;
int moving, startx, starty;

GLfloat angle = 180.0;   /* in degrees */
GLfloat angle2 = 0.0;   /* in degrees */


double eye[] = { 0, 0, -8 };
double center[] = { 0, 0, 1};
double up[] = { 0, 1, 0 };

double perpendicular[] = { 0,0,-21 };
double c[] = { 0,0,0 };
double direction[] = { 0,0,0 };
float speed = 0.1;
int poses[5][11] = { {0,0,0,0,0,0,0,0,0,0,0},
{0,0,0,0,0,25,0,-35,0,0,0},
{0,0,0,0,0,35,5,-20,-20,0,0},
{0,0,0,0,0,15,0,-10,-15,0,-30},
{0,0,0,0,0,15,-10,0,-15,0,-10},
};

//const char* modelname = "data/monitorLCD.obj";
const char* modelname = "data/bureau3.obj";
//const char* modelname1 = "data/oriental-rug.obj";
//const char* modelname2 = "data/bureau3.obj";
//const char* modelname3 = "data/apple-ibook-2001.obj";
//const char* modelname4 = "data/lamp_office.obj";

GLfloat light_ambient[] = { 0.0, 0.0, 0.0, 0.0 };
GLfloat light_diffuse[] = { 1.0, 1.0, 1.0, 1.0 };
GLfloat light_specular[] = { 1.0, 1.0, 1.0, 1.0 };

GLfloat light0_position[] = { 0, 0 , 2.0, 1.0 };

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void drawArm()
{
	glPushMatrix();
	glRotatef((GLfloat)shoulderAngle, 1.0, 0.0, 0.0);
	glRotatef((GLfloat)shoulder, 0.0, 0.0, 1.0);
	glTranslatef(1.0, 0.0, 0.0);
	glPushMatrix();
	glScalef(1.3, 0.2, 0.15);
	glutWireCube(1.0);
	glPopMatrix();

	glTranslatef(-0.7, 0.0, 0.0);
	glRotatef((GLfloat)elbow, 0.0, 0.0, 1.0);
	glTranslatef(1.0, 0.0, 0.0);
	glPushMatrix();
	glScalef(0.4, 0.2, 0.15);
	glutWireCube(1.0);
	glPopMatrix();
	glPopMatrix();
}
void drawRobot(void)
{
	glPushMatrix();
	glTranslatef(3.0, 0.0, 3);
	glRotatef(GLfloat(fullbody), 0, 1, 0);
	glTranslatef(-3.0, 0.0, -1.3);
	//Head
	glPushMatrix();
	glTranslatef(0.0, 1.5, 0.0);
	glutSolidSphere(0.4, 10.0, 10.0);
	glPopMatrix();
	//Legs
	glPushMatrix();
	glTranslatef(-0.5, -1.45, 1.0);
	glRotatef(GLfloat(L_thigh), 0, 0, 1);
	glTranslatef(0.5, 2.0, -1.0);
	glTranslatef(0.0, -2.0, 0.0);
	glRotatef(GLfloat(l_thigh), 1, 0, 0);
	glTranslatef(0.0, 2.0, 0.0);
	glPushMatrix();
	glScalef(0.2, 1.2, 0.15);
	glTranslatef(-1.5, -1.8, 0.0);
	glutWireCube(1);//left thigh
	glPopMatrix();
	glTranslatef(0.0, -4.2, 0.0);
	glRotatef(GLfloat(l_knee), 1, 0, 0);
	glTranslatef(0.0, 4.2, 0.0);
	glPushMatrix();

	glScalef(0.2, 0.8, 0.15);
	glTranslatef(-1.5, -2.5, 0.0);
	glutWireCube(1);//left lower leg
	glPopMatrix();
	glTranslatef(0.15, -3, 0.0);
	glScalef(0.3, 0.3, 0.15);
	glTranslatef(-1.5, 0.0, 0.0);
	glutSolidCube(1);//left feet
	glPopMatrix();
			//Right
	glPushMatrix();
	glTranslatef(0.5, -1.45, 1.0);
	glRotatef(GLfloat(R_thigh), 0, 0, 1);
	glTranslatef(-0.5, 2.0, -1.0);
	glTranslatef(0.0, -2.0, 0.0);
	glRotatef(GLfloat(r_thigh), 1, 0, 0);
	glTranslatef(0.0, 2.0, 0.0);
	glPushMatrix();
	glScalef(0.2, 1.2, 0.15);
	glTranslatef(1.5, -1.8, 0.0);
	glutWireCube(1);//right thigh
	glPopMatrix();
	glTranslatef(0.0, -4.2, 0.0);
	glRotatef(GLfloat(r_knee), 1, 0, 0);
	glTranslatef(0.0, 4.2, 0.0);
	glPushMatrix();

	glScalef(0.2, 0.8, 0.15);
	glTranslatef(1.5, -2.5, 0.0);
	glutWireCube(1);//right lower leg
	glPopMatrix();
	glTranslatef(0.0, -3, 0.0);
	glScalef(0.3,0.3,0.15);
	glTranslatef(0.9, 0.0, 0.0);
	glutSolidCube(1);//right feet
	glPopMatrix();
	//Body
	glPushMatrix();
	glScalef(1.0, 1.7, 0.5);
	glutWireCube(1.0);
	glPopMatrix();
	//Arms
	glPushMatrix();
	glTranslatef(-0.65, 1, 0.0);
	glRotatef(-90, 0, 0, 1);
	drawArm();
	glPopMatrix();
	glPushMatrix();
	glTranslatef(0.65,1,0);
	glRotatef(90, 0, 0, 1);
	glRotatef(180, 0, 1, 0);
	drawArm();
	glPopMatrix();
	glPopMatrix();
	glPopMatrix();
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


void drawmodel(char* filename)
{
	GLMmodel* model = glmReadOBJ(filename);
	glmUnitize(model);
	glmFacetNormals(model);
	glmVertexNormals(model, 90.0);
	glmScale(model, .15);
	glmDraw(model, GLM_SMOOTH | GLM_MATERIAL);
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void init(void)
{
	glMatrixMode(GL_PROJECTION);
	gluPerspective(65.0, (GLfloat)1024 / (GLfloat)869, 1.0, 60.0);

}

void crossProduct(double a[], double b[], double c[])
{
	c[0] = a[1] * b[2] - a[2] * b[1];
	c[1] = a[2] * b[0] - a[0] * b[2];
	c[2] = a[0] * b[1] - a[1] * b[0];
}

void normalize(double a[])
{
	double norm;
	norm = a[0] * a[0] + a[1] * a[1] + a[2] * a[2];
	norm = sqrt(norm);
	a[0] /= norm;
	a[1] /= norm;
	a[2] /= norm;
}

void reshape(int w, int h)
{
	glViewport(0, 0, (GLsizei)w, (GLsizei)h);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluPerspective(85.0, (GLfloat)w / (GLfloat)h, 1.0, 20.0);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glTranslatef(0.0, 0.0, -5.0);
}

void rotatePoint(double a[], double theta, double p[])
{

	double temp[3];
	temp[0] = p[0];
	temp[1] = p[1];
	temp[2] = p[2];

	temp[0] = -a[2] * p[1] + a[1] * p[2];
	temp[1] = a[2] * p[0] - a[0] * p[2];
	temp[2] = -a[1] * p[0] + a[0] * p[1];

	temp[0] *= sin(theta);
	temp[1] *= sin(theta);
	temp[2] *= sin(theta);

	temp[0] += (1 - cos(theta)) * (a[0] * a[0] * p[0] + a[0] * a[1] * p[1] + a[0] * a[2] * p[2]);
	temp[1] += (1 - cos(theta)) * (a[0] * a[1] * p[0] + a[1] * a[1] * p[1] + a[1] * a[2] * p[2]);
	temp[2] += (1 - cos(theta)) * (a[0] * a[2] * p[0] + a[1] * a[2] * p[1] + a[2] * a[2] * p[2]);

	temp[0] += cos(theta) * p[0];
	temp[1] += cos(theta) * p[1];
	temp[2] += cos(theta) * p[2];

	p[0] = temp[0];
	p[1] = temp[1];
	p[2] = temp[2];

}

void Left()
{
	rotatePoint(up, GLfloat(lmove), eye);
	lmove += 0.001;
}

void Right()
{
	rotatePoint(up, GLfloat(rmove), eye);
	rmove -= 0.001;
}

void Up()
{
	for (int i = 0; i < 3; i++)
	{
		perpendicular[i] = eye[i] - center[i];

	}

	crossProduct(up, perpendicular, c);
	normalize(c);

	rotatePoint(c, GLfloat(Umove), eye);
	rotatePoint(c, GLfloat(umove), up);
	Umove -= 0.001;
	umove -= 0.001;
}

void Down()
{
	for (int i = 0; i < 3; i++)
	{
		perpendicular[i] = eye[i] - center[i];

	}
	crossProduct(up, perpendicular, c);
	normalize(c);
	rotatePoint(c, GLfloat(dmove), eye);
	rotatePoint(c, GLfloat(dmove), up);
	dmove += 0.001;
}

void moveForward()
{
	direction[0] = center[0] - eye[0];
	direction[1] = center[1] - eye[1];
	direction[2] = center[2] - eye[2];
	eye[0] += direction[0] * speed;
	eye[1] += direction[1] * speed;
	eye[2] += direction[2] * speed;

	center[0] += direction[0] * speed;
	center[1] += direction[1] * speed;
	center[2] += direction[2] * speed;
}

void moveBack()
{
	direction[0] = center[0] - eye[0];
	direction[1] = center[1] - eye[1];
	direction[2] = center[2] - eye[2];
	eye[0] -= direction[0] * speed;
	eye[1] -= direction[1] * speed;
	eye[2] -= direction[2] * speed;

	center[0] -= direction[0] * speed;
	center[1] -= direction[1] * speed;
	center[2] -= direction[2] * speed;
}

void reset()
{
	double e[] = { 0.0, 0.0, 1.0 };
	double c[] = { 0.0, 0.0, 0.0 };
	double u[] = { 0.0, 1.0, 0.0 };
	for (int i = 0; i < 3; i++)
	{
		eye[i] = e[i];
		center[i] = c[i];
		up[i] = u[i];
	}
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void initRendering()
{
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
	glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient);
	glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse);
	glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular);
	glLightfv(GL_LIGHT0, GL_POSITION, light0_position);
	glEnable(GL_NORMALIZE);
	//Enable smooth shading
	glShadeModel(GL_SMOOTH);
	// Enable Depth buffer
	glEnable(GL_DEPTH_TEST);
}

void screen_menu(int value)
{

	switch (value)
	{
	case '0':
		break;
	case '1':
		modelname = "data/oriental-rug.obj";
		break;
	case '2':
		modelname = "data/bureau3.obj";
		break;
	case '3':
		modelname = "data/apple-ibook-2001.obj";
		break;
	case '4':
		modelname = "data/lamp_office.obj";
		break;
	case '5':
		modelname = "data/couchTwoSeats.obj";
		break;
	}
	reset();
	glutPostRedisplay();
}

void display(void)
{

	glClearColor(0.0, 0.0, 0.0, 0.0);
	// Clear Depth and Color buffers
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	gluLookAt(eye[0], eye[1], eye[2], center[0],
		center[1], center[2], up[0], up[1], up[2]);
	//glPushMatrix();
	glPushMatrix();
	glScalef(5, 5, 5);
	glColor3f(0.5f, 0.0f, 1.0f);
	drawmodel((char*)modelname);
	//glPopMatrix();
	//glPushMatrix();
	//glScalef(4, 4, 4);
	//glColor3f(1.0f, 1.0f, 1.0f);
	//drawmodel((char*)modelname2);
	//glPopMatrix();
	//glPushMatrix();
	//glScalef(0.5, 0.5, 0.5);
	//glColor3f(0.0f, 0.0f, 0.0f);
	//drawmodel((char*)modelname3);
	//glPopMatrix();
	//glPushMatrix();
	//glScalef(0.5, 0.5, 0.5);
	//glColor3f(1.0f, 0.0f, 0.0f);
	//drawmodel((char*)modelname4);
	//glPopMatrix();
	glPopMatrix();
	glRotatef(angle2, 1.0, 0.0, 0.0);
	glRotatef(angle, 0.0, 1.0, 0.0);
	drawRobot();
	glutSwapBuffers();
}

void specialKeys(int key, int x, int y)
{
	switch (key)
	{
	case GLUT_KEY_LEFT: Left(); break;
	case GLUT_KEY_RIGHT: Right(); break;
	case GLUT_KEY_UP: Up(); break;
	case GLUT_KEY_DOWN: Down(); break;
	}
	glutPostRedisplay();
}

void keyboard(unsigned char key, int x, int y)
{
	switch (key)
	{
	case 'f':
		moveForward();
		glutPostRedisplay();
		break;
	case 'b':
		moveBack();
		glutPostRedisplay();
		break;
	case 's':
		if (shoulder < 180)
		{
			shoulder = (shoulder + 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'S':
		if (shoulder > 0)
		{
			shoulder = (shoulder - 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'e':
		if (elbow < 150)
		{
			elbow = (elbow + 5) % 90;
			glutPostRedisplay();
		}
		break;
	case 'E':
		if (elbow > 0)
		{
			elbow = (elbow - 5) % 90;
			glutPostRedisplay();
		}
		break;
	case 'a':
		shoulderAngle = (shoulderAngle + 5) % 90;
		glutPostRedisplay();
		break;
	case 'A':
		if (shoulderAngle > -1)
		{
			shoulderAngle = (shoulderAngle - 5) % 90;
			glutPostRedisplay();
		}
		break;
	case 'q':
		if (r_thigh < 90)
		{
			r_thigh = (r_thigh + 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'Q':
		if (r_thigh > -90)
		{
			r_thigh = (r_thigh - 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'n':
		if (R_thigh < 90)
		{
			R_thigh = (R_thigh + 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'N':
		if (R_thigh > 0)
		{
			R_thigh = (R_thigh - 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'k':
		if (r_knee < 90)
		{
			r_knee = (r_knee + 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'K':
		if (r_knee > 0)
		{
			r_knee = (r_knee - 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'c':
		if (l_thigh < 90)
		{
			l_thigh = (l_thigh + 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'C':
		if (l_thigh > 0)
		{
			l_thigh = (l_thigh - 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'j':
		if (L_thigh > -90)
		{
			L_thigh = (L_thigh - 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'J':
		if (L_thigh < 0)
		{
			L_thigh = (L_thigh + 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'm':
		if (l_knee < 90)
		{
			l_knee = (l_knee + 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'M':
		if (l_knee > 0)
		{
			l_knee = (l_knee - 5) % 360;
			glutPostRedisplay();
		}
		break;
	case 'x':
		fullbody = (fullbody + 3) % 360;
		glutPostRedisplay();
		break;
	case 'X':
		fullbody = (fullbody - 3) % 360;
		glutPostRedisplay();
		break;
	case'r':
		shoulder = 0;
		shoulder2 = 0;
		elbow = 0;
		elbow2 = 0;
		L_thigh = 0;
		l_thigh = 0;
		R_thigh = 0;
		r_thigh = 0;
		l_knee = 0;
		r_knee = 0;
		fullbody = 0;
		break;
	default:
		break;
	}
}

static void mouse(int button, int state, int x, int y)
{
	if (button == GLUT_LEFT_BUTTON) {
		if (state == GLUT_DOWN) {
			moving = 1;
			startx = x;
			starty = y;
		}
		if (state == GLUT_UP) {
			moving = 0;
		}
	}
}

static void motion(int x, int y)
{
	angle = angle + (x - startx);
	angle2 = angle2 + (y - starty);
	startx = x;
	starty = y;
	glutPostRedisplay();
}

void attachMenu()
{
	glutCreateMenu(screen_menu);
	glutAddMenuEntry("Models", 0);
	glutAddMenuEntry("", 0);
	//glutAddMenuEntry("Al Capone", '1');
	//glutAddMenuEntry("Soccerball", '2');
	//glutAddMenuEntry("Rose", '3');
	//glutAddMenuEntry("Pc", '4');
	glutAddMenuEntry("Rug", '1');
	glutAddMenuEntry("Desk", '2');
	glutAddMenuEntry("Apple laptop", '3');
	glutAddMenuEntry("Desk lamp", '4');
	glutAddMenuEntry("Couch", '5');
	glutAttachMenu(GLUT_RIGHT_BUTTON);
}
void setposes(int frameNum)
{
	shoulder = poses[frameNum][0];
	shoulder2 = poses[frameNum][1];
	elbow = poses[frameNum][2];
	fingerBase = poses[frameNum][3];
	fingerUp = poses[frameNum][4];
	rhip = poses[frameNum][5];
	rhip2 = poses[frameNum][6];
	rknee = poses[frameNum][7];
	lhip = poses[frameNum][8];
	lhip2 = poses[frameNum][9];
	lknee = poses[frameNum][10];
}
static int f = 0;
void timer(int value)
{
	f = f % 5;
	setposes(f);
	f++;
		glutPostRedisplay();
	glutTimerFunc(150, timer, 0);
}
int main(int argc, char** argv)
{

	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(800, 800);
	glutInitWindowPosition(100,100);
	glutCreateWindow("Model");
	initRendering();
	glMatrixMode(GL_PROJECTION);
	gluPerspective(60, 1.0, 0.1, 10);
	attachMenu();
	glutDisplayFunc(display);
	glutMouseFunc(mouse);
	glutMotionFunc(motion);
	glutSpecialFunc(specialKeys);
	glutKeyboardFunc(keyboard);
	glutTimerFunc(0, timer, 0);
	glutMainLoop();
	return 0;
}
