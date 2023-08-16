#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", PyBytes_AsString(p));

	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; ++i) {
		printf("%02x ", (unsigned char)bytes->ob_sval[i]);
	}
	printf("\n");
}
