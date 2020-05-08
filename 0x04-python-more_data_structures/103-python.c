#include <Python.h>

void print_python_list(PyObject *p);

void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints a python list
 * @p: pointer to list to print
 **/

void print_python_list(PyObject *p)
{
	PyTypeObject *object = (PyTypeObject *)p;
	int len = object->tp_itemsize;

	printf("%d", len);
}

/**
 * print_python_bytes - prints first bytes of a python object
 * @p: pointer to object to print
 **/

void print_python_bytes(PyObject *p)
{
	PyTypeObject *object = (PyTypeObject *)p;
	int len = object->tp_itemsize;

	printf("%d", len);
}
