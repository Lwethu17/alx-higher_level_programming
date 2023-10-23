#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - Gives the info of the PyFloatObject.
 * @p: Pointer to the PyObject
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  val: %s\n", str);
}

/**
 * print_python_bytes -Gives the info of the PyBytesObject.
 * @p: Pointer to the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t tmp = 0;
	Py_ssize_t index = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	tmp = PyBytes_Size(p);
	printf("  size: %zd\n", tmp);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", tmp < 10 ? tmp + 1 : 10);
	while (index < tmp + 1 && index < 10)
	{
		printf(" %02hhx", str[index]);
		index++;
	}
	printf("\n");
}

/**
 * print_python_list - Gives the info of the PyListObject.
 * @p: Pointer to the PyObject.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t tmp = 0;
	PyObject *object;
	int n = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		tmp = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", tmp);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (n > tmp)
		{
			object = PyList_GET_ITEM(p, n);
			printf("Element %d: %s\n", n, object->ob_type->tp_name);
			if (PyBytes_Check(object))
				print_python_bytes(object);
			else if (PyFloat_Check(object))
					print_python_float(object);
			n++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
