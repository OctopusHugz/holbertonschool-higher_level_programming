#include <Python.h>

void print_python_list(PyObject *p);

void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints a python list
 * @p: pointer to list to print
 **/

void print_python_list(PyObject *p)
{
	int len = PyList_Size(p), count = 0;
	PyListObject *object = (PyListObject *)p;

	printf("[*] Python List Info\n");
	printf("[*] Size of the Python List = %d\n[*] Allocated = %lu\n", len, object->allocated);
	while (count < len)
	{
		printf("Element %d: %s\n", count, Py_TYPE(object->ob_item[count])->tp_name);
		count++;
	}
}

/**
 * print_python_bytes - prints first bytes of a python object
 * @p: pointer to object to print
 **/

void print_python_bytes(PyObject *p)
{
	if (p)
		printf("[.] bytes object info\n");
	return;
}
