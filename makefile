
python_files=$(shell fd -tf py$$)

f format: format_python_files

format_python_files: $(python_files)
	@black $^
