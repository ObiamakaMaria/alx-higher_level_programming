#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list object.
 * @p: The Python list object.
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	PyObject *element_type = (size > 0) ? PyList_GET_ITEM(p, 0) : NULL;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GET_ITEM(p, i);

		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object.
 * @p: The Python bytes object.
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  [.] size: %zd\n", PyBytes_Size(p));
	printf("  [.] trying string: %s\n", PyBytes_AsString(p));
	printf("  [.] first %zd bytes: ", (PyBytes_Size(p) < 10) ? PyBytes_Size(p) : 10);
	for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; ++i)
	{
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
		if (i < PyBytes_Size(p) - 1 && i < 9)
		{
			printf(" ");
		}
	}
	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object.
 * @p: The Python float object.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	double value = PyFloat_AsDouble(p);

	printf("[.] float object info\n");
	printf("  [.] value: %lf\n", value);
}
