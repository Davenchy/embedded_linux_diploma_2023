typedef int (*callback)();

int add(int a, int b) {
	return a + b;
}

void addl(int a, int b, int *c) {
	*c = add(a, b);
}

int callme() {
	return 0;
}

callback callme_wraper() {
	return callme;
}

void my_func(float demo, int data[10]) {}


int main(int argc, char *argv[], char *envp[]) {
	int c;

	addl(1, 2, &c);
	return 0;
}
