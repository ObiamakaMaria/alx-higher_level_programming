#include <Python.h>

/**
 * print_python_string - This function prints information about a
 * Python string object.
 * @p: Pointer to the Python object to be printed.
 *
 * This function checks if the provided Python object is a valid
 * string object, extracts its type, length, and value information,
 * and prints it to the standard output.
 * If the object is not a valid string, an error message is printed
 * to the standard error.
 */
void print_python_string(PyObject *p)
{
	long int string_len;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	string_len = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", string_len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &string_len));
}
