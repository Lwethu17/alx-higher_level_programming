#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - Gives the info of the PyFloatObject.
 * @p: The PyObject
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, n, limit;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (n = 0; n < limit; n++)
		if (string[n] >= 0)
			printf(" %02x", string[n]);
		else
			printf(" %02x", 256 + string[n]);

	printf("\n");
	setbuf(stdout, NULL);
}

/**
 * print_python_float - Prints float info
 * @p: The PyObject.
 */
void print_python_float(PyObject *p)
{
	double val;
	char *res;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	val = ((PyFloatObject *)(p))->ob_fval;
	res = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, Py_DTST_FINITE);

	printf("  value: %s\n", res);
	setbuf(stdout, NULL);
}

/**
 * print_python_list - Prints list info
 * @p: The PyObject.
 */
void print_python_list(PyObject *p)
{
	long int size;
	long int n;
	PyListObject *list;
	PyObject *object;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (n = 0; n < size; n++)
	{
		object = list->ob_item[n];
		printf("Element %ld: %s\n", m, ((object)->ob_type)->tp_name);

		if (PyBytes_Check(object))
			print_python_bytes(object);
		if (PyFloat_Check(object))
			print_python_float(object);
	}
	setbuf(stdout, NULL);
}
