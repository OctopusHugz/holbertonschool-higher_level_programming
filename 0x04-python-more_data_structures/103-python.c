#include <Python.h>

void print_python_list(PyObject *p);

void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints a python list
 * @p: pointer to list to print
 **/

void print_python_list(PyObject *p)
{
	int len = PyList_Size(p), count = 0, i = 0;
	PyListObject *object = (PyListObject *)p;
	PyObject *type;
	char const *type_name;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %lu\n", object->allocated);
	while (count < len)
	{
		type = PyList_GetItem(p, i);
		type_name = type->ob_type->tp_name;
		printf("Element %d: %s\n", count, type->ob_type->tp_name);
		if (strcmp(type_name, "bytes") == 0)
			print_python_bytes(type);
		count++, i++;
	}
}

/**
 * print_python_bytes - prints first bytes of a python object
 * @p: pointer to object to print
 **/

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	int size = PyBytes_Size(p), len = PyList_GET_SIZE(p), count = 0, i = 0;
	char *string;

	if (count < len)
	{
		string = bytes->ob_sval;
		printf("[.] bytes object info\n");
		if (size > 0)
		{
			printf("  size: %d\n  trying string: %s\n", size, string);
			printf("  first 6 bytes:");
			while (i < 6)
			{
				printf(" %02x", string[i]);
				i++;
			}
			putchar('\n');
			count++;
		}
		else
			return;
	}
}
