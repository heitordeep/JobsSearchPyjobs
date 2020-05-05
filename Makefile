SHELL=/bin/bash
PROJECT_NAME = SearchJobs


help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort


style:  ## Run isort and black auto formatting code style in the project
	@isort -m 3 -tc -y
	@black -S -t py37 -l 79 $(PROJECT_NAME)/. --exclude '/(\.git|\.venv|env|venv|build|dist)/'


requirements: ## Install project packages
	@pip install --upgrade pip
	@pip install -r requirements_dev.txt 


clean:  ## Clean python bytecodes, optimized files, cache, coverage...
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf
	@find . -name ".coverage" -type f | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@echo 'Temporary files deleted'

run: ## Run crawler
	cd crawl_jobs && scrapy crawl jobs
