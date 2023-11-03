.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: start
start:	## Start server
	docker-compose build
	docker-compose up

.PHONY: test
test:	## Start tests
	docker exec code-union_web python3 manage.py test
