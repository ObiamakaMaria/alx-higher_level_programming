#include <Python.h>

/**
 * print_python_list_info - This function prints basic info 
 * about a Python lists.
 * @p: A PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size;
	int alloc; 
	int z;

	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (z = 0; z < size; z++)
	{
		printf("Element %d: ", z);

		obj = PyList_GetItem(p, z);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
