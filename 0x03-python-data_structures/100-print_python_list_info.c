#include <Python.h>

/**
 * print_python_list_info - Prints basic information about python lists.
 * @p:A python object list.
 */
void print_python_list_info(PyObject *p)
{
	int size;
	int alloc;
	int c;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (c = 0; c < size; c++)
	{
		printf("Element %d: ", c);

		obj = PyList_GetItem(p, c);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
