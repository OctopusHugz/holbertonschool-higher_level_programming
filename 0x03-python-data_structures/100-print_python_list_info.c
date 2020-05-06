#include <Python.h>

/**
 * print_python_list_info - prints info about the objects in a python list
 * @p: pointer to the python object containing all objects
 **/

void print_python_list_info(PyObject *p)
{
	int len = PyList_Size(p);
	int count = 0;
	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of the Python List = %d\n[*] Allocated = %lu\n", len, object->allocated);
	while (count < len)
	{
		printf("Element %d: %s\n", count, Py_TYPE(object->ob_item[count])->tp_name);
		count++;
	}
}
