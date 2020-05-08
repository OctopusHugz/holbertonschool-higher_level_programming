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
	char const *type = "";

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %lu\n", object->allocated);
	while (count < len)
	{
		type = Py_TYPE(object->ob_item[count])->tp_name;
		printf("Element %d: %s\n", count, type);
		if (strcmp(type, "bytes") == 0)
			printf("Found bytes!\n");
			/* print_python_bytes(p); */
		count++;
	}
}

/**
 * print_python_bytes - prints first bytes of a python object
 * @p: pointer to object to print
 **/

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	int size = PyBytes_Size(p), len = PyList_GET_SIZE(p), count = 0;

	if (count < len)
	{
		printf("[.] bytes object info\n");
		printf("  size: %d\n  trying string: %s\n", size, bytes->ob_sval);
		printf("  first 6 bytes: %s\n", (char *)bytes);
		count++;
	}
}
