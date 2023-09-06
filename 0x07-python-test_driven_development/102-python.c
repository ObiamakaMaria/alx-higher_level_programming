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
	if (!PyUnicode_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid String Object\n");
		return;
	}

	Py_ssize_t length = PyUnicode_GET_LENGTH(p);
	const char *type = PyUnicode_IS_COMPACT_ASCII(p) ?
		"compact ascii" :
		"compact unicode";
	const char *value = PyUnicode_AsUTF8(p);

	fprintf(stdout, "[.] string object info\n");
	fprintf(stdout, "  type: %s\n", type);
	fprintf(stdout, "  length: %zd\n", length);
	fprintf(stdout, "  value: %s\n", value);
}
/**
* main - Entry point of the program.
* This function initializes the Python interpreter, performs a series of
* test cases using the print_python_string function, and finalizes the
* Python interpreter.
*
* Return: Always 0.
*/
int main(void)
{
	PyObject *s;

	Py_Initialize();

	s = PyUnicode_DecodeUTF8("The spoon does not exist", 24, "strict");
	print_python_string(s);
	Py_DECREF(s);

	Py_Finalize();
	return (0);
}
