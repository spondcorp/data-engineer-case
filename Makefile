run_in_local:
	@echo "INFO: Running Flyte workflow in local environment"
	PWD=$(shell pwd)
	pyflyte run src/workflow.py daily_workflow \
		--data_dir_path=${PWD}/data \
		--output_dir_path=${PWD}/output
	