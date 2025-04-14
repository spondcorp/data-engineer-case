dev-setup:
	@echo "INFO: Setting up development environment"
	uv sync --dev
	@echo "INFO: Execute source . venv/bin/activate to activate the virtual environment"

run_in_local:
	@echo "INFO: Running Flyte workflow in local environment"
	@echo "WARNING: Make sure to run 'dev-setup' before running this target"
	PWD=$(shell pwd)
	pyflyte run src/workflow.py daily_workflow \
		--data_dir_path=${PWD}/data \
		--output_dir_path=${PWD}/output
